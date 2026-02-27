import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="GFI Flow Intelligence — Capital Efficiency Verification",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🔍"
)

# ============================================================================
# STRIPE PAYMENT LINKS
# ============================================================================
STRIPE_LINK_999  = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_LINK_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"
STRIPE_LINK_9999 = "https://buy.stripe.com/8x228t3WyazS7fL4vR3VC02"

# ============================================================================
# DESIGN TOKENS — matches gfiintel.com exactly
# ============================================================================
BG       = "#141d2e"
SURF     = "#1c2740"
SURF2    = "#22304e"
BORDER   = "rgba(255,255,255,0.08)"
TEXT     = "#edf0f8"
MUTED    = "#8fa3c0"
DIM      = "#4a6080"
ACCENT   = "#c8f542"   # lime green
BLUE     = "#4da3ff"
DANGER   = "#ff6b6b"
WARN     = "#f59e0b"
SUCCESS  = "#34d399"

# ============================================================================
# GLOBAL CSS
# ============================================================================
st.markdown(f"""
<style>
  /* ── Base ── */
  html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
    background-color: {BG} !important;
    color: {TEXT} !important;
    font-family: 'DM Sans', system-ui, sans-serif;
  }}

  [data-testid="stSidebar"] {{ background-color: {SURF} !important; }}

  /* Remove default padding */
  .block-container {{ padding-top: 2rem !important; max-width: 1100px; }}

  /* ── Typography ── */
  h1, h2, h3, h4, h5 {{ color: {TEXT} !important; font-weight: 500 !important; letter-spacing: -0.01em; }}
  p, li, span, div {{ color: {MUTED}; }}
  strong {{ color: {TEXT} !important; }}

  /* ── Inputs ── */
  [data-testid="stTextInput"] input,
  [data-testid="stNumberInput"] input,
  [data-testid="stSelectbox"] div[data-baseweb="select"] {{
    background-color: {SURF} !important;
    border: 1px solid {BORDER} !important;
    color: {TEXT} !important;
    border-radius: 6px !important;
  }}
  [data-testid="stSelectbox"] div[data-baseweb="select"]:hover {{
    border-color: rgba(255,255,255,0.18) !important;
  }}
  [data-baseweb="popover"] ul {{
    background-color: {SURF2} !important;
  }}

  /* Sliders */
  [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {{
    background-color: {ACCENT} !important;
  }}
  [data-testid="stSlider"] div[data-testid="stTickBarMin"],
  [data-testid="stSlider"] div[data-testid="stTickBarMax"] {{
    color: {MUTED} !important;
  }}

  /* ── Tabs ── */
  [data-testid="stTabs"] [data-baseweb="tab-list"] {{
    background-color: {SURF} !important;
    border-radius: 8px;
    padding: 4px;
    gap: 4px;
    border: 1px solid {BORDER};
  }}
  [data-testid="stTabs"] [data-baseweb="tab"] {{
    background-color: transparent !important;
    color: {MUTED} !important;
    border-radius: 6px !important;
    font-size: 14px !important;
    padding: 8px 16px !important;
    transition: all .2s;
  }}
  [data-testid="stTabs"] [aria-selected="true"] {{
    background-color: {SURF2} !important;
    color: {TEXT} !important;
  }}
  [data-testid="stTabs"] [data-baseweb="tab-border"] {{ display: none !important; }}

  /* ── Form submit button ── */
  [data-testid="stFormSubmitButton"] button {{
    background-color: {ACCENT} !important;
    color: #0d1117 !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 28px !important;
    font-size: 16px !important;
    transition: opacity .2s !important;
    width: 100% !important;
  }}
  [data-testid="stFormSubmitButton"] button:hover {{
    opacity: 0.88 !important;
  }}

  /* ── Expanders ── */
  [data-testid="stExpander"] {{
    background-color: {SURF} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 8px !important;
    margin-bottom: 8px;
  }}
  [data-testid="stExpander"] summary {{
    color: {TEXT} !important;
    font-size: 15px !important;
  }}

  /* ── Alerts ── */
  [data-testid="stAlert"] {{
    background-color: {SURF} !important;
    border-radius: 8px !important;
    border: 1px solid {BORDER} !important;
  }}

  /* ── Divider ── */
  hr {{ border-color: {BORDER} !important; }}

  /* ── Plotly charts background ── */
  .js-plotly-plot .plotly {{ background: transparent !important; }}

  /* ── Custom components ── */

  .eyebrow {{
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: {ACCENT};
    margin-bottom: 8px;
  }}

  .card {{
    background: {SURF};
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: clamp(20px, 3vw, 32px);
  }}

  .card-accent {{
    background: rgba(200,245,66,0.03);
    border-color: rgba(200,245,66,0.18);
  }}

  .price-card {{
    background: {SURF};
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: 28px;
    text-align: center;
    height: 100%;
    transition: border-color .2s, transform .25s;
  }}
  .price-card:hover {{
    border-color: rgba(200,245,66,0.22);
    transform: translateY(-3px);
  }}
  .price-card.featured {{
    background: rgba(200,245,66,0.03);
    border-color: rgba(200,245,66,0.2);
  }}

  .price-tier {{
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: {MUTED};
    margin-bottom: 12px;
  }}
  .featured .price-tier {{ color: {ACCENT}; }}

  .price-amount {{
    font-size: 48px;
    font-weight: 600;
    color: {TEXT};
    line-height: 1;
    margin-bottom: 4px;
  }}
  .price-cur {{ font-size: 20px; color: {MUTED}; vertical-align: top; line-height: 1.3; }}

  .feat-list {{
    list-style: none;
    padding: 0;
    text-align: left;
    margin: 16px 0 24px;
  }}
  .feat-list li {{
    font-size: 14px;
    color: {MUTED};
    padding: 8px 0;
    border-bottom: 1px solid {BORDER};
    display: flex;
    gap: 8px;
  }}
  .feat-list li::before {{ content: '→'; color: {ACCENT}; flex-shrink: 0; }}

  .cta-btn {{
    display: block;
    width: 100%;
    text-align: center;
    padding: 13px 20px;
    background: {SURF2};
    color: {TEXT};
    border: 1px solid {BORDER};
    border-radius: 7px;
    font-size: 14px;
    text-decoration: none;
    transition: background .2s, border-color .2s;
    margin-top: 8px;
    cursor: pointer;
  }}
  .cta-btn:hover {{ background: rgba(255,255,255,0.04); border-color: rgba(255,255,255,0.18); color: {TEXT}; }}

  .cta-btn-primary {{
    background: {ACCENT};
    color: #0d1117;
    border-color: transparent;
    font-weight: 600;
  }}
  .cta-btn-primary:hover {{ opacity: 0.88; background: {ACCENT}; color: #0d1117; }}

  .result-hero {{
    background: {SURF};
    border: 1px solid rgba(255,107,107,0.25);
    border-radius: 12px;
    padding: 2.5rem;
    text-align: center;
    margin: 1.5rem 0;
  }}
  .result-num {{
    font-size: 56px;
    font-weight: 600;
    color: {DANGER};
    line-height: 1;
    margin: 1rem 0;
  }}

  .insight-box {{
    background: {SURF};
    border: 1px solid {BORDER};
    border-left: 3px solid {ACCENT};
    border-radius: 8px;
    padding: 20px 24px;
    margin: 16px 0;
  }}

  .risk-hi  {{ color: {DANGER}; }}
  .risk-med {{ color: {WARN}; }}
  .risk-lo  {{ color: {SUCCESS}; }}

  .guarantee {{
    background: rgba(52,211,153,0.05);
    border: 1px solid rgba(52,211,153,0.2);
    border-radius: 8px;
    padding: 20px 24px;
    text-align: center;
    margin: 24px 0;
  }}
  .guarantee h4 {{ color: {SUCCESS} !important; }}

  .badge {{
    display: inline-block;
    background: rgba(200,245,66,0.12);
    color: {ACCENT};
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 12px;
  }}

  .two-col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
  }}
  @media (max-width: 640px) {{
    .two-col {{ grid-template-columns: 1fr; }}
    .result-num {{ font-size: 40px; }}
  }}
</style>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE
# ============================================================================
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'calculated_leak' not in st.session_state:
    st.session_state.calculated_leak = 0
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 0

# ============================================================================
# HEADER
# ============================================================================
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("GFILOGO.png", width=80)
    except:
        st.markdown(f'<div style="font-family:monospace;font-size:22px;color:{ACCENT};font-weight:600;padding-top:8px">GFI</div>', unsafe_allow_html=True)

with col_title:
    st.markdown(f"""
    <div style="padding: 4px 0 0 8px;">
      <div class="eyebrow">GFI Flow Intelligence · Boston</div>
      <div style="font-size: 22px; font-weight: 500; color: {TEXT}; line-height: 1.2;">
        Capital Efficiency Verification
      </div>
      <div style="font-size: 14px; color: {MUTED}; margin-top: 4px;">
        Measure execution before transformation. Prove it after.
        &nbsp;·&nbsp;
        <span style="color:{ACCENT}">Free diagnostic — 12 minutes</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f'<hr style="border-color:{BORDER};margin:16px 0 24px;">', unsafe_allow_html=True)

