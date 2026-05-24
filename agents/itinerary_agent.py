from utils.openai_client import client


class ItineraryAgent:
    async def run(
        self,
        trip_data,
        budget_result,
        travel_result,
        stay_result,
        weather_result,
        places_result,
        food_result,
        risk_result
    ):
        prompt = f"""
        Create a day-wise travel itinerary.

        Trip Details:
        {trip_data}

        Budget:
        {budget_result}

        Travel:
        {travel_result}

        Stay:
        {stay_result}

        Weather:
        {weather_result}

        Places:
        {places_result}

        Food:
        {food_result}

        Risks:
        {risk_result}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content