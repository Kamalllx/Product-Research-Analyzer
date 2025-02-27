import os
import json
import requests
import arxiv
from typing import Dict, Any, List
from langchain.chains import create_extraction_chain
from langchain_groq import ChatGroq
import datetime
import aiohttp
import asyncio
from io import BytesIO

# Get API key from environment or use the provided one
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY")

# Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.2-90b-vision-preview",
    temperature=0,
    max_tokens=2000,
    timeout=30,
    max_retries=3,
    api_key=GROQ_API_KEY
)

async def search_research_papers(product_data: Dict) -> List[Dict]:
    """Search for relevant research papers based on product data."""
    print("\nSearching for relevant research papers...")
    
    # Extract key terms from product data
    keywords = product_data['product_name'].split()
    search_query = f"{' '.join(keywords)} innovation technology"
    
    # Search arXiv
    client = arxiv.Client()
    search = arxiv.Search(
        query=search_query,
        max_results=5,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    papers = []
    results = list(client.results(search))
    
    for result in results:
        paper = {
            'title': result.title,
            'summary': result.summary,
            'authors': [author.name for author in result.authors],
            'url': result.pdf_url,
            'published': str(result.published),
            'doi': result.doi if hasattr(result, 'doi') else None
        }
        papers.append(paper)
    
    return papers

async def analyze_papers(papers: List[Dict], product_data: Dict) -> str:
    """Analyze research papers for innovation potential and generate insights."""
    print("\nAnalyzing research papers for innovation potential...")
    
    analysis_prompt = f"""
    Product Context:
    {product_data['product_name']}
    
    Based on the following research papers, analyze:
    1. Potential technological innovations
    2. Implementation strategies
    3. Market impact and feasibility
    
    Papers to analyze:
    {json.dumps(papers, indent=2)}
    
    Additionally, provide actionable insights on how to integrate the research findings seamlessly into our product to make it the best in the market. Focus on:
    1. Specific features or functionalities that can be added or improved.
    2. Relevant technological enhancements from the research papers.
    3. Ways to achieve market differentiation and enhance customer satisfaction.
    """
    
    # Use Groq for analysis
    try:
        analysis = llm.invoke(analysis_prompt)
        # Extract textual content from the analysis
        if hasattr(analysis, "content"):
            analysis_content = analysis.content.strip()
        else:
            analysis_content = str(analysis).strip()
            
        return analysis_content
    except Exception as e:
        print(f"Error during analysis: {e}")
        return "Error: Unable to generate analysis."

async def download_paper(url: str, paper_id: str) -> str:
    """Download research paper as PDF and return the file path."""
    try:
        base_dir = "data/research_papers"
        os.makedirs(base_dir, exist_ok=True)
        
        filename = f"{base_dir}/paper_{paper_id}.pdf"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    with open(filename, 'wb') as f:
                        f.write(content)
                    print(f"Downloaded: {filename}")
                    return filename
                else:
                    print(f"Failed to download paper: HTTP {response.status}")
                    return None
                    
    except Exception as e:
        print(f"Error downloading paper: {str(e)}")
        return None
