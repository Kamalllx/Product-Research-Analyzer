import asyncio
import json
from extractor import extract_products_from_url
from research import search_research_papers, analyze_papers, download_paper

async def main():
    # Step 1: Get URL from user input
    url = input("Enter the product URL: ").strip()

    # Step 2: Extract products from URL
    print("\nExtracting product details...")
    products = await extract_products_from_url(url)

    if not products:
        print("No products found. Please try a different URL.")
        return

    # Step 3: Show extracted products to the user
    print("\nProducts found:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product.get('product_name', 'Unknown')} - {product.get('current_price', 'Price not available')}")

    # Step 4: Let user select a product
    choice = int(input("\nEnter the number of the product you want to analyze: ")) - 1
    if choice < 0 or choice >= len(products):
        print("Invalid choice. Exiting...")
        return

    selected_product = products[choice]
    print(f"\nSelected Product: {selected_product['product_name']}\n")

    # Step 5: Search for research papers
    print("Searching for related research papers...")
    papers = await search_research_papers(selected_product)

    if not papers:
        print("No research papers found.")
    else:
        print("\nResearch Papers Found:")
        for i, paper in enumerate(papers):
            print(f"{i + 1}. {paper['title']} ( {paper['url']} )")

    # Step 6: Perform AI Analysis
    print("\nPerforming AI-based analysis...")
    analysis_result = await analyze_papers(papers, selected_product)

    # Step 7: Display results
    print("\n====== Analysis Report ======")
    print(f"Product Name: {selected_product['product_name']}")
    print(f"Current Price: {selected_product.get('current_price', 'N/A')}")
    print(f"Original Price: {selected_product.get('original_price', 'N/A')}")
    print(f"Discount: {selected_product.get('discount_percentage', 'N/A')}")
    print(f"Rating: {selected_product.get('rating', 'N/A')} ⭐")
    print(f"Review Count: {selected_product.get('review_count', 'N/A')}")
    print("\nAvailable Offers:")
    for offer in selected_product.get("available_offers", []):
        print(f" - {offer}")

    print("\nProduct Highlights:")
    for highlight in selected_product.get("product_highlights", []):
        print(f" - {highlight}")

    print("\nResearch Papers:")
    for i, paper in enumerate(papers):
        print(f"{i + 1}. {paper['title']} - {paper['url']}")

    print("\nAI Analysis:")
    print(analysis_result)

if __name__ == "__main__":
    asyncio.run(main())
