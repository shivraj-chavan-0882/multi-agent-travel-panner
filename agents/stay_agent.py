from utils.openai_client import client


class StayAgent:
    async def run(self, trip_data: dict):
        try:
            destination = trip_data["destination"]
            budget = trip_data["budget"]

            prompt = f"""
            Suggest best stay areas in {destination}
            under budget {budget}.
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            return {
                "recommended_stay":
                    response.choices[0].message.content
            }

        except Exception as e:
            return {"error": str(e)}