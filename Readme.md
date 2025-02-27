# Product Research Analyzer

A powerful tool to analyze products and research papers for innovation potential. This project integrates web scraping, AI-based analysis, and a modern frontend to provide actionable insights for product development.

---

## **Key Features**

- **Product Extraction**:
  - Extracts product details (name, price, rating, offers, etc.) from e-commerce URLs (Flipkart, Amazon, etc.).
  - Uses LangChain and Groq LLM for structured data extraction.

- **Research Paper Search**:
  - Searches for relevant research papers on arXiv based on product keywords.
  - Displays paper titles, summaries, authors, and download links.

- **AI Analysis**:
  - Analyzes research papers for innovation potential using Groq LLM.
  - Provides actionable insights for product improvement and market differentiation.

- **Modern UI**:
  - Built with **Next.js** and **shadcn/ui**.
  - Features vibrant gradients, animations, and smooth transitions.
  - Includes a text reveal effect for AI analysis results.

- **Download Research Papers**:
  - Allows users to download research papers in PDF format with a single click.

---

## **Tech Stack**

### **Frontend**
- **Next.js**: React framework for server-side rendering and static site generation.
- **shadcn/ui**: Modern UI components for a sleek design.
- **Framer Motion**: For animations and transitions.
- **Tailwind CSS**: Utility-first CSS framework for styling.

### **Backend**
- **Flask**: Lightweight Python web framework for API handling.
- **LangChain**: Framework for integrating LLMs into applications.
- **Groq LLM**: High-performance language model for AI-based analysis.
- **arXiv API**: For searching and retrieving research papers.

### **Other Tools**
- **aiohttp**: For asynchronous HTTP requests.
- **BeautifulSoup**: For HTML parsing and transformation.
- **asyncio**: For asynchronous programming in Python.

---

## **Process Flow**

1. **User Input**:
   - User enters a product URL (e.g., Flipkart or Amazon).

2. **Product Extraction**:
   - Backend scrapes the URL and extracts product details using LangChain and Groq LLM.

3. **Research Paper Search**:
   - Backend searches arXiv for research papers related to the product.

4. **AI Analysis**:
   - Backend analyzes the research papers using Groq LLM to generate insights.

5. **Frontend Display**:
   - Frontend displays the extracted products, research papers, and AI analysis in a modern UI.

6. **Download Research Papers**:
   - Users can download research papers in PDF format.

---

## **How to Run the App**

### **Prerequisites**
- Python 3.8+
- Node.js 16+
- npm or yarn

### **Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/product-research-analyzer.git
   ```

2. **Navigate to the Backend Directory**:
   ```bash
   cd product-research-analyzer/backend
   ```

3. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Backend**:
   ```bash
   python app.py
   ```
   - The backend will start on `http://localhost:5000`.

5. **Navigate to the Frontend Directory**:
   ```bash
   cd ../frontend
   ```

6. **Install Node.js Dependencies**:
   ```bash
   npm install
   ```

7. **Run the Next.js Frontend**:
   ```bash
   npm run dev
   ```
   - The frontend will start on `http://localhost:3000`.

8. **Access the Application**:
   - Open your browser and go to `http://localhost:3000`.

---

## **Acknowledgments**

- **LangChain**: For structured data extraction.
- **Groq**: For high-performance AI analysis.
- **arXiv**: For providing access to research papers.
- **Next.js** and **shadcn/ui**: For the modern frontend.

---
