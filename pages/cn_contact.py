import streamlit as st

st.title("聯絡")
st.subheader("申請 $999 自助式流程診斷")

st.divider()

FORM_URL = "https://forms.gle/96rG6e4PTAJgDkcJ9"

st.markdown("## 申請表單")
st.markdown(FORM_URL)

st.info("交付時間：員工問卷完成後 **48 小時內** 出報告。")
