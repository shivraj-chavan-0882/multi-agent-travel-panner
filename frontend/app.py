import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("✈️ Multi-Agent AI Travel Planner")
st.caption("Plan smart trips using AI + MCP Server")

# ---------------- FORM ----------------
with st.form("trip_form"):
    st.subheader("Trip Details")

    col1, col2 = st.columns(2)

    with col1:
        source = st.text_input("Source City")
        destination = st.text_input("Destination City")
        budget = st.number_input("Budget (₹)", min_value=1000, step=500)
        days = st.number_input("Days", min_value=1, step=1)

    with col2:
        travelers = st.number_input("Travelers", min_value=1, step=1)

        travel_mode = st.selectbox(
            "Travel Mode",
            ["any", "flight", "train", "bus"]
        )

        stay_type = st.selectbox(
            "Stay Type",
            ["hotel", "hostel", "resort"]
        )

        food_preference = st.selectbox(
            "Food Preference",
            ["veg", "non-veg", "any"]
        )

    interests = st.multiselect(
        "Interests",
        [
            "beaches",
            "nightlife",
            "adventure",
            "shopping",
            "nature",
            "historical places"
        ]
    )

    submit = st.form_submit_button("Generate Travel Plan 🚀")

# ---------------- API CALL ----------------
if submit:
    payload = {
        "source": source,
        "destination": destination,
        "budget": budget,
        "days": days,
        "travelers": travelers,
        "travel_mode": travel_mode,
        "stay_type": stay_type,
        "food_preference": food_preference,
        "interests": interests
    }

    try:
        with st.spinner("Creating your AI travel plan..."):
            response = requests.post(
                "http://127.0.0.1:8000/plan-trip",
                json=payload,
                timeout=120
            )

        if response.status_code == 200:
            result = response.json()
            trip = result["trip_plan"]

            st.success("Travel Plan Generated Successfully ✨")

            # ---------------- TRIP SUMMARY ----------------
            st.subheader("📍 Trip Summary")
            c1, c2, c3, c4 = st.columns(4)

            c1.metric("From", trip["trip_details"]["source"])
            c2.metric("To", trip["trip_details"]["destination"])
            c3.metric("Budget", f"₹{trip['trip_details']['budget']}")
            c4.metric("Days", trip["trip_details"]["days"])

            # ---------------- BUDGET ----------------
            st.subheader("💰 Budget Breakdown")
            b1, b2, b3, b4, b5 = st.columns(5)

            budget_data = trip["budget"]

            b1.metric("Travel", f"₹{int(budget_data['travel_budget'])}")
            b2.metric("Stay", f"₹{int(budget_data['stay_budget'])}")
            b3.metric("Food", f"₹{int(budget_data['food_budget'])}")
            b4.metric("Activities", f"₹{int(budget_data['activities_budget'])}")
            b5.metric("Buffer", f"₹{int(budget_data['buffer'])}")

            # ---------------- WEATHER ----------------
            st.subheader("🌦 Weather")
            weather = trip["weather"]

            wc1, wc2 = st.columns(2)
            wc1.info(f"Temperature: {weather.get('temperature', 'N/A')}°C")
            wc2.info(f"Condition: {weather.get('weather', 'N/A')}")

            # ---------------- STAY ----------------
            st.subheader("🏨 Stay Suggestions")
            st.success(trip["stay"].get("recommended_stay", "No stay suggestion available"))

            # ---------------- PLACES ----------------
            st.subheader("📌 Best Places to Visit")

            places = trip["places"].get("places", [])

            if places:
                cols = st.columns(2)

                for i, place in enumerate(places):
                    cols[i % 2].success(f"📍 {place}")
            else:
                st.warning("No places found")
            

            # ---------------- FOOD ----------------
            st.subheader("🍛 Food Suggestions")
            st.info(
                trip["food"].get(
                    "food_suggestions",
                    "No food suggestions available"
                )
            )

            # ---------------- RISKS ----------------
            st.subheader("⚠️ Risks / Alerts")
            risks = trip["risk"].get("risks", [])

            if risks:
                for risk in risks:
                    st.warning(risk)
            else:
                st.success("No major travel risks found")

            # ---------------- ITINERARY ----------------
            st.subheader("🗓 Final AI Itinerary")
            st.markdown(trip["itinerary"])

        else:
            st.error(f"Backend Error: {response.text}")

    except Exception as e:
        st.error(f"Request Failed: {str(e)}")