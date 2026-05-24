import httpx
from config import WEATHER_API_KEY


class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    async def get_weather(self, city: str):
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.get(
                    self.BASE_URL,
                    params={
                        "q": city,
                        "appid": WEATHER_API_KEY,
                        "units": "metric"
                    }
                )

                response.raise_for_status()
                data = response.json()

                return {
                    "temperature": data["main"]["temp"],
                    "weather": data["weather"][0]["description"]
                }

        except Exception as e:
            return {"error": str(e)}