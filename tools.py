import os
import subprocess
import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool
from colors import tag, data, BLUE, GREEN, RED, RESET


# -------------------------------------------------------------------
# Tool Definitions
# -------------------------------------------------------------------
@tool
def fetch_web_page(url: str) -> str:
    """Reads and returns the text content of a web page/URL."""
    print(f"{tag('TOOL', BLUE)} fetch_web_page called with url={data(url)}")
    try:
        # For a local demo, we simulate fetching an untrusted URL
        # If testing live, ensure you point this to a mock local server or text file
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.get_text()
        return result
    except Exception as e:
        print(f"{tag('TOOL', RED)} fetch_web_page failed: {data(str(e))}")
        return f"Error fetching URL: {str(e)}"


@tool
def read_file(filename: str) -> str:
    """Reads and returns the content of a local file."""
    print(f"{tag('TOOL', BLUE)} read_file called with filename={data(filename)}")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            result = f.read()
            print(f"{tag('TOOL', GREEN)} read_file succeeded, read {data(len(result))} chars")
            return result
    except Exception as e:
        print(f"{tag('TOOL', RED)} read_file failed: {data(str(e))}")
        return f"Error reading file: {str(e)}"


@tool
def write_file(filename: str, content: str) -> str:
    """Writes or overwrites text/code content to a specific local file."""
    print(f"{tag('TOOL', BLUE)} write_file called with filename={data(filename)}, content_len={data(len(content))}")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{tag('TOOL', GREEN)} write_file succeeded, wrote {data(len(content))} chars to {data(filename)}")
        return f"Successfully wrote to {filename}"
    except Exception as e:
        print(f"{tag('TOOL', RED)} write_file failed: {data(str(e))}")
        return f"Error writing file: {str(e)}"


# llama3.1 is retarded and gives 'cmd' instead of 'command' for some reason, so we support both arg names
@tool
def execute_command(command: str = None, cmd: str = None) -> str:
    """Executes a command line / CLI instruction on the host system and returns output."""
    # Fallback in case the injected model guesses 'cmd' instead of 'command'
    actual_command = command or cmd

    if not actual_command:
        return "Error: No command provided to execute_command tool."

    print(f"{tag('TOOL', BLUE)} execute_command called with command={data(actual_command)}")
    try:
        result = subprocess.run(actual_command, shell=True, capture_output=True, text=True, timeout=10)
        print(f"{tag('TOOL', GREEN)} execute_command succeeded, exit_code={data(result.returncode)}")
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        print(f"{tag('TOOL', RED)} execute_command failed: {data(str(e))}")
        return f"Execution failed: {str(e)}"


# List of all available tools
tools = [fetch_web_page, read_file, write_file, execute_command]
