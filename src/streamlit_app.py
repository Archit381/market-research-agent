import streamlit as st
import asyncio
from workflows.research_workflow import ResearchWorkflow
from workflows.generate_usecase_workflow import GenerateUseCaseWorkflow
from utils.settings import project_settings
from llama_index.core.settings import Settings

# Streamlit UI
st.title("Multi Agent-based Market Analysis System")

company_name = st.text_input("Enter Company Name:")
industry_name = st.text_input("Enter Industry Name:")

rwf = ResearchWorkflow(timeout=None, verbose=True)
gen = GenerateUseCaseWorkflow(timeout=None)

async def run_combined_workflows(company_name, industry_name):
    research_result = await rwf.run(
        company_name=company_name,
        industry_name=industry_name,
        query_LLM=project_settings.query_LLM
    )
    
    usecase_response = await gen.run(extracted_data=research_result)
    
    return usecase_response

if st.button("Submit"):
    if company_name and industry_name:
        usecase_response = asyncio.run(run_combined_workflows(company_name, industry_name))
        
        st.subheader("Generated Use Cases")
        st.write(usecase_response)
    else:
        st.warning("Please enter both company name and industry name.")
