from utils.openai_client import client


class FoodAgent:
    async def run(self, trip_data: dict):
        destination = trip_data["destination"]
        food = trip_data["food_preference"]

        prompt = f"""
        Suggest best local food options in {destination}
        for {food} travelers.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "food_suggestions": response.choices[0].message.content
        }