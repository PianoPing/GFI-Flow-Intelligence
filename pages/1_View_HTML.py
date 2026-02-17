import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

st.title("GFI / OFI Method Definition")

# 確保 index.html 存在
html_path = os.path.join(os.getcwd(), "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_data = f.read()

    components.html(
        html_data,
        height=1200,
        scrolling=True
    )
else:
    st.error("❌ index.html not found. Please confirm the file exists in the root directory.")
