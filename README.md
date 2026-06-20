# Agentic AI Research Assistant

An AI-powered research assistant that automates the research process by searching the web, extracting relevant content, generating structured research reports, and evaluating the quality of the generated output.

The project uses LangGraph to orchestrate an agentic workflow consisting of multiple specialized components that work together to produce reliable research reports.

---

## Features

- Search the web for recent and reliable information
- Extract and clean webpage content using web scraping
- Generate structured research reports
- Critically evaluate generated reports
- LangGraph-based workflow orchestration
- Modular architecture for easy scalability

---

## Workflow

The application follows this workflow:

```text
User Topic
    |
    v
Search Agent
    |
    v
Reader Agent
    |
    v
Writer Chain
    |
    v
Critic Chain
    |
    v
Final Output
```

### Components

#### Search Agent

- Searches the internet using Tavily Search API
- Retrieves recent and relevant information

#### Reader Agent

- Selects the most relevant resource
- Scrapes webpage content using BeautifulSoup

#### Writer Chain

- Combines gathered information
- Generates a professional research report

#### Critic Chain

- Evaluates the report
- Provides strengths, weaknesses and an overall score

---

## Tech Stack

### AI Frameworks

- LangChain
- LangGraph

### Language Models

- Mistral AI

### Tools

- Tavily Search API
- BeautifulSoup

### Backend

- Python

### UI

- Streamlit

### Utilities

- LCEL (LangChain Expression Language)
- Requests
- Python Dotenv

---

## Project Structure

```text
agentic-ai-research-assistant/

│
├── tools.py
├── agents.py
├── graph.py
├── app.py
├── requirements.txt
└── .env (for api)
```

### File Responsibilities

#### tools.py

Contains external tools used by agents.

- Web Search Tool (Tavily)
- Web Scraping Tool (BeautifulSoup)

#### agents.py

Contains AI agents and chains.

- Search Agent
- Reader Agent
- Writer Chain
- Critic Chain

#### graph.py

Contains the LangGraph workflow.

Responsible for:

- Defining state
- Creating nodes
- Connecting workflow steps
- Compiling the graph

#### app.py

Streamlit user interface.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/agentic-ai-research-assistant.git

cd agentic-ai-research-assistant
```

### Create a virtual environment

Using uv:

```bash
uv venv
```

Activate environment.

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
uv pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
TAVILY_API_KEY=your_api_key

MISTRAL_API_KEY=your_api_key
```

---

## Run the Application

### Streamlit UI

```bash
streamlit run app.py
```

### LangGraph Workflow

```bash
python graph.py
```

---

## Example Usage

Input:

```text
Latest advancements in Generative AI
```

Output:

```text
Research Report

Introduction

Key Findings

Conclusion

Sources

Critic Feedback

Score

Strengths

Areas to Improve

Verdict
```

---

## Concepts Implemented

- AI Agents
- Tool Calling
- LangGraph Workflow Orchestration
- LCEL
- Runnable Chains
- Prompt Engineering
- Web Scraping
- Research Automation

---

## Future Improvements

- Add PDF export functionality
- Add source citation cards
- Add downloadable reports
- Add report history
- Add multiple LLM support
- Add deployment support

---

## Author

Krina Suthar

Computer Science Engineering Student

Aspiring Data Scientist and AI/ML Engineer
