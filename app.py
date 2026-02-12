import math
import streamlit as st

# 1. 頁面權威設定
st.set_page_config(page_title="GFT Flow Intelligence", layout="wide")
st.title("🛡️ GFT Flow Intelligence")
st.caption("Founder: Ping | Strategic Risk Auditor | Boston, MA")

# 2. 建立標籤分頁 (讓一頁看起來像多頁網站)
tab1, tab2, tab3 = st.tabs(["🔍 Risk Diagnostic", "📖 Methodology", "🏢 Corporate Identity"])

with tab1:
    st.header("Real-time Asset Evaporation Diagnostic")
    st.write("Enter your organizational variables to quantify institutional friction.")
    
    # 這裡放妳原本的計算邏輯 (Pd, Cf 等)
    c1, c2 = st.columns(2)
    with c1:
        pd = st.number_input("Latency Hours (Pd)", 0.0, 5000.0, 150.0)
        rate = st.number_input("Avg. Hourly Rate ($)", 20.0, 2000.0, 65.0)
    with c2:
        raw_cf = st.number_input("Complexity Points (Raw)", 0.0, 200.0, 30.0)
        vol = st.number_input("Monthly Volume", 1, 1000000, 2000)

    # 核心計算
    waste = (pd * rate * vol * 12) + (raw_cf * 200 * vol * 12) 
    st.metric("Estimated Annual Asset Evaporation", f"${waste:,.0f}")
    
    st.divider()
    st.link_button("💳 Order Full Strategic Roadmap ($1,999)", "https://buy.stripe.com/your_link_here")

with tab2:
    st.header("The GFI/OFI Frameworks")
    st.write("Our proprietary models treat administrative friction as a physics problem.")
    st.markdown("### **GFI (Governance Flow Index)**")
    st.write("Quantifying friction in public policy delivery to restore government legitimacy.")
    st.markdown("### **OFI (Operational Flow Index)**")
    st.write("Identifying the 'friction tax' in private operations to recover lost margins.")

with tab3:
    st.header("About GFT Flow Intelligence")
    st.write("Based in Boston, MA, we provide strategic interventions for high-scale institutional risk.")
    st.write("For inquiries regarding UN P5-level economic affairs or state-level policy reform:")
    st.link_button("✉️ Contact Principal Auditor", "mailto:YOUR_EMAIL_HERE")