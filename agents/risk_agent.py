class RiskAgent:
    async def run(self, trip_data: dict):
        budget = trip_data["budget"]
        days = trip_data["days"]

        risks = []

        if budget < 5000:
            risks.append("Budget may be too low")

        if days <= 1:
            risks.append("Trip duration may be too short")

        return {
            "risks": risks
        }