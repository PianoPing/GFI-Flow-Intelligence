# app.py  (EN main page)
import streamlit as st

st.set_page_config(
    page_title="GFI Flow Intelligence",
    layout="wide",
)

st.title("Governance Flow Index (GFI)")
st.subheader("Stop Structural Friction. Restore Institutional Flow.")
st.caption("Independent diagnostic reports for public-sector & large institutions.")

st.divider()

st.markdown("## $999 Self-Service Friction Scan")
st.markdown("""
This is a **fully self-service** diagnostic.

Your team completes the structured questionnaire.  
Within **48 hours**, you receive a friction analysis report.

**No meetings. No consulting calls. No customization.**
""")

st.markdown("### What you receive")
st.markdown("""
- Friction concentration map  
- Delay accumulation indicators  
- Structural overload signals  
- Risk exposure estimate  
""")

st.info("This is a **signal report** — not a full institutional audit.")

st.divider()

st.markdown("## Upgrade Path")
st.markdown("""
If deeper modeling is required:

A **$4,999 deposit** is required to initiate a full structural audit engagement.
""")
st.warning("No unpaid strategy sessions. Serious engagement only.")
