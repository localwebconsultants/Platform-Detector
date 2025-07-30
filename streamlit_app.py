
import streamlit as st
import pandas as pd
from app.detector import detect_platform

st.set_page_config(layout="wide")
st.title("🌐 Website Platform Detector")

st.markdown("Enter a niche and location to simulate detection of websites built on Wix, GoDaddy, etc.")

niche = st.text_input("Niche (e.g., plumber, dentist):")
location = st.text_input("Location (e.g., London, Miami):")

if st.button("Search and Detect"):
    if not niche or not location:
        st.warning("Please enter both a niche and location.")
    else:
        st.info("Simulating website detection...")
        # Simulated websites (real project would use Google/Bing scraping or API)
        sample_websites = [
            {"business": "Alpha Plumbing", "url": "https://alphaplumbing.wixsite.com"},
            {"business": "Speedy Heating", "url": "https://speedyheating.com"},
            {"business": "Fix-It Fast", "url": "https://fixitfast.godaddysites.com"},
            {"business": "Bright Smiles", "url": "https://brightsmilesdental.com"}
        ]

        results = []
        for entry in sample_websites:
            platform, confidence = detect_platform(entry["url"])
            results.append({
                "Business Name": entry["business"],
                "Website": entry["url"],
                "Platform": platform,
                "Confidence": confidence
            })

        df = pd.DataFrame(results)
        st.dataframe(df)
        st.download_button("📥 Download CSV", df.to_csv(index=False), "detected_websites.csv", "text/csv")
