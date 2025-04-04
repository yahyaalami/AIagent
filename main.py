from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from prompts import context
from code_reader import code_reader
from dotenv import load_dotenv
from llama_index.core.tools import FunctionTool

# Load environment variables from .env
load_dotenv()

# Load LLM from Ollama (llama2, 120s timeout, no stream)
llm = Ollama(model="llama2", request_timeout=120.0, stream=False)

# Load PDF parser for extracting documentation
parser = LlamaParse(result_type="markdown")
file_extractor = {".pdf": parser}

# Load documents from the ./data directory
documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

# Use a lightweight local embedding model
embed_model = resolve_embed_model("local:sentence-transformers/all-MiniLM-L6-v2")

# Index the documents
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Query engine based on the indexed documentation
query_engine = vector_index.as_query_engine(llm=llm)

# Define tool to block the generic invalid `Tool` name
def invalid_tool(**kwargs):
    raise Exception("❌ Invalid tool used. You must use only 'code_reader' or 'api_documentation'.")

invalid = FunctionTool.from_defaults(
    fn=invalid_tool,
    name="Tool",
    description="This is an invalid tool name and should not be used."
)

# Register tools
tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="api_documentation",
            description="This tool answers technical questions using the API documentation (PDFs)."
        ),
    ),
    code_reader,
    invalid  # Optional: block invalid generic usage
]

# Create the reasoning agent with the tools
agent = ReActAgent.from_tools(
    tools=tools,
    llm=llm,
    verbose=True,
    context=context,
)

# Prompt loop
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    try:
        result = agent.query(prompt)
        print("\n🧠 Agent Response:\n", result, "\n")
    except Exception as e:
        print("⚠️ Error during agent execution:", e)
