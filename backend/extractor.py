import os
import json
from typing import Dict, Any, List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_extraction_chain
from langchain_groq import ChatGroq
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

# Get API key from environment or use the provided one
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY")

# Set a default User-Agent
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.2-90b-vision-preview",
    temperature=0,
    max_tokens=2000,
    timeout=30,
    max_retries=3,
    api_key=GROQ_API_KEY
)

# Schema for e-commerce products
product_schema = {
    "properties": {
        "product_name": {
            "type": "string",
            "description": "The full name of the product"
        },
        "current_price": {
            "type": "string",
            "description": "The current selling price including currency symbol"
        },
        "original_price": {
            "type": "string",
            "description": "The original price before discount including currency symbol"
        },
        "discount_percentage": {
            "type": "string",
            "description": "The discount percentage if available"
        },
        "rating": {
            "type": "string",
            "description": "Product rating out of 5 stars"
        },
        "review_count": {
            "type": "string",
            "description": "Number of customer reviews"
        },
        "seller_name": {
            "type": "string",
            "description": "Name of the seller"
        },
        "available_offers": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of available offers and deals"
        },
        "product_highlights": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Key features and highlights of the product"
        }
    },
    "required": ["product_name", "current_price"]
}

async def extract_content(content: str, schema: Dict[str, Any]) -> Dict[str, Any]:
    """Extract structured data from content using LLM."""
    try:
        chain = create_extraction_chain(
            schema=schema,
            llm=llm
        )
        
        response = chain.invoke({"input": content})
        
        if response and isinstance(response, dict) and 'text' in response:
            return response['text']
        return None
        
    except Exception as e:
        print(f"Extraction error: {str(e)}")
        return None

async def extract_products_from_url(url: str) -> List[Dict[str, Any]]:
    """Extract product information from a URL."""
    try:
        print(f"Loading URL: {url}")
        loader = AsyncChromiumLoader([url])
        docs = await loader.aload()
        
        if not docs:
            print("No documents were loaded")
            return None
            
        print(f"Successfully loaded {len(docs)} documents")
        
        # Transform HTML
        bs_transformer = BeautifulSoupTransformer()
        docs_transformed = bs_transformer.transform_documents(
            docs,
            tags_to_extract=[
                "div", "span", "p", "h1", "h2", "section",
                "button", "li", "ul", "table", "tr", "td"
            ]
        )
        
        if not docs_transformed or not docs_transformed[0].page_content.strip():
            print("No usable content after transformation")
            return None
            
        print("Content transformed successfully")
        
        # Split into chunks
        splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=2000,
            chunk_overlap=200
        )
        splits = splitter.split_documents(docs_transformed)
        
        if not splits:
            print("No content after splitting")
            return None
            
        print(f"Split into {len(splits)} chunks")
        
        # Process chunks with meaningful content
        extracted_contents = []
        for split in splits:
            content = split.page_content.strip()
            if len(content) > 100:
                print("Attempting content extraction...")
                extracted_content = await extract_content(schema=product_schema, content=content)
                if extracted_content:
                    extracted_contents.extend(extracted_content)
        
        # Remove duplicates based on product_name
        unique_products = {}
        for product in extracted_contents:
            product_name = product.get("product_name")
            if product_name and product_name not in unique_products:
                unique_products[product_name] = product
        
        return list(unique_products.values())
        
    except Exception as e:
        print(f"Scraping error: {str(e)}")
        return []
