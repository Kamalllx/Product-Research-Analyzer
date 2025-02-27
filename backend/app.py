from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
from extractor import extract_products_from_url
from research import search_research_papers, analyze_papers

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/analyze', methods=['POST'])
async def analyze():
    data = request.json
    url = data.get('url')
    product = data.get('product')

    if url:
        # Extract products from the URL
        products = await extract_products_from_url(url)
        return jsonify({"products": products})

    if product:
        # Search for research papers related to the product
        papers = await search_research_papers(product)
        # Analyze the papers for innovation potential
        analysis = await analyze_papers(papers, product)
        return jsonify({"papers": papers, "analysis": analysis})

    return jsonify({"error": "Invalid request"}), 400

# Helper function to run async functions in Flask
def run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

# Wrap the async route with a sync function for Flask
@app.route('/api/analyze-sync', methods=['POST'])
def analyze_sync():
    return run_async(analyze())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)