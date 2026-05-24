import asyncio
from agents.budget_agent import BudgetAgent
from agents.travel_agent import TravelAgent
from agents.stay_agent import StayAgent
from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent
from agents.food_agent import FoodAgent
from agents.risk_agent import RiskAgent
from agents.itinerary_agent import ItineraryAgent


class MCPServer:
    def __init__(self):
        self.budget_agent = BudgetAgent()
        self.travel_agent = TravelAgent()
        self.stay_agent = StayAgent()
        self.weather_agent = WeatherAgent()
        self.places_agent = PlacesAgent()
        self.food_agent = FoodAgent()
        self.risk_agent = RiskAgent()
        self.itinerary_agent = ItineraryAgent()

    async def generate_plan(self, trip_data: dict):
        (
            budget_result,
            travel_result,
            stay_result,
            weather_result,
            places_result,
            food_result,
            risk_result
        ) = await asyncio.gather(
            self.budget_agent.run(trip_data),
            self.travel_agent.run(trip_data),
            self.stay_agent.run(trip_data),
            self.weather_agent.run(trip_data),
            self.places_agent.run(trip_data),
            self.food_agent.run(trip_data),
            self.risk_agent.run(trip_data),
        )

        itinerary = await self.itinerary_agent.run(
            trip_data,
            budget_result,
            travel_result,
            stay_result,
            weather_result,
            places_result,
            food_result,
            risk_result
        )

        final_response = {
            "trip_details": trip_data,
            "budget": budget_result,
            "travel": travel_result,
            "stay": stay_result,
            "weather": weather_result,
            "places": places_result,
            "food": food_result,
            "risk": risk_result,
            "itinerary": itinerary
        }

        return final_response