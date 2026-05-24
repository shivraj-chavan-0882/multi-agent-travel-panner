from api.weather import WeatherAPI


class WeatherAgent:
    def __init__(self):
        self.weather_api = WeatherAPI()

    async def run(self, trip_data: dict):
        destination = trip_data["destination"]
        return await self.weather_api.get_weather(destination)