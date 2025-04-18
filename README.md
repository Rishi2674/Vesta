

# 🏠 Vesta: Multi-Agent Real Estate Assistant

Vesta is an AI-powered chatbot designed for real estate platforms, capable of analyzing property issues via images/text and answering tenancy questions using LangGraph agents.

🌐 **Live Demo:** [https://vesta-x7zr.onrender.com/](https://vesta-x7zr.onrender.com/)

## 🔧 Tech Stack
- **Framework:** LangGraph
- **Backend:** FastAPI (Python)
- **Frontend:** React.js
- **LLM:** Groq API (Llama)
- **Deployment:** Render

## ✨ Features
1. **Multi-Agent System**:
   - 🖼️ **Visual Troubleshooter**: Analyzes property images + descriptions
     - Takes the input from user
     - Parses the input and image to the groq API, utilising  - meta-llama/llama-4-scout-17b-16e-instruct - model
     - System decides an automatic role and a custom pre defined prompt to identify the issues in the image.
   - 📚 **Tenancy Expert**: Answers legal/FAQ questions using tools:
     - Web search summarizer
        - generates a google search query from the given user text
        - executes the search using SERPapi and returns the JSON of web searches scraped
        - utilisies beautifulSoup to scrape the top links and extract the data
        - summarises the data scraped from the top links and returns to the user along with the links used.
     - Also answers based on past context and common knowledge.
     - Utilises the llama3-70b-8192 model from groq.

2. **Smart Routing**:
   - Automatically directs queries to the appropriate agent
   - Handles mixed image+text inputs
   - Uses LangGraph to automatically handle fallbacks based on trigger or image detections.
   - Sets the agent to "FAQ agent" initially but fallbacks on receiving certain triggers or detecting an image and calls "Image Agent".


## 🚀 Quick Start
```bash
# 1. Clone repo
git clone https://github.com/yourusername/vesta.git
cd vesta

# 2. Backend
cd app
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# 3. Frontend
cd ../frontend
npm install
npm start
```

## 🖼️ Example Workflow
1. User uploads image of cracked wall + description
2. Agent 1:
   - Identifies structural damage
   - Suggests repair options
3. User asks "What's the notice period in California?"
4. Agent 2:
   - Checks tenancy laws
   - Returns formatted answer

## 📁 Project Structure
```
/vesta
├── app/               # FastAPI backend       # API entry point
│   └── routers/
├── frontend/          # React app
│   ├── public/
│   └── src/           # React components
└── render.yaml        # Deployment config
```

## 🌐 Deployment
1. Push to GitHub
2. Connect repo to Render
3. Auto-deploy using `render.yaml`

## 🤝 Contributing
PRs welcome! Please:
1. Fork the repo
2. Create a feature branch
3. Submit PR with clear description

