# app.py — FINAL deploy-ready (single-file Streamlit)
# GFI Flow Intelligence | Consultant-grade site + Stripe + Intake + Lead capture
# Copy-paste ready.

import os
import re
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="GFI Flow Intelligence",
    page_icon="🛡️",
    layout="wide",
)

# -----------------------------
# Brand constants (EDIT HERE ONLY)
# -----------------------------
BRAND = "GFI Flow Intelligence"
FOUNDER = "Ping Xu"
CITY = "Boston, MA, USA"
CONTACT_EMAIL = "pingshyu0@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/ping-shyu/"

# Stripe Buy Button (optional) — keep as-is or replace with your own.
STRIPE_BUY_BUTTON_HTML = """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>
<stripe-buy-button
  buy-button-id="buy_btn_1T1sUvRw9CVw8oC7f8G5G2UR"
  publishable-key="pk_live_51SzplSRw9CVw8oC78qxLy57eZRzWrELB0tBzLJa9FWOkxijGMyDDxrr1si3LdzdOEkoNxY4k5pXwCGAshI5iJ1ul00QnZ6DdJQ">
</stripe-buy-button>
"""

# Post-payment intake URL (set this in Stripe success redirect too)
INTAKE_URL = "https://yourdomain.com/intake"  # <- replace when ready

# Put your PDF in the same folder as app.py with this name to enable download
EXEC_BRIEF_PATH = "executive_brief.pdf"

# Local lead capture file (Streamlit filesystem)
LEAD_LOG = "leads.csv"

