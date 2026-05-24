from tavily import TavilyClient
from config import TAVILY_API_KEY


class SearchAPI:
    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    async def search_places(self, destination: str):
        try:
            result = self.client.search(
                query=f"Best tourist places in {destination}",
                max_results=5
            )
            return result

        except Exception as e:
            return {"error": str(e)}