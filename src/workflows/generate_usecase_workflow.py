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
from llama_index.core.llms import LLM
from utils.prompts import EXTRACT_COMPETITORS_AI_USE_PROMPT, GENERATE_USE_CASE_PROMPT

class GenerateUseCaseWorkflow(Workflow):
    '''
    Uses the data gathered to design AI/ML/GenAI use cases
    args: extracted_data
    '''
    @step
    async def _generate_usecases(self, ctx: Context, ev: StartEvent)->StopEvent:
        extracted_data: List = ev.extracted_data
        
        company_data = ""
        for item in extracted_data[0].research_data:
            company_data+=item.main

        competitor_analysis_data = ""
        for item in extracted_data[1].research_data:
            competitor_analysis_data+=item.main

        ai_applications_data = ""
        for item in extracted_data[2].research_data:
            ai_applications_data+=item.main
        
        prompt = EXTRACT_COMPETITORS_AI_USE_PROMPT.format(
            competitor_analysis_data = competitor_analysis_data,
        )

        output = await helper._getLLMOutput(prompt)

        prompt_2 = GENERATE_USE_CASE_PROMPT.format(
            ai_competitor_analysis = output,
            ai_research = ai_applications_data
        )

        final_result = await helper._getLLMOutput(prompt_2)

        return StopEvent(result=final_result)









        



