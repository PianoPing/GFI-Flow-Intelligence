import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# 檢查檔案是否存在，避免程式崩潰
if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()

    # 顯示你的 HTML 內容
    components.html(html_data, height=1000, scrolling=True)
else:
    st.error("找不到 index.html 檔案，請確認檔案在 GitHub 根目錄。")
