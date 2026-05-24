from api.flights import FlightAPI


class TravelAgent:
    def __init__(self):
        self.flight_api = FlightAPI()

    async def run(self, trip_data: dict):
        source = trip_data["source"]
        destination = trip_data["destination"]

        flights = await self.flight_api.get_flights()

        return {
            "source": source,
            "destination": destination,
            "flight_data": flights
        }