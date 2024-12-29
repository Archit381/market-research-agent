from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field
from llama_index.core.settings import Settings
from llama_index.llms.groq import Groq

class ProjectSettings(BaseSettings):
    GROQ_API_KEY: Optional[str] = Field(None, env="GROQ_API_KEY")
    JINA_API_KEY: Optional[str] = Field(None, env="JINA_API_KEY")

    class Config:
        env_file = '.env'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Settings._llm = Groq(
            model = "llama-3.3-70b-versatile",
            api_key = self.GROQ_API_KEY 
        )

project_settings = ProjectSettings()

# print(project_settings.JINA_API_KEY)