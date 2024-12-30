from llama_index.core.workflow import (
    Event,
    StartEvent,
    StopEvent,
    Workflow,
    Context,
    step
)
from models.schema import WebSearchEvent, ScrapeURLEvent, ScrapeResultsSchema
from duckduckgo_search import DDGS
from utils.helper import helper
from tqdm import tqdm

class WebSearchWorkflow(Workflow):
    '''
    Searches using user-query for top results across the web and scrapes webpages for relevant data
    args: search_query   
    '''
    @step
    async def _webSearch(self, ctx: Context, ev: StartEvent)->WebSearchEvent:
        search_query = ev.search_query
        # jina_api_key = ev.jina_api_key
        await ctx.set("search_query", search_query)
        # await ctx.set("JINA_API_KEY", jina_api_key)

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
        # jina_api_key:str = await ctx.get("JINA_API_KEY")
        
        data = ""
        source_urls = []
        for search_result in tqdm(url_list, desc="Scraping search results"):
            # fetched_raw_data = helper._apiRequest(url = search_result['href'], jina_api_key=jina_api_key)
            fetched_raw_data = helper._apiRequest(url = search_result['href'])
            data+=fetched_raw_data+"\n"
            source_urls.append(search_result['href'])
        

        parsed_data = await helper._parseScrapedData(
                scrapedData = data,
                searchQuery = search_query
        )
            
        data = ScrapeResultsSchema(urls = source_urls, query = search_query, main = parsed_data)
        return StopEvent(result=data)
