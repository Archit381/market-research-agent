from pydantic import BaseModel, Field
from llama_index.core.workflow import Event
from typing import List, Dict

class ResearchSchema(BaseModel):
    title: str = Field(description="This is the headline or topic of the query")
    main: str = Field(description="This contains the complete report")

class WebSearchEvent(Event):
    url_list: List[Dict] = Field(description="This contains the list of all search results with their urls")

class ScrapedResultsSchema(BaseModel):
    source_urls: List[str] = Field(description="This contains the urls of the fetched data from the web search using query")
    query: str = Field(description="This contains the query for the search")
    main: str = Field(description="This contains the main textual data scraped from the url of the webpage")

class GeneratedQueriesSchema(BaseModel):
    query_title: str = Field(description="Title for query prompts")
    query_list: List[str] = Field(description="Contains list of queries")

class GenerateQueriesEvent(Event):
    queries: List[GeneratedQueriesSchema]

class ResearchDataSchema(BaseModel):
    research_domain: str = Field(description="Name of the domain researched")
    research_data: List[ScrapedResultsSchema] = Field(description="Contains the gathered data from web scraping")

