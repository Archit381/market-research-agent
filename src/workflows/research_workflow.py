from llama_index.core.workflow import (
    Event,
    StartEvent,
    StopEvent,
    Workflow,
    Context,
    step
)
from typing import List
from utils.helper import helper
from utils.prompts import INDUSTRY_RESEARCH_PROMPT, COMPETITOR_ANALYSIS_PROMPT, AI_APPLICATIONS_RESEARCH_PROMPT
from workflows.web_search_workflow import WebSearchWorkflow
from models.schema import GeneratedQueriesSchema, GenerateQueriesEvent, ResearchDataSchema
from tqdm import tqdm
from llama_index.core.llms import LLM

class ResearchWorkflow(Workflow):
    '''
    Generates searh queries for multiple research aspects and gathers data from web search
    args: company_name
    args: industry_name
    '''
    @step
    async def _generate_queries(self, ctx: Context, ev: StartEvent)->GenerateQueriesEvent:
        company_name: str = ev.company_name
        industry_name: str = ev.industry_name
        queryLLM: LLM = ev.query_LLM

        prompts = [
            {   
                'title': 'industry_research',
                'prompt': INDUSTRY_RESEARCH_PROMPT
            },
            {
                'title': 'competitor_analysis',
                'prompt': COMPETITOR_ANALYSIS_PROMPT
            },
            {
                'title': 'ai_applications_research',
                'prompt': AI_APPLICATIONS_RESEARCH_PROMPT
            },
        ]

        queries = []

        for item in prompts:

            llm_prompt = item['prompt'].format(
                company_name = company_name,
                industry_name = industry_name
            )

            response = await queryLLM.acomplete(llm_prompt)

            queries.append(GeneratedQueriesSchema(
                query_title = item['title'],
                query_list = response.text.split('\n') 
            ))

        return GenerateQueriesEvent(queries = queries)

    @step
    async def _gatherResearchData(self, ctx: Context, ev: GenerateQueriesEvent)->StopEvent:
        queries = ev.queries

        search_workflow = WebSearchWorkflow(timeout=60, verbose=True)

        data = []

        for item in queries:
            
            search_results = []
            for query in tqdm(item.query_list, desc=f"Scraping data for {item.query_title}"):
                result = await search_workflow.run(search_query = query)
                search_results.append(result)

            data.append(ResearchDataSchema(
                research_domain = item.query_title,
                research_data = search_results
            ))
            
        return StopEvent(result=data)







        



