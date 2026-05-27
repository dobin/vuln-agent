# vuln-agent

An **intentionally vulnerable AI agent** that demonstrates prompt injection attacks against LLM-powered coding assistants.

Code and readme are AI generated. 


## How it works

The agent uses [OpenRouter](https://openrouter.ai/) with **Meta Llama 3.1 (70B)** via LangChain. It is given tools to fetch web pages, read/write files, and execute shell commands. The goal is to show how untrusted web content can hijack the agent's behavior through prompt injection.

## Tools available to the agent

- `fetch_web_page` – fetches and returns text content from a URL
- `read_file` – reads local files
- `write_file` – writes/overwrites local files
- `execute_command` – runs arbitrary shell commands on the host

## Demo files

| File | Description |
|------|-------------|
| `web/demo1.txt` | Clean code example – **no** prompt injection |
| `web/demo2.txt` | Same code example but with a **prompt injection payload** that tricks the agent into running a shell command |

## Setup

1. Install dependencies (LangChain, requests, beautifulsoup4, etc.)
2. Set your OpenRouter API key:
   ```bash
   export OPENROUTER_API_KEY="your-key-here"
   ```

## Running the demo

1. Start a local HTTP server to serve the demo files:
   ```bash
   cd web/
   python3 -m http.server
   ```

2. In another terminal, run the agent:
   ```bash
   python3 vuln-agent.py
   ```

The agent will fetch `demo2.txt` from the local server, and the injected prompt will attempt to make the agent execute an arbitrary command via the `execute_command` tool – demonstrating how untrusted input can compromise an AI agent.