# ============================================================================
# FRAMEWORK OVERVIEW
# ============================================================================
st.markdown(f"""
<div class="card" style="margin-bottom:24px;">
  <div class="eyebrow">GL Framework</div>
  <div style="font-size:18px;color:{TEXT};margin-bottom:12px;font-weight:500;">
    Structural Intelligence Layer for Institutional Transformation
  </div>
  <p style="color:{MUTED};line-height:1.75;max-width:800px;">
    Most engagements stop at implementation. GFI measures structural risk 
    <strong>before</strong> transformation and proves structural improvement <strong>after</strong> — 
    creating measurable, defensible ROI.
  </p>
</div>
<div class="two-col" style="margin-bottom:24px;">
  <div class="card">
    <div class="eyebrow">Phase I · Pre-Transformation</div>
    <div style="font-size:16px;color:{TEXT};margin-bottom:10px;font-weight:500;">Quantify structural execution risk</div>
    <ul style="color:{MUTED};line-height:1.85;padding-left:16px;margin:0 0 16px;">
      <li>Decision latency density mapping</li>
      <li>Organizational friction coefficient</li>
      <li>Capacity loss baseline measurement</li>
      <li>Execution readiness index</li>
    </ul>
    <div style="background:rgba(77,163,255,0.07);border:1px solid rgba(77,163,255,0.15);border-radius:6px;padding:10px 14px;font-size:13px;color:{BLUE};">
      Output: Executive Execution Readiness Scorecard
    </div>
  </div>
  <div class="card">
    <div class="eyebrow">Phase II · Post-Transformation</div>
    <div style="font-size:16px;color:{TEXT};margin-bottom:10px;font-weight:500;">Prove structural improvement</div>
    <ul style="color:{MUTED};line-height:1.85;padding-left:16px;margin:0 0 16px;">
      <li>Friction reduction delta analysis</li>
      <li>Latency compression measurement</li>
      <li>Execution capacity expansion rate</li>
      <li>Institutional resilience index</li>
    </ul>
    <div style="background:rgba(200,245,66,0.06);border:1px solid rgba(200,245,66,0.18);border-radius:6px;padding:10px 14px;font-size:13px;color:{ACCENT};">
      Output: Transformation Impact Certification Report
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<hr style="border-color:{BORDER};margin:8px 0 28px;">', unsafe_allow_html=True)

# ============================================================================
# TABS
# ============================================================================
tab1, tab2, tab3 = st.tabs(["Free Assessment", "Sample Report", "Pricing"])

# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — FREE ASSESSMENT
# ════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown(f'<div style="font-size:22px;font-weight:500;color:{TEXT};margin-bottom:4px;">GL Friction Calculator</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{MUTED};margin-bottom:24px;">Answer 12 questions to estimate your annual capital efficiency loss.</p>', unsafe_allow_html=True)

    with st.form("assessment_form"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f'<div style="font-size:13px;font-family:monospace;letter-spacing:.1em;text-transform:uppercase;color:{ACCENT};margin-bottom:12px;">Organisation</div>', unsafe_allow_html=True)
            company_name = st.text_input("Company Name", placeholder="Acme Corp")
            employee_count = st.selectbox("Number of Employees", ["1-10","11-50","51-200","201-500","501-1000","1000+"])
            industry = st.selectbox("Industry", ["Technology/SaaS","Professional Services","Finance","Healthcare","Manufacturing","Retail","Other"])
            avg_salary = st.number_input("Average Annual Salary (USD)", min_value=30000, value=75000, step=5000)
            revenue_per_employee = st.number_input("Annual Revenue per Employee (USD)", min_value=50000, value=150000, step=10000)
            meeting_hours_per_week = st.slider("Avg Meeting Hours / Employee / Week", 0, 40, 15)

        with col2:
            st.markdown(f'<div style="font-size:13px;font-family:monospace;letter-spacing:.1em;text-transform:uppercase;color:{ACCENT};margin-bottom:12px;">Friction Inputs</div>', unsafe_allow_html=True)
            approval_layers = st.slider("Approval Layers for Key Decisions", 1, 10, 3)
            project_delay_pct = st.slider("Project Delay Rate (%)", 0, 100, 30)
            rework_pct = st.slider("Rework Due to Miscommunication (%)", 0, 50, 15)
            decision_time_days = st.slider("Avg Days to Make Strategic Decisions", 1, 90, 14)
            turnover_rate = st.slider("Annual Employee Turnover Rate (%)", 0, 50, 15)
            customer_complaint_rate = st.slider("Customer Complaint Rate (per 100)", 0, 50, 5)

        st.form_submit_button("Calculate Capital Efficiency Loss →")

    # ── RESULTS ──
    if st.session_state.get('assessment_complete'):

        emp_map = {"1-10":5,"11-50":30,"51-200":125,"201-500":350,"501-1000":750,"1000+":1500}
        employees = emp_map.get(st.session_state.get('_emp_count','51-200'), 125)
        total_leak = st.session_state.calculated_leak
        risk_score = st.session_state.risk_score
        company    = st.session_state.get('company_name','Your Company')
        breakdown  = st.session_state.get('breakdown', {})

        st.markdown(f"""
        <div class="result-hero">
          <div class="eyebrow">Assessment Complete</div>
          <div style="color:{TEXT};font-size:17px;margin-bottom:4px;">{company} · Estimated Annual Capital Efficiency Loss</div>
          <div class="result-num">${total_leak:,.0f}</div>
          <div style="color:{MUTED};font-size:15px;">${total_leak/max(employees,1):,.0f} per employee per year</div>
        </div>
        """, unsafe_allow_html=True)

        col_gauge, col_risk = st.columns(2)

        with col_gauge:
            risk_color = DANGER if risk_score > 70 else WARN if risk_score > 40 else SUCCESS
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk_score,
                domain={'x':[0,1],'y':[0,1]},
                title={'text':"Operational Friction Score", 'font':{'color':TEXT,'size':14}},
                number={'font':{'color':TEXT}},
                gauge={
                    'axis':{'range':[0,100],'tickcolor':MUTED,'tickfont':{'color':MUTED}},
                    'bar':{'color':risk_color},
                    'bgcolor':SURF2,
                    'bordercolor':BORDER,
                    'steps':[
                        {'range':[0,40],'color':'rgba(52,211,153,0.1)'},
                        {'range':[40,70],'color':'rgba(245,158,11,0.1)'},
                        {'range':[70,100],'color':'rgba(255,107,107,0.1)'}
                    ],
                }
            ))
            fig.update_layout(
                height=280,
                paper_bgcolor=SURF,
                plot_bgcolor=SURF,
                margin=dict(t=40,b=20,l=20,r=20),
                font={'color':TEXT}
            )
            st.plotly_chart(fig, use_container_width=True)

        with col_risk:
            if risk_score > 70:
                level, cls, msg = "HIGH RISK", "risk-hi", "Multiple critical friction sources detected. Immediate GL verification recommended."
            elif risk_score > 40:
                level, cls, msg = "MODERATE RISK", "risk-med", "Several friction points are impacting capital velocity. Structured verification will identify priority interventions."
            else:
                level, cls, msg = "LOW RISK", "risk-lo", "Operations show strong flow characteristics. GL verification can confirm and benchmark efficiency gains."

            st.markdown(f"""
            <div class="card" style="height:100%;">
              <div class="eyebrow">Risk Profile</div>
              <div style="font-size:22px;font-weight:600;" class="{cls}">{level}</div>
              <p style="color:{MUTED};margin-top:12px;line-height:1.7;">{msg}</p>
            </div>
            """, unsafe_allow_html=True)

        # Breakdown chart
        if breakdown:
            st.markdown(f'<div style="font-size:16px;font-weight:500;color:{TEXT};margin:24px 0 12px;">Where Capital Is Leaking</div>', unsafe_allow_html=True)
            df = pd.DataFrame({'Category': list(breakdown.keys()), 'Annual Cost': list(breakdown.values())})
            fig2 = px.bar(df, x='Category', y='Annual Cost',
                         color='Annual Cost', color_continuous_scale=[[0,SURF2],[0.5,BLUE],[1,DANGER]])
            fig2.update_layout(
                height=320,
                paper_bgcolor=SURF,
                plot_bgcolor=SURF,
                font={'color':TEXT},
                showlegend=False,
                coloraxis_showscale=False,
                xaxis=dict(tickfont={'color':MUTED}, gridcolor=BORDER),
                yaxis=dict(tickfont={'color':MUTED}, gridcolor=BORDER, title='Annual Cost (USD)')
            )
            fig2.update_traces(marker_line_color=BG, marker_line_width=1)
            st.plotly_chart(fig2, use_container_width=True)

        # CTA
        st.markdown(f"""
        <div class="insight-box">
          <div style="font-size:16px;font-weight:500;color:{TEXT};margin-bottom:10px;">This estimate is the surface. GL verification goes deeper.</div>
          <p style="color:{MUTED};line-height:1.75;margin:0;">
            The calculator gives you magnitude. A full GL assessment identifies which specific layers are generating friction, 
            quantifies the pre/post delta, and produces a board-ready verification report.
          </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f'<div style="font-size:16px;font-weight:500;color:{TEXT};margin:24px 0 16px;">Start Verification</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
            <div class="price-card">
              <div class="price-tier">Diagnostic</div>
              <div class="price-amount"><span class="price-cur">$</span>999</div>
              <p style="color:{MUTED};font-size:14px;margin:10px 0 16px;">Baseline GL assessment. Identify friction before committing to transformation.</p>
              <ul class="feat-list">
                <li>12-question GL diagnostic</li>
                <li>Friction source identification</li>
                <li>GL score + risk classification</li>
                <li>12-page PDF report</li>
                <li>48-hour delivery</li>
              </ul>
              <a href="{STRIPE_LINK_999}" target="_blank" class="cta-btn">Begin Assessment →</a>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="price-card featured">
              <div class="badge">Most Popular</div>
              <div class="price-tier">Verification</div>
              <div class="price-amount"><span class="price-cur">$</span>4,999</div>
              <p style="color:{MUTED};font-size:14px;margin:10px 0 16px;">Before & after GL measurement. Verify whether transformation improved capital efficiency.</p>
              <ul class="feat-list">
                <li>Everything in Diagnostic</li>
                <li>Pre/post GL delta analysis</li>
                <li>Layer-by-layer friction map</li>
                <li>Executive strategy session (2hr)</li>
                <li>30-day follow-up support</li>
              </ul>
              <a href="{STRIPE_LINK_4999}" target="_blank" class="cta-btn cta-btn-primary">Start Verification →</a>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="guarantee">
          <h4>100% Money-Back Guarantee</h4>
          <p style="color:{MUTED};margin-top:8px;line-height:1.7;">
            If you don't discover at least <strong>5× the report cost</strong> in actionable savings, we refund in full. No questions.
          </p>
        </div>
        """, unsafe_allow_html=True)

    # Handle form submission
    elif st.session_state.get('_submitted'):
        emp_map = {"1-10":5,"11-50":30,"51-200":125,"201-500":350,"501-1000":750,"1000+":1500}
        employees = emp_map.get(st.session_state._emp_count, 125)
        avg_sal   = st.session_state._avg_salary
        rev_pe    = st.session_state._rev_pe
        hourly    = avg_sal / 2080

        mtg_cost   = st.session_state._meeting_h * 0.4 * 50 * employees * hourly
        delay_cost = (st.session_state._delay_pct/100) * (rev_pe*0.3) * employees * 0.2
        rework_cost= (st.session_state._rework_pct/100) * avg_sal * employees * 0.15
        dec_cost   = ((st.session_state._dec_days/7)-1) * 500 * employees * 10
        turn_cost  = (st.session_state._turnover/100) * employees * avg_sal * 1.5
        cust_cost  = (st.session_state._cust_rate/100) * employees * (rev_pe*2) * 0.1

        total_leak = max(mtg_cost+delay_cost+rework_cost+dec_cost+turn_cost+cust_cost, 0)
        risk_factors = [
            (st.session_state._approval-1)*10,
            st.session_state._delay_pct*0.5,
            st.session_state._rework_pct*1.5,
            (st.session_state._dec_days/30)*20,
            st.session_state._turnover,
            st.session_state._cust_rate*1.5
        ]
        risk_score = min(sum(risk_factors)/len(risk_factors), 100)

        st.session_state.assessment_complete = True
        st.session_state.calculated_leak = total_leak
        st.session_state.risk_score = risk_score
        st.session_state.company_name = st.session_state._company
        st.session_state.employees = employees
        st.session_state.breakdown = {
            "Meeting Overhead": mtg_cost,
            "Project Delays": delay_cost,
            "Rework": rework_cost,
            "Decision Bottlenecks": dec_cost,
            "Turnover": turn_cost,
            "Customer Friction": cust_cost
        }
        st.rerun()

# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — SAMPLE REPORT
# ════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown(f'<div style="font-size:22px;font-weight:500;color:{TEXT};margin-bottom:4px;">Sample Report Preview</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{MUTED};margin-bottom:24px;">Your actual report will be fully customized with your organisation\'s data.</p>', unsafe_allow_html=True)

    sections = [
        ("Page 1 — Executive Summary", f"""
**GL VERIFICATION REPORT**
*Prepared for: [Organisation Name]*  ·  *Date: [Report Date]*  ·  *Analyst: Ping Xu (徐萍), GFI Flow Intelligence*

---

**Key Findings**

🔴 Primary Friction Source: [Largest cost category]  
💰 Total Annual Efficiency Loss: $[X]  
📊 GL Score (Pre-Transformation): [X.XX]  
📈 Recovery Potential: $[X] within 90 days
"""),
        ("Pages 2–3 — Friction Layer Analysis", f"""
| Layer | Annual Cost | % of Total | Severity |
|-------|-------------|------------|----------|
| Meeting Overhead | $[X] | [X]% | High |
| Project Delays | $[X] | [X]% | Medium |
| Rework & Errors | $[X] | [X]% | High |
| Decision Bottlenecks | $[X] | [X]% | Medium |
| Turnover Costs | $[X] | [X]% | High |
| Customer Friction | $[X] | [X]% | Low |
"""),
        ("Pages 4–5 — Top 3 Friction Sources", """
**Bottleneck #1: [Specific Issue]**  
Annual Cost Impact: $[X] · Affected Layers: [Teams]  
Root Cause: [Structural issue]  

Recommended Intervention:  
1. [Specific action]  
2. [Specific action]  
3. [Specific action]  

Expected GL Delta: +[X.XX] within [timeframe]
"""),
        ("Pages 6–7 — GL Score & Benchmarks", """
GL score breakdown vs. international case benchmarks:

| System | Domain | GL Score |
|--------|---------|----------|
| Estonia e-Governance | Digital Identity | 4.17 |
| Singapore SkillsFuture | Workforce | 3.84 |
| Your Organisation (pre) | [Domain] | [X.XX] |
| UK NHS Digital | Healthcare | 0.89 |
"""),
        ("Pages 8–12 — Interventions & Methodology", """
**90-Day Intervention Roadmap**

Phase 1 (0–30 days): Quick wins — immediate friction removal  
Phase 2 (30–60 days): Structural adjustments  
Phase 3 (60–90 days): GL re-measurement and delta confirmation  

**Methodology**  
All scores derived from the GL formula: GL = (Fs × Vn) / (Pd × Cf)  
Variable definitions, data sources, and confidence intervals documented in full.
"""),
    ]

    for title, content in sections:
        with st.expander(title):
            st.markdown(content)

# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — PRICING
# ════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown(f'<div style="font-size:22px;font-weight:500;color:{TEXT};margin-bottom:4px;">Engagement Tiers</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{MUTED};margin-bottom:28px;">Three levels for different transformation stages.</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="price-card">
          <div class="price-tier">Diagnostic</div>
          <div class="price-amount"><span class="price-cur">$</span>999</div>
          <p style="color:{MUTED};font-size:14px;margin:10px 0 16px;">Baseline GL assessment. Identify friction before committing to transformation.</p>
          <ul class="feat-list">
            <li>12-question GL diagnostic</li>
            <li>Friction source identification</li>
            <li>GL score + risk classification</li>
            <li>12-page PDF report</li>
            <li>48-hour delivery</li>
          </ul>
          <a href="{STRIPE_LINK_999}" target="_blank" class="cta-btn">Begin Assessment →</a>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="price-card featured">
          <div class="badge">Most Popular</div>
          <div class="price-tier">Verification</div>
          <div class="price-amount"><span class="price-cur">$</span>4,999</div>
          <p style="color:{MUTED};font-size:14px;margin:10px 0 16px;">Before & after GL measurement. Verify whether transformation improved capital efficiency.</p>
          <ul class="feat-list">
            <li>Everything in Diagnostic</li>
            <li>Pre/post GL delta analysis</li>
            <li>Layer-by-layer friction map</li>
            <li>Executive strategy session (2hr)</li>
            <li>30-day follow-up support</li>
          </ul>
          <a href="{STRIPE_LINK_4999}" target="_blank" class="cta-btn cta-btn-primary">Start Verification →</a>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="price-card">
          <div class="price-tier">Board-Ready</div>
          <div class="price-amount"><span class="price-cur">$</span>9,999</div>
          <p style="color:{MUTED};font-size:14px;margin:10px 0 16px;">Full independent verification for board presentation, investor reporting, or M&A due diligence.</p>
          <ul class="feat-list">
            <li>Everything in Verification</li>
            <li>Independent auditor sign-off</li>
            <li>Board presentation format</li>
            <li>Investor / LP summary</li>
            <li>Quarterly tracking</li>
          </ul>
          <a href="{STRIPE_LINK_9999}" target="_blank" class="cta-btn">Engage →</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="guarantee" style="margin-top:32px;">
      <h4>100% Money-Back Guarantee</h4>
      <p style="color:{MUTED};margin-top:8px;line-height:1.7;">
        If you don't discover at least <strong>5× the report cost</strong> in actionable savings, we refund in full. No questions.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div style="font-size:16px;font-weight:500;color:{TEXT};margin:32px 0 16px;">Frequently Asked Questions</div>', unsafe_allow_html=True)

    faqs = [
        ("What makes this different from traditional consulting?", f"""
Traditional consulting: $50K–$200K+, 3–6 months, generalised frameworks.

GL Verification: Fixed transparent pricing · Delivered in 24–48 hours · Focused specifically on capital efficiency delta · Actionable from day one.
"""),
        ("How is the GL score calculated?", f"""
The GL formula: **GL = (Fs × Vn) / (Pd × Cf)**

- **Fs** Flow Success Rate (0–1)
- **Vn** Strategic Value (0–10)
- **Pd** Pain Duration (annual hours)
- **Cf** Cognitive Friction Index (0–10)

Full methodology available at [gfiintel.com/methodology.html](https://gfiintel.com/methodology.html)
"""),
        ("What if I don't find actionable savings?", """
100% money-back guarantee. If the report doesn't identify at least 5× its cost in potential savings, full refund, no questions.
"""),
    ]

    for q, a in faqs:
        with st.expander(q):
            st.markdown(a)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown(f'<hr style="border-color:{BORDER};margin:40px 0 24px;">', unsafe_allow_html=True)
fc1, fc2 = st.columns([1, 4])
with fc1:
    try:
        st.image("GFILOGO.png", width=60)
    except:
        pass
with fc2:
    st.markdown(f"""
    <div style="padding-top:4px;">
      <div style="font-size:14px;font-weight:500;color:{TEXT};">GFI Flow Intelligence</div>
      <div style="font-size:13px;color:{MUTED};margin-top:4px;">
        Created by Ping Xu (徐萍) · Boston, MA · 
        <a href="mailto:gfi@gfiintel.com" style="color:{MUTED};text-decoration:none;">gfi@gfiintel.com</a>
        &nbsp;·&nbsp;
        <a href="https://gfiintel.com" style="color:{MUTED};text-decoration:none;">gfiintel.com</a>
      </div>
      <div style="font-size:12px;color:{DIM};margin-top:4px;">© 2026 All Rights Reserved</div>
    </div>
    """, unsafe_allow_html=True)
