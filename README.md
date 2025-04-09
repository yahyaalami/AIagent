# 🧠 AI Agent Code Generator

This project is an intelligent code assistant that leverages **LlamaIndex**, **Ollama**, and local language models (`llama2`, `codellama`) to analyze documents, respond to prompts, and generate code in a structured format.

It supports:
- Reading API documentation (PDFs)
- Inspecting and summarizing local code files
- Generating new code files with explanations
- Saving output to disk

---

## 🚀 Features

- 🧠 Local LLM reasoning using Ollama (`llama2`, `codellama`)
- 📄 Parses and indexes PDF documentation
- 🧾 Reads and explains `.py` files
- ⚙️ Generates code with description and filename using a structured output format
- 💾 Saves generated code to the `output/` directory
- 🔁 Retry system for robust agent interactions

---

## 📁 Project Structure

### Folder & File Explanation

- **`ai/`**  
  Python virtual environment (optional). Recommended to isolate dependencies.

- **`data/`**  
  Folder where you place your input files:
  - `.pdf` → Documentation
  - `.py` → Source files the agent can read

- **`output/`**  
  Folder where the generated Python files are automatically saved.

- **`.env`**  
  Optional environment variables. Example:
  ```env
  LLAMA_CLOUD_API_KEY=your_key_here


---

## ⚙️ Requirements

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com) — local LLM server with `llama2` and `codellama` models pulled
- Git
- (Optional) [LlamaParse API key](https://cloud.llamaindex.ai) if you want to enable enhanced PDF parsing

---

## 🧱 Setup Instructions


### 1. Clone the repository

### 2.Create and activate a virtual environment
python -m venv ai

- Activate on Windows:
ai\Scripts\activate

- Or activate on Unix/Mac:
source ai/bin/activate

### 3.Install Python dependencies
- pip install -r requirements.txt

### 4. Pull Ollama models (if not already installed)
- ollama pull llama2
- ollama pull codellama



## 🧪 Running the App
python Main.py

### Example prompt:
+ read the content of test.py and explain what it does
+ analyze the API documentation in readme.pdf
+ send a post request to make a new item using api in python

### The agent will:
💬 Process your request
🧠 Understand your intent
💾 Save the generated code in the output/ directory
📄 Provide an explanation of what the code does


##  🔐.env Example (Optional):
LLAMA_CLOUD_API_KEY=your_api_key_here 
(You can get your API key from: https://cloud.llamaindex.ai)


## 📦 Dependencies
The most important packages in requirements.txt:
+ llama-index
+ llama-parse
+ ollama
+ python-dotenv
+ pydantic

You can generate the file automatically with:
- pip freeze > requirements.txt



# ✨ Credits
- Powered by LlamaIndex + Ollama
