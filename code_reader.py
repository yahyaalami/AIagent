from llama_index.core.tools import FunctionTool
import os

def code_reader_func(file_name: str) -> dict:
    path = os.path.join("data", file_name)
    if not os.path.exists(path):
        return {"error": f"File '{file_name}' not found in the data directory."}
    try:
        with open(path, "r") as f:
            return {"file_content": f.read()}
    except Exception as e:
        return {"error": str(e)}

code_reader = FunctionTool.from_defaults(
    fn=code_reader_func,
    name="code_reader",
    description="Reads the contents of a .py file from the ./data folder. Use when the user asks to read a specific code file."
)
