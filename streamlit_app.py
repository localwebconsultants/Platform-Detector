import streamlit as st
import pandas as pd
import requests
import os
from app.detector import detect_platform

st.set_page_config(layout="wide")
st.title("🌐 Website Platform Detector")
st.markdown("Enter a niche and location to find websites and detect if they're built on Wix, GoDaddy, etc.")

niche = st.text_input("Niche (e.g., plumber, dentist):")
location = st.text_input("Location (e.g., London, Miami):")

if st.button("Search and Detect"):
    if not niche or not location:
        st.warning("Please enter both a niche and location.")
    else:
        st.info("Searching Yelp for businesses...")

        headers = {
            "Authorization": f"Bearer {os.getenv('YELP_API_KEY')}"
        }

        params = {
            "term": niche,
            "location": location,
            "limit": 10
        }

        response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
        data = response.json()

        if "businesses" not in data:
            st.error("No businesses found or invalid API key.")
        else:
            results = []
            for biz in data["businesses"]:
                name = biz["name"]
                url = biz.get("url", "")
                website = biz.get("url", "")  # Yelp doesn't always return actual business websites

                platform, confidence = detect_platform(website)
                results.append({
                    "Business Name": name,
                    "Website": website,
                    "Platform": platform,
                    "Confidence": confidence
                })

            df = pd.DataFrame(results)
            st.dataframe(df)

            st.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="platform_results.csv", mime="text/csv")
