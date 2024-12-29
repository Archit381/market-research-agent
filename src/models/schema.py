from pydantic import BaseModel, Field
from llama_index.core.workflow import Event
from typing import List, Dict

class ResearchSchema(BaseModel):
    title: str = Field(description="This is the headline or topic of the query")
    main: str = Field(description="This contains the complete report")

class WebSearchEvent(Event):
    url_list: List[Dict] = Field(description="This contains the list of all search results with their urls")

class ScrapeResultsSchema(BaseModel):
    urls: List[str] = Field(description="This contains the urls of the fetched data from the web search using query")
    query: str = Field(description="This contains the query for the search")
    main: str = Field(description="This contains the main textual data scraped from the url of the webpage")

class ScrapeURLEvent(Event):
    scraped_data: List[ScrapeResultsSchema]
