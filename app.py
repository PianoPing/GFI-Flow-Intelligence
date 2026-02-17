import streamlit as st
import plotly.graph_objects as go

# 1. 設置
st.set_page_config(page_title="GFI Hidden Profit Leak Report", layout="wide")

# 2. 強力視覺 CSS
st.markdown("""
<style>
    .main-title { font-size: 3.5rem; font-weight: 800; color: #1e3a8a; text-align: center; margin-bottom: 0.5rem; }
    .value-card { background: white; padding: 1.5rem; border-radius: 10px; border-top: 5px solid #1e3a8a;
                  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); height: 100%; }
    .alert-box { background: #fff1f2; padding: 2rem; border-radius: 12px; border: 2px solid #be123c; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# 3. 價值說明區
st.markdown('<h1 class="main-title">GFI Hidden Profit Leak Audit™</h1>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:1.2rem; color:#475569;'>Detect and quantify the “Efficiency Tax” draining your company’s net profit.</p>",
    unsafe_allow_html=True
)

st.divider()

col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    st.markdown('<div class="value-card"><h4>🚫 Stop Rework</h4><p>Quantify wasted hours from revision loops and duplicated effort.</p></div>', unsafe_allow_html=True)
with col_v2:
    st.markdown('<div class="value-card"><h4>⚡ Accelerate Decisions</h4><p>Measure the financial cost of administrative delays and approval bottlenecks.</p></div>', unsafe_allow_html=True)
with col_v3:
    st.markdown('<div class="value-card"><h4>📉 Reduce Churn</h4><p>Estimate opportunity loss from internal friction that compresses output and retention.</p></div>', unsafe_allow_html=True)

st.write("")
st.subheader("🔍 Preliminary Risk Assessment")

# 4. 診斷區（先給 submitted 預設值，避免未定義）
submitted = False

with st.form("audit_form"):
    c1, c2 = st.columns(2)
    with c1:
        n_emp = st.number_input("Headcount (Full-Time Equivalents)", min_value=1, value=50, step=1)
        avg_rate = st.number_input("Avg. Fully-Loaded Hourly Rate ($)", min_value=1, value=85, step=1)
        rework_rate = st.slider("Estimated Rework/Revision Rate (%)", 0, 100, 20)
    with c2:
        delay_hrs = st.slider("Weekly Delay per Employee (Hours)", 0, 20, 5)
        multiplier = st.selectbox("Revenue Multiplier (Value generated per $1 of cost)", [3.0, 5.0, 8.0, 10.0])

    submitted = st.form_submit_button("GENERATE FINANCIAL IMPACT PREVIEW")

if submitted:
    # 5. 計算邏輯（把 rework_rate 真的算進去）
    weeks = 52

    # Delay loss = paid time that produces no output
    direct_delay_loss = n_emp * avg_rate * delay_hrs * weeks

    # Rework loss = additional repeated effort (approx. proportional to delay burden)
    rework_loss = n_emp * avg_rate * (delay_hrs * (rework_rate / 100.0)) * weeks

    # Opportunity cost = scaled value loss beyond direct labor cost
    opportunity_cost = (direct_delay_loss + rework_loss) * (multiplier - 1.0)

    leak_total = direct_delay_loss + rework_loss + opportunity_cost

    st.markdown(f"""
    <div class="alert-box">
        <h3 style="color:#be123c; margin:0;">AUDIT ALERT: LEAKAGE DETECTED</h3>
        <p style="font-size:1.1rem; color:#475569; margin-top:10px;">Estimated annual leakage (direct + opportunity):</p>
        <h1 style="color:#be123c; font-size:4.2rem; margin:10px 0;">${leak_total:,.0f} / Year</h1>
        <p style="color:#64748b; margin:0;">Preview estimate. Full audit refines by department and process variance bands.</p>
    </div>
    """, unsafe_allow_html=True)

    # 6. Waterfall（用正值，更像財務報告）
    fig = go.Figure(go.Waterfall(
        name="Profit Leak", orientation="v",
        measure=["relative", "relative", "relative", "total"],
        x=["Direct Delay Loss", "Rework Loss", "Opportunity Cost", "Total Leakage"],
        textposition="outside",
        text=[f"{direct_delay_loss:,.0f}", f"{rework_loss:,.0f}", f"{opportunity_cost:,.0f}", f"{leak_total:,.0f}"],
        y=[direct_delay_loss, rework_loss, opportunity_cost, 0],
        connector={"line": {"color": "rgba(80,80,80,0.6)"}},
    ))
    fig.update_layout(title="Breakdown of Identified Losses (Preview)", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.write("### 📄 Get the Full Audit & Action Plan")
    st.write("This preview is a fast estimate. The full report provides department-by-department breakdown and 3 immediate denominator fixes.")
    st.link_button("REQUEST FULL AUDIT (Intake)", "https://example.com/intake")  # 換成你的 Stripe 或 Intake 連結

# 7. 側邊欄
st.sidebar.markdown("### GFI Intelligence")
st.sidebar.write("Institutional Risk Auditing")
st.sidebar.caption("© 2026 GFI Intelligence | Boston, MA")
