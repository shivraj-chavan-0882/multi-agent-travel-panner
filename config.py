import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")