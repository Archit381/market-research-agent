# Market Research Agent

This repository contains all the code to run the conduct market analysis and use case generation pipeline.

## Project Structure

```plaintext
MARKET-RESEARCH-AGENT/
├── src/
│   ├── models/
│   │    ├── schema.py
│   ├── utils/
│   │    ├── helper.py
│   │    ├── prompts.py
│   │    ├── settings.py
│   ├── workflows/
│   │    ├── generate_usecase_workflow.py
│   │    ├── research_workflow.py
│   │    ├── web_search_workflow.py
│   ├── main.ipynb
│   ├── proxies.txt
│   ├── streamlit_app.py
├── .env.template
├── README.md
└──pyproject.toml
```

## Getting Started

Follow these steps to get the application up and running:

### 1. Clone the Repository

### 2. Creating a virtual environment for the repo

Make sure you have Python & Poetry installed. Create and activate the virtual enviroment:

```bash
poetry init
poetry shell
```

### 3. Installing Dependencies

Install the project dependencies using:

```bash
poetry install
```

### 4. Setting up Enviroment File

Use the .env.template to create a .env file with the required API_KEYS

### 5. Generate the Workflow

With all configs done, you can run the streamlit demo by using following cmd:

```bash
streamlit run src/streamlit_app.py
```


