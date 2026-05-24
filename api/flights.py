import httpx
from config import AVIATIONSTACK_API_KEY


class FlightAPI:
    BASE_URL = "http://api.aviationstack.com/v1/flights"

    async def get_flights(self):
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                response = await client.get(
                    self.BASE_URL,
                    params={"access_key": AVIATIONSTACK_API_KEY}
                )

                response.raise_for_status()
                data = response.json()

                return data.get("data", [])

        except Exception as e:
            return {"error": str(e)}