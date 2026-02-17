import streamlit as st

st.title("案例（摩擦模式）")
st.subheader("自助式掃描會抓到哪些典型堵塞")

st.divider()

st.markdown("## 常見模式")
st.markdown("""
- **審批瓶頸：**單一關卡堆積等待  
- **重工迴圈：**規則不清導致反覆修正  
- **交接斷裂：**跨部門資訊重置、重新來過  
- **延遲漂移：**小延遲累積成制度性失速  
""")

st.markdown("## 訊號報告會標示")
st.markdown("""
- 摩擦在哪裡集中  
- 延遲在哪裡堆積  
- 哪裡開始形成結構性過載  
""")
