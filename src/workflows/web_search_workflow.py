from llama_index.core.workflow import (
    Event,
    StartEvent,
    StopEvent,
    Workflow,
    Context,
    step
)
from llama_index.core.settings import Settings
from llama_index.llms.ollama import Ollama
from models.schema import ResearchSchema, WebSearchEvent, ScrapeURLEvent, ScrapeResultsSchema
import requests
from duckduckgo_search import DDGS


class WebSearchWorkflow(Workflow):
    '''
    Searches using user-query for top results across the web and scrapes webpages for relevant data
    args: search_query   
    '''
    @step
    async def _webSearch(self, ctx: Context, ev: StartEvent)->WebSearchEvent:
        search_query = ev.search_query
        await ctx.set("search_query", search_query)

        list_ = DDGS().text(  
                keywords = search_query,
                region = 'wt-wt',
                safesearch = 'off',
                timelimit = '7d',
                max_results = 2
            )

        return WebSearchEvent(url_list=list_)

    @step
    async def _scrapeURL(self, ctx: Context, ev: WebSearchEvent)->StopEvent:
        url_list = ev.url_list
        search_query:str = await ctx.get("search_query")
        
        data = ""
        source_urls = []
        for search_result in tqdm(url_list, desc="Scraping search results"):
            fetched_raw_data = _apiRequest(url = search_result['href'])
            data+=fetched_raw_data+"\n"
            source_urls.append(search_result['href'])

        parsed_data = await _parseScrapedData(
                scrapedData = data,
                searchQuery = search_query
        )
            
        data = ScrapeResultsSchema(urls = source_urls, query = search_query, main = parsed_data)
        return StopEvent(result=data)
