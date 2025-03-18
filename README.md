```
# NewsSummarizationApp
A simple app using FastAPI and streamlit to summarize news articles

News Summarization & Text-to-Speech Application
🚀 A FastAPI & Streamlit-based web app that extracts news, analyzes sentiment, and generates Hindi TTS output.

📌 Features
🔍 News Extraction: Fetches the latest articles related to a company.
📊 Sentiment Analysis: Classifies articles as Positive, Neutral, or Negative.
🔗 Comparative Analysis: Highlights key differences across articles.
🗣 Text-to-Speech: Converts summary into Hindi audio.
🌐 User Interface: Simple Streamlit-based web UI.
🚀 Deployed on Hugging Face Spaces (if applicable).

#  Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create & Activate Virtual Environment
python -m venv .venv
Windows: 
.venv\Scripts\activate

macOS/Linux: source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run FastAPI Backend
uvicorn api.api:app --reload

Test API in the browser: http://127.0.0.1:8000/docs

5️⃣ Run Streamlit Frontend
In a new terminal, run:
streamlit run frontend/app.py

📂 Project Structure


📦 your-repo-name

├── 📂 api
│   ├── __init__.py
│   ├── api.py
│   ├── news_extractor.py
│   ├── sentiment_analysis.py
│   ├── comparative_analysis.py
│   ├── text_to_speech.py
├── 📂 frontend
│   ├── app.py
├── 📂 .venv
├── 📜 requirements.txt
├── 📜 README.md
└── 📜 .gitignore

```