# -----------------------------
# Consultant-grade CSS (minimal, clean)
# -----------------------------
st.markdown(
    """
<style>
:root { --maxw: 1040px; }
.block-container { padding-top: 2.0rem; padding-bottom: 4rem; max-width: var(--maxw); }
h1, h2, h3 { letter-spacing: -0.02em; }
.smallcaps { font-variant: small-caps; letter-spacing: 0.06em; }
.subtle { color: rgba(0,0,0,0.62); }
.hr { border-top: 1px solid rgba(0,0,0,0.10); margin: 24px 0; }
.pill { display: inline-block; padding: 6px 10px; border: 1px solid rgba(0,0,0,0.14); border-radius: 999px; font-size: 12px; color: rgba(0,0,0,0.72); margin-right: 8px; margin-bottom: 8px;}
.card { border: 1px solid rgba(0,0,0,0.10); border-radius: 18px; padding: 18px 18px 14px 18px; background: #fff; }
.kpi { font-size: 34px; font-weight: 700; letter-spacing: -0.03em; }
.kpi_label { color: rgba(0,0,0,0.62); font-size: 13px; margin-top: -6px; }
a { text-decoration: none; }
.footer { margin-top: 26px; color: rgba(0,0,0,0.62); font-size: 12.5px; line-height: 1.55; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers
# -----------------------------
def safe_email(s: str) -> bool:
    s = (s or "").strip()
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", s))

def append_csv(path: str, row: list[str]):
    line = ",".join([f'"{str(x).replace(chr(34), chr(34)*2)}"' for x in row]) + "\n"
    exists = os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if not exists:
            f.write('"timestamp","type","org","name","role","email","scope","concern","notes"\n')
        f.write(line)

def hr():
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

def pills(*items: str):
    html = "".join([f'<span class="pill">{i}</span>' for i in items])
    st.markdown(html, unsafe_allow_html=True)

def contact_block(compact: bool = False):
    if compact:
        st.markdown(
            f"""
**{FOUNDER}** · {CITY}  
Email: **{CONTACT_EMAIL}**  
LinkedIn: {LINKEDIN_URL}
""".strip()
        )
    else:
        st.markdown(
            f"""
## Contact

**{FOUNDER}**  
Founder, {BRAND}  
{CITY}

Email: **{CONTACT_EMAIL}**  
LinkedIn: {LINKEDIN_URL}

Independent advisory. Confidential engagements only.  
Not affiliated with any AI vendor.
""".strip()
        )

def footer():
    st.markdown(
        f"""
<div class="footer">
<b>{BRAND}</b><br/>
AI Workflow Impact Assessment<br/><br/>
{FOUNDER} · {CITY}<br/>
{CONTACT_EMAIL}<br/>
linkedin.com/in/ping-shyu<br/><br/>
Independent advisory. Confidential engagements only.<br/>
© {datetime.now().year} {BRAND}. All rights reserved.
</div>
""",
        unsafe_allow_html=True,
    )

# -----------------------------
# Sections (content)
# -----------------------------
def hero():
    st.markdown(f"<div class='smallcaps subtle'>{BRAND}</div>", unsafe_allow_html=True)
    st.markdown("## AI Workflow Impact Assessment")
    st.markdown("### Measuring Operational Stability After AI Integration")

    st.markdown(
        """
AI increases output.  
But output is not the same as effective throughput.

We assess how AI deployment reshapes workflow:

- Where correction load concentrates  
- Where review latency accumulates  
- Where throughput becomes unstable  
- Where operational drag increases
""".strip()
    )
    pills("Independent", "Confidential", "Engineering-based")

def cta_row():
    c1, c2, c3 = st.columns([1.05, 1.05, 1.2])
    with c1:
        st.link_button("Request Assessment", "#request")
    with c2:
        st.link_button("Download Executive Brief", "#brief")
    with c3:
        st.link_button("Initiate Engagement", "#engage")

def proof_band():
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='kpi'>14</div><div class='kpi_label'>Day staff signal window</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='kpi'>7</div><div class='kpi_label'>Days to executive brief after close</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='kpi'>5–7</div><div class='kpi_label'>Pages executive output</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def services():
    st.markdown("## Services")
    st.markdown("### AI Workflow Impact Assessment")

    st.markdown(
        """
AI does not eliminate operational friction.  
It redistributes it.

We identify:

- Rework density  
- Correction latency concentration  
- Human–AI interface pressure  
- Throughput stability risk
""".strip()
    )

    hr()
    st.markdown("### Deliverables")
    colA, colB = st.columns(2)
    with colA:
        st.markdown(
            """
- Workflow redistribution map  
- Friction concentration analysis  
- Throughput stability profile
""".strip()
        )
    with colB:
        st.markdown(
            """
- Executive brief (5–7 pages)  
- Strategic risk summary  
- Engagement next-step options
""".strip()
        )

    hr()
    st.markdown("### Engagement Structure")
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("**Impact Scan**")
        st.markdown("Focused assessment to locate correction load and latency concentration.")
        st.markdown("<div class='subtle'>Typical scope: 1 unit / 1 workflow</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with g2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("**Stability Audit**")
        st.markdown("Deep workflow analysis with stability profile and friction concentration mapping.")
        st.markdown("<div class='subtle'>Typical scope: multi-team workflow</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with g3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("**Enterprise Flow Review**")
        st.markdown("Full-system evaluation for organizations scaling AI across operations.")
        st.markdown("<div class='subtle'>Custom engagement</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def gfi_page():
    st.markdown("## Governance Flow Index (GFI)")
    st.markdown(
        """
An engineering framework for diagnosing operational flow in implemented systems.

GFI measures current workflow conditions:

- Latency load  
- Friction density  
- Throughput stability  
- Workflow conversion integrity

GFI is a diagnostic tool — not a prediction product.
""".strip()
    )
    hr()
    st.markdown("### Typical use cases")
    st.markdown(
        """
- AI-assisted documentation and review loops  
- Automated intake / triage workflows  
- AI-driven compliance review systems  
- Case/claim processing with exception handling  
- Support automation with escalation congestion
""".strip()
    )

def exec_brief():
    st.markdown('<a id="brief"></a>', unsafe_allow_html=True)
    st.markdown("## Executive Brief")
    st.markdown(
        """
A concise overview of:

- AI-induced workflow redistribution  
- Hidden correction load  
- Operational drag concentration  
- Throughput stability patterns
""".strip()
    )

    if os.path.exists(EXEC_BRIEF_PATH):
        with open(EXEC_BRIEF_PATH, "rb") as f:
            st.download_button(
                "Download PDF",
                data=f,
                file_name="GFI_Executive_Brief.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.info(f"To enable download, place your PDF next to app.py as **{EXEC_BRIEF_PATH}**.")

    hr()
    st.markdown("### Request the brief by email (lead capture)")
    with st.form("brief_email_capture", clear_on_submit=True):
        email = st.text_input("Email", placeholder="name@organization.com")
        org = st.text_input("Organization (optional)")
        submitted = st.form_submit_button("Request the brief", use_container_width=True)
        if submitted:
            if not safe_email(email):
                st.error("Invalid email.")
            else:
                append_csv(
                    LEAD_LOG,
                    [
                        datetime.utcnow().isoformat(),
                        "brief_request",
                        org.strip(),
                        "",
                        "",
                        email.strip(),
                        "",
                        "",
                        "",
                    ],
                )
                st.success("Captured.")

def request_assessment():
    st.markdown('<a id="request"></a>', unsafe_allow_html=True)
    st.markdown("## Request Assessment")
    st.markdown(
        """
Submit a short request. We will respond with scope confirmation and next steps.

Confidential engagement. No data sharing.
""".strip()
    )

    with st.form("request_form", clear_on_submit=True):
        org = st.text_input("Organization")
        name = st.text_input("Contact name")
        role = st.text_input("Role / Title")
        email = st.text_input("Email")
        scope = st.selectbox(
            "AI deployment scope",
            [
                "AI-assisted documentation",
                "Automated intake / triage",
                "AI-driven compliance review",
                "Customer support automation",
                "Claims / case processing",
                "Other",
            ],
        )
        concern = st.multiselect(
            "Primary concern (select up to 2)",
            [
                "Rework / correction load rising",
                "Review latency increasing",
                "Quality / error recurrence",
                "Escalations & exception handling",
                "Throughput instability",
                "Staff overload post-AI",
            ],
            max_selections=2,
        )
        notes = st.text_area("Notes (optional)", height=90)

        submitted = st.form_submit_button("Submit request", use_container_width=True)
        if submitted:
            if not safe_email(email):
                st.error("Invalid email.")
            else:
                append_csv(
                    LEAD_LOG,
                    [
                        datetime.utcnow().isoformat(),
                        "assessment_request",
                        org.strip(),
                        name.strip(),
                        role.strip(),
                        email.strip(),
                        scope,
                        "; ".join(concern),
                        notes.strip(),
                    ],
                )
                st.success("Submitted.")

    hr()
    contact_block(compact=True)

def engage():
    st.markdown('<a id="engage"></a>', unsafe_allow_html=True)
    st.markdown("## Initiate Engagement")
    st.markdown("Secure checkout (optional) and post-payment intake.")

    if STRIPE_BUY_BUTTON_HTML.strip():
        st.markdown("### Secure checkout")
        components.html(STRIPE_BUY_BUTTON_HTML, height=210)
        st.caption("Set the Stripe success URL to your intake page.")
    else:
        st.info("Stripe buy button not configured.")

    hr()
    st.markdown("### Post-payment intake")
    st.markdown(INTAKE_URL)
    st.caption("Replace INTAKE_URL when your intake page is live.")

    hr()
    contact_block(compact=True)

def about():
    contact_block(compact=False)

def home():
    hero()
    cta_row()
    hr()
    proof_band()
    hr()
    services()
    hr()
    exec_brief()
    hr()
    request_assessment()
    hr()
    engage()
    footer()

# -----------------------------
# Sidebar navigation
# -----------------------------
with st.sidebar:
    st.markdown(f"### {BRAND}")
    st.caption("High-trust, confidential workflow diagnostics.")
    page = st.radio(
        "Navigate",
        ["Home", "Services", "GFI", "Executive Brief", "Request", "Engage", "About"],
        index=0,
        label_visibility="collapsed",
    )
    hr()
    st.caption(f"{FOUNDER} · {CITY}")
    st.caption(CONTACT_EMAIL)
    st.caption("linkedin.com/in/ping-shyu")

# -----------------------------
# Render
# -----------------------------
if page == "Home":
    home()
elif page == "Services":
    services()
    footer()
elif page == "GFI":
    gfi_page()
    footer()
elif page == "Executive Brief":
    exec_brief()
    footer()
elif page == "Request":
    request_assessment()
    footer()
elif page == "Engage":
    engage()
    footer()
elif page == "About":
    about()
    footer()
