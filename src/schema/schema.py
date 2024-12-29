from pydantic import BaseModel, Field

class ResearchSchema(BaseModel):
    title: str = Field(description="This is the headline or topic of the query")
    main: str = Field(description="This contains the complete report")

class ScrapeDataSchema(BaseModel):
    url: str = Field(description="This contains the url of the fetched data from the web search using query")
    main: str = Field(description="This contains the data scraped from the url of the webpage")