
import streamlit as st

# =========================
# STRIPE LINKS
# =========================
QUICK_PAY_URL = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
DEEP_PAY_URL  = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="GFI Flow Intelligence — AI Impact Audit",
    page_icon="⚖️",
    layout="wide"
)

# =========================
# CLEAN PROFESSIONAL CSS
# =========================
st.markdown("""
<style>
.block-container {padding-top: 3rem; padding-bottom: 3rem; max-width: 1150px;}
h1 {font-size: 2.8rem !important; font-weight: 800;}
h2 {font-size: 1.6rem !important;}
.card {
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 14px;
    padding: 1.5rem;
    background: #ffffff;
}
hr {margin: 2rem 0;}
.small {font-size: 0.9rem; opacity: 0.7;}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (NO HEAVY BANNER)
# =========================
col1, col2 = st.columns([1, 4])

with col1:
    st.image("GFILOGO.png", width=120)

with col2:
    st.markdown("# We Audit Your AI Investment")
    st.markdown("### Measure. Validate. De-Risk.")
    st.markdown("""
AI deployment is easy.  
Measuring whether it improved performance is not.

We quantify operational impact using structured friction analysis.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# CORE VALUE
# =========================
st.markdown("## What We Measure")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**Hidden Friction Load**")
    st.write("Detect manual rework, escalation spikes, and workflow duplication.")

with c2:
    st.markdown("**AI Value Deviation**")
    st.write("Compare baseline vs post-implementation performance.")

with c3:
    st.markdown("**Decision Path Optimization**")
    st.write("Identify latency layers and structural inefficiencies.")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ENGAGEMENT OPTIONS
# =========================
st.markdown("## Engagement Options")

colA, colB = st.columns(2)

with colA:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### AI Impact Quick Diagnostic — $999")
    st.write("""
48-hour structured review using submitted metrics.

Deliverables:
- Net Impact Index (ANI)
- Risk classification
- Executive summary PDF
""")
    st.link_button("Start Diagnostic", QUICK_PAY_URL)
    st.markdown('</div>', unsafe_allow_html=True)

with colB:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### AI Friction Deep Audit — $4,999")
    st.write("""
Full workflow friction mapping.

Deliverables:
- Process map
- Bottleneck & latency breakdown
- Governance Impact Report
""")
    st.link_button("Request Deep Audit", DEEP_PAY_URL)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# METHOD
# =========================
st.markdown("## Methodology")

st.write("""
**ANI = ΔFlow − ΔFriction**

Where:
- ΔFlow = speed & throughput improvement
- ΔFriction = rework, manual correction, added review layers
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# FINAL CTA
# =========================
st.markdown("## Measure Real AI ROI")

st.write("""
Stop guessing.  
Get measurable performance validation within 48 hours.
""")
