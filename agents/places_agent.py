from api.search import SearchAPI
from utils.llm_client import client


class PlacesAgent:
    def __init__(self):
        self.search_api = SearchAPI()

    async def run(self, trip_data: dict):
        destination = trip_data["destination"]

        try:
            result = await self.search_api.search_places(destination)

            raw_places = []
            if "results" in result:
                for item in result["results"]:
                    raw_places.append(item.get("title", ""))

            prompt = f"""
            Extract only tourist place names.

            Rules:
            - Return only names
            - No intro sentence
            - No explanation
            - No numbering
            - No bullets
            - One place per line

            Destination: {destination}
            Data: {raw_places}
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            text = response.choices[0].message.content

            # cleanup
            places = []
            for line in text.split("\n"):
                line = line.strip()
                if not line:
                    continue
                if "based on" in line.lower():
                    continue
                if "here are" in line.lower():
                    continue

                line = (
                    line.replace("-", "")
                    .replace("•", "")
                    .replace("1.", "")
                    .replace("2.", "")
                    .replace("3.", "")
                    .replace("4.", "")
                    .replace("5.", "")
                    .strip()
                )

                if line:
                    places.append(line)

            return {"places": places}

        except Exception as e:
            return {"places": [], "error": str(e)}