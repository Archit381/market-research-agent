import streamlit as st
import asyncio
from workflows.research_workflow import ResearchWorkflow
from utils.settings import project_settings
from llama_index.core.settings import Settings

st.title("Multi Agent-based Market Analysis System")

company_name = st.text_input("Enter Company Name:")
industry_name = st.text_input("Enter Industry Name:")

async def run_analysis(company_name, industry_name):
    rwf = ResearchWorkflow(timeout=None, verbose=True)
    result = await rwf.run(company_name=company_name, industry_name=industry_name, query_LLM=project_settings.query_LLM)
    return result

if st.button("Submit"):
    if company_name and industry_name:
        result = asyncio.run(run_analysis(company_name, industry_name))
        st.subheader(f"Analysis Result for {company_name} in {industry_name}")
        st.write(result)
    else:
        st.warning("Please enter both company name and industry name.")
