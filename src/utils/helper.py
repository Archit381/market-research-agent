import requests
from llama_index.core.settings import Settings

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

        parsing_prompt = f'''

        You are an advanced text extraction model. Your task is to extract only the main textual content from the provided scraped webpage data, removing all unrelated elements such as URLs, images, JavaScript, or redundant navigational text. 
        Focus on delivering clear, meaningful content that reflects the primary information and purpose of the webpage. You will also be given a search query which you will use to find the textual data, from the web scraped data, that is relevant to the search query  
        
        Instructions:
        - Don't modify the text extracted from the data into your own words. Just extract the main textual data as it is.
        - Don't say 'Here is the extracted content..' or 'This is a web page...', just remove the unwanted data from the entire input and only output the main textual data as it is.
        - Only find out textual data that is relevant to the search query given to you.
        - Don't give me the HTML code. Just plain simple text 

        Search Query: {searchQuery} (To be used to find relevance)
        Web Scraped Input: (Data to be parsed) 

        {scrapedData}

        Output: 

        '''

        response = Settings._llm.complete(parsing_prompt)

        return response.text

helper = HelperClass()