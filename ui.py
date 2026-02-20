import streamlit as st
from tracker import load_items

st.title("🧥 Fashion Ownership Tracker")

items = load_items()

if not items:
    st.write("Wardrobe is empty.")
else:
    for item in items:
        st.markdown("---")
        st.subheader(item["name"])
        st.write(item)