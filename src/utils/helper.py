import requests
from llama_index.core.settings import Settings
from prompts import PARSING_PROMPT_TEMPLATE

class HelperClass:
    
    @staticmethod
    def _apiRequest(url: str)->str:

        # headers = {
        #     "Authorization": f"Bearer {jina_api_key}"
        # }
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

    @staticmethod
    async def _parseScrapedData(scrapedData: str, searchQuery: str)->str:

        parsing_prompt = PARSING_PROMPT_TEMPLATE.format(searchQuery=searchQuery, scraped=scrapedData)

        response = Settings._llm.complete(parsing_prompt)

        return response.text

helper = HelperClass()