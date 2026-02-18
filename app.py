
import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="GFI Flow Intelligence — AI Impact Audit",
    page_icon="🧪",
    layout="wide"
)

# =========================
# SIMPLE CSS (clean + consulting-grade)
# =========================
st.markdown("""
<style>
/* global spacing */
.block-container {padding-top: 2.2rem; padding-bottom: 2.2rem; max-width: 1200px;}
/* buttons */
.stButton>button {
    width: 100%;
    padding: 0.9rem 1.0rem;
    border-radius: 14px;
    font-weight: 700;
}
.small-note {opacity: 0.75; font-size: 0.92rem;}
.kicker {letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.85rem; opacity: 0.75;}
.hero {font-size: 2.6rem; font-weight: 800; line-height: 1.05; margin: 0.3rem 0 0.6rem 0;}
.subhero {font-size: 1.2rem; opacity: 0.85; max-width: 60ch;}
.card {
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 1.1rem 1.2rem;
    background: rgba(255,255,255,0.03);
}
.hr {height: 1px; background: rgba(255,255,255,0.15); margin: 1.2rem 0;}
.badge {
    display: inline-block;
    padding: 0.25rem 0.55rem;
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 999px;
    font-size: 0.85rem;
    opacity: 0.85;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER / HERO
# =========================
left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown('<div class="kicker">AI Implementation Impact Audit</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero">We Audit Your AI Investment.</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="subhero">
<b>Not by hype.</b><br/>
<b>By measurable performance shift.</b>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    st.markdown("""
Most organizations deploy AI.  
Very few measure whether it actually **reduced friction**.

We quantify the difference between:

- **Speed gained**
- **Friction created**
- **Net operational impact**
""")

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    st.markdown("### After AI implementation, can you answer this?")
    st.markdown("""
- Did processing time actually decrease?
- Did manual review quietly increase?
- Did error correction workload rise?
- Did hidden workflow steps multiply?
- Do you have baseline comparison data?

If you cannot answer these clearly — you don’t know your AI ROI.
""")

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### What you get")
    st.markdown("""
- Baseline vs Post-Implementation comparison  
- **Net Impact Index (ANI)** = ΔFlow − ΔFriction  
- Risk classification: **Green / Yellow / Red**  
- Executive-ready PDF report  
""")
    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.markdown("#### Typical outcomes")
    st.markdown("""
- AI improved throughput, **but** increased hidden rework  
- AI reduced cycle time, **but** added approval layers  
- AI lowered cost, **but** raised compliance risk exposure  
""")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# OFFERING / PRICING
# =========================
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("## Engagement Options")

c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔎 AI Impact Quick Diagnostic — **$999**")
    st.markdown("""
**48-hour performance review** using self-reported operational metrics.

**Deliverables**
- ANI score (ΔFlow − ΔFriction)
- Risk classification (Green / Yellow / Red)
- 6–8 page PDF report
""")
    st.markdown('<div class="small-note">Best for: teams that need an immediate answer for leadership.</div>', unsafe_allow_html=True)
    st.write("")
    if st.button("Start Diagnostic"):
        st.session_state["nav_target"] = "contact"
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔬 AI Friction Deep Audit — **$4,999**")
    st.markdown("""
**Full workflow mapping** to identify where AI created or shifted friction.

**Deliverables**
- Process map + bottleneck analysis
- Latency breakdown & shadow labor detection
- 15–25 page Governance Impact Report
""")
    st.markdown('<div class="small-note">Best for: organizations seeing mixed results after AI deployment.</div>', unsafe_allow_html=True)
    st.write("")
    if st.button("Request Deep Audit"):
        st.session_state["nav_target"] = "contact"
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# TRUST / METHOD
# =========================
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns([1.2, 1.2, 1.6], gap="large")

with t1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Method (simple)")
    st.markdown("""
**ANI = ΔFlow − ΔFriction**

- ΔFlow: time-to-complete, throughput, completion rate  
- ΔFriction: rework, manual review, added steps, error correction  
""")
    st.markdown('</div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### What we don’t do")
    st.markdown("""
- No hype decks  
- No vague “AI transformation” claims  
- No vendor marketing language  
""")
    st.markdown('</div>', unsafe_allow_html=True)

with t3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Who this is for")
    st.markdown("""
- Public agencies modernizing services  
- Healthcare / education operations teams  
- Compliance-heavy organizations  
- Any team under pressure to justify AI spend  
""")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER CTA
# =========================
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
f1, f2 = st.columns([2, 1], gap="large")

with f1:
    st.markdown("### Ready to measure real AI ROI?")
    st.markdown("""
Stop guessing.  
Get a measurable performance shift summary — fast.
""")

with f2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Contact / Intake")
    st.markdown("""
Use the **Contact** page to submit your baseline + post-AI metrics.  
We’ll confirm scope and delivery timeline.
""")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# OPTIONAL: SIMPLE NAV HANDOFF
# If you have a pages/Contact.py, this will hint where to go next.
# =========================
if st.session_state.get("nav_target") == "contact":
    st.info("Next step: open the **Contact** page in the sidebar to submit your intake metrics.")
    st.session_state["nav_target"] = None
