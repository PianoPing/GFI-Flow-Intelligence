import os
import re
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="GFI Flow Intelligence",
    page_icon="🛡️",
    layout="wide",
)

# -----------------------------
# BRAND INFO
# -----------------------------
BRAND = "GFI Flow Intelligence"
FOUNDER = "Ping Xu"
CITY = "Boston, MA, USA"
EMAIL = "pingshyu0@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ping-shyu/"

# -----------------------------
# MINIMAL CONSULTANT STYLE
# -----------------------------
st.markdown("""
<style>
.block-container {max-width: 980px; padding-top: 2rem;}
.hr {border-top: 1px solid rgba(0,0,0,0.1); margin: 30px 0;}
.footer {color: rgba(0,0,0,0.6); font-size: 12px; margin-top: 40px;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# STRIPE BUTTON
# -----------------------------
STRIPE_BUTTON = """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>
<stripe-buy-button
  buy-button-id="buy_btn_1T1sUvRw9CVw8oC7f8G5G2UR"
  publishable-key="pk_live_51SzplSRw9CVw8oC78qxLy57eZRzWrELB0tBzLJa9FWOkxijGMyDDxrr1si3LdzdOEkoNxY4k5pXwCGAshI5iJ1ul00QnZ6DdJQ">
</stripe-buy-button>
"""

# -----------------------------
# NAVIGATION
# -----------------------------
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Services", "GFI", "Request Assessment", "Engage", "About"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**{FOUNDER}**")
st.sidebar.markdown(CITY)
st.sidebar.markdown(EMAIL)
st.sidebar.markdown(LINKEDIN)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":

    st.markdown(f"### {BRAND}")
    st.markdown("## AI Workflow Impact Assessment")
    st.markdown("### Measuring Operational Stability After AI Integration")

    st.markdown("""
AI increases output.  
But output is not the same as effective throughput.

We assess:

• Where correction load concentrates  
• Where review latency accumulates  
• Where throughput becomes unstable  
• Where operational drag increases  
""")

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.markdown("### Engagement Model")
    st.markdown("""
**14-Day Signal Window**  
**7-Day Executive Delivery**  
**Confidential & Independent**
""")

# -----------------------------
# SERVICES
# -----------------------------
elif page == "Services":

    st.markdown("## AI Workflow Impact Assessment")

    st.markdown("""
AI does not eliminate friction.  
It redistributes it.

We identify:

• Rework Density  
• Correction Latency  
• Human-AI Interface Pressure  
• Throughput Stability Risk
""")

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.markdown("### Deliverables")

    st.markdown("""
✔ Workflow Redistribution Map  
✔ Friction Concentration Analysis  
✔ Executive Brief (5–7 pages)  
✔ Strategic Stability Assessment  
""")

# -----------------------------
# GFI FRAMEWORK
# -----------------------------
elif page == "GFI":

    st.markdown("## Governance Flow Index (GFI)")

    st.markdown("""
An engineering framework for diagnosing operational flow in implemented systems.

GFI measures:

• Latency load  
• Friction density  
• Throughput stability  
• Workflow conversion integrity  

This is a diagnostic tool — not a prediction product.
""")

# -----------------------------
# REQUEST ASSESSMENT
# -----------------------------
elif page == "Request Assessment":

    st.markdown("## Request Assessment")

    with st.form("assessment_form"):
        org = st.text_input("Organization")
        name = st.text_input("Contact Name")
        role = st.text_input("Role")
        email = st.text_input("Email")
        notes = st.text_area("Primary Concern")

        submit = st.form_submit_button("Submit Request")

        if submit:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Invalid email.")
            else:
                st.success("Request submitted.")

# -----------------------------
# ENGAGE (STRIPE)
# -----------------------------
elif page == "Engage":

    st.markdown("## Initiate Engagement")

    st.markdown("""
Confidential engagement.  
Independent advisory.
""")

    components.html(STRIPE_BUTTON, height=220)

    st.caption("After payment, you will be redirected to intake form.")

# -----------------------------
# ABOUT
# -----------------------------
elif page == "About":

    st.markdown(f"## {FOUNDER}")
    st.markdown(f"Founder, {BRAND}")
    st.markdown(CITY)

    st.markdown("""
Architect of the Governance Flow Index (GFI).

Specializing in workflow diagnostics for AI-integrated systems.
""")

    st.markdown(f"Email: {EMAIL}")
    st.markdown(f"LinkedIn: {LINKEDIN}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
{BRAND}  
{FOUNDER} · {CITY}  
{EMAIL}  
linkedin.com/in/ping-shyu  

Independent advisory. Confidential engagements only.  
© 2026 {BRAND}. All rights reserved.
</div>
""", unsafe_allow_html=True)
