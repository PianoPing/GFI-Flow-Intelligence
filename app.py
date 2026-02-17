import streamlit as st

APP_TITLE = "GFI Flow Intelligence"
TAGLINE = "Independent Diagnostic Reports · Confidential · Non-Political"

st.set_page_config(page_title=APP_TITLE, page_icon="🛡️", layout="wide")

# ---------- Global CSS ----------
st.markdown("""
<style>
.block-container { max-width: 1200px; padding-top: 2.0rem; padding-bottom: 3rem; }
h1 { letter-spacing: -0.02em; }
h2, h3 { letter-spacing: -0.01em; }
.gfi-hero {
  padding: 18px 18px;
  border: 1px solid rgba(49,51,63,0.16);
  border-radius: 18px;
  background: linear-gradient(180deg, rgba(49,51,63,0.04), rgba(49,51,63,0.01));
  margin-bottom: 18px;
}
.gfi-title { font-size: 44px; font-weight: 800; margin: 0; }
.gfi-tag
