from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from mcp_server import MCPServer

app = FastAPI(
    title="AI Travel Planner",
    version="1.0.0"
)

mcp = MCPServer()


class TripRequest(BaseModel):
    source: str
    destination: str
    budget: float = Field(gt=0)
    days: int = Field(gt=0)
    travelers: int = Field(gt=0)
    travel_mode: Optional[str] = "any"   # train/flight/bus/any
    stay_type: Optional[str] = "hotel"   # hotel/hostel/resort
    food_preference: Optional[str] = "veg"
    interests: Optional[List[str]] = []


@app.get("/")
async def home():
    return {"message": "AI Travel Planner Running 🚀"}


@app.post("/plan-trip")
async def plan_trip(request: TripRequest):
    try:
        result = await mcp.generate_plan(request.dict())
        return {
            "success": True,
            "trip_plan": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))