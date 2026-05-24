class BudgetAgent:
    async def run(self, trip_data: dict):
        budget = trip_data["budget"]
        days = trip_data["days"]

        return {
            "total_budget": budget,
            "travel_budget": budget * 0.30,
            "stay_budget": budget * 0.35,
            "food_budget": budget * 0.15,
            "activities_budget": budget * 0.15,
            "buffer": budget * 0.05,
            "budget_per_day": budget / days
        }