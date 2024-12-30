import requests
from llama_index.core.settings import Settings
from utils.prompts import PARSING_PROMPT_TEMPLATE


class HelperClass:
    
    @staticmethod
    def _apiRequest(url: str)->str:
        '''
        Proxy Rotation
        '''
        
        with open('proxies.txt', 'r', encoding='utf-8') as file:
            proxies = file.read().split('\n')

        for proxy in proxies:
            try:
                api_url = f"https://r.jina.ai/{url}"
                response = requests.get(api_url, proxies={"http":proxy, "https": proxy})

                if response.status_code==200:
                    return response.text

            except Exception as e:
                raise RuntimeError(f"Api Request failed with error: {e}")

    async def _getLLMOutput(self, prompt: str)->str:
        token_count = len(prompt.split(" "))
        print(f"Token count: {token_count}")
        try:
            response = await Settings._llm.acomplete(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Failed to Get LLM Ouput with error: {e}")

helper = HelperClass()