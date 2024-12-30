from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field
from llama_index.core.settings import Settings
from llama_index.llms.groq import Groq
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import LLM

class ProjectSettings(BaseSettings):
    GROQ_API_KEY: Optional[str] = Field(None, env="GROQ_API_KEY")
    query_LLM: Optional[LLM] = None

    class Config:
        env_file = '.env'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Settings._llm = Groq(
        #     model = "llama-3.3-70b-versatile",
        #     api_key = self.GROQ_API_KEY 
        # )
        self.query_LLM = Groq(
            model = "llama-3.3-70b-versatile",
            api_key = self.GROQ_API_KEY 
        )
        Settings._llm = Ollama(
            model = "llama3.2:3b"
        )

project_settings = ProjectSettings()
