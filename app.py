
# app.py  — GFI Intel CN/EN Homepage (FULL REPLACE)
# Put GFILOGO.png in the SAME folder as this app.py

import streamlit as st
from pathlib import Path

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="GFI Flow Intelligence | 中国版",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

LOGO_PATH = "GFILOGO.png"

CN_FORM_URL = "https://forms.gle/KmFdjdu97bC43CYL6"
CN_SITE_URL = "https://gfi-intel-cn.streamlit.app/"
EN_SITE_URL = "https://gfi-intelligence.streamlit.app/"
CONTACT_EMAIL = "pingshyu@gmail.com"

# =========================
# CSS (KEEP)
# =========================
st.markdown(
    """
<style>
/* Global */
html, body, [class*="css"] { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB",
"Microsoft YaHei", Arial, sans-serif; }
.block-container { padding-top: 1.2rem; padding-bottom: 3.5rem; max-width: 1200px; }

/* Top bar */
.topbar {
  border-radius: 18px;
  padding: 14px 18px;
  background: linear-gradient(135deg, rgba(10,45,95,0.92), rgba(18,140,155,0.85));
  border: 1px solid rgba(255,255,255,0.14);
  box-shadow: 0 10px 30px rgba(0,0,0,0.18);
  margin-bottom: 18px;
}

/* Make radio visible + pill style */
div[role="radiogroup"] { gap: 10px !important; }
div[role="radiogroup"] label { 
  padding: 6px 12px !important; 
  border-radius: 999px !important;
  border: 1px solid rgba(255,255,255,0.26) !important;
  background: rgba(255,255,255,0.10) !important;
  color: white !important;
  font-weight: 600 !important;
}
div[role="radiogroup"] label:hover {
  background: rgba(255,255,255,0.18) !important;
}
div[role="radiogroup"] input:checked + div {
  background: rgba(255,255,255,0.22) !important;
  border-radius: 999px !important;
}

/* Hero */
.hero {
  border-radius: 22px;
  padding: 22px 22px 18px 22px;
  background: radial-gradient(1200px 420px at 20% 0%, rgba(30,180,200,0.20), rgba(0,0,0,0) 60%),
              radial-gradient(900px 360px at 80% 10%, rgba(80,120,255,0.18), rgba(0,0,0,0) 60%),
              rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.10);
  box-shadow: 0 12px 40px rgba(0,0,0,0.18);
  margin-bottom: 18px;
}

/* Cards */
.card {
  border-radius: 18px;
  padding: 18px 18px 16px 18px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.10);
  box-shadow: 0 10px 30px rgba(0,0,0,0.14);
}
.card h3 { margin: 0 0 8px 0; }
.muted { opacity: 0.82; }
.kicker { letter-spacing: .12em; text-transform: uppercase; font-size: 12px; opacity: .85; }
.divline { height: 1px; background: rgba(255,255,255,0.10); margin: 12px 0 12px 0; }

.badge {
  display:inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.14);
  margin-right: 6px;
}

.small { font-size: 13px; opacity: 0.86; }

/* Buttons */
.stButton > button {
  border-radius: 12px !important;
  padding: 10px 14px !important;
  font-weight: 700 !important;
  border: 1px solid rgba(255,255,255,0.16) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# LANG STATE
# =========================
if "lang" not in st.session_state:
    st.session_state.lang = "中文"

# =========================
# TOP BAR (Logo + Lang Toggle + Quick Links)
# =========================
st.markdown('<div class="topbar">', unsafe_allow_html=True)
c1, c2, c3 = st.columns([1.4, 1.3, 1.3], vertical_alignment="center")

with c1:
    logo_file = Path(LOGO_PATH)
    if logo_file.exists():
        st.image(LOGO_PATH, width=88)
    st.markdown(
        "<div style='color:white; font-size:22px; font-weight:800; line-height:1.05;'>GFI Flow Intelligence</div>"
        "<div style='color:rgba(255,255,255,.85); font-size:13px; font-weight:600;'>量化摩擦 • 释放执行力 • 识别隐性损耗</div>",
        unsafe_allow_html=True,
    )

with c2:
    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    st.session_state.lang = st.radio(
        "",
        ["中文", "EN"],
        index=0 if st.session_state.lang == "中文" else 1,
        horizontal=True,
        label_visibility="collapsed",
    )

with c3:
    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns(3)
    with b1:
        st.link_button("中文版", CN_SITE_URL, use_container_width=True)
    with b2:
        st.link_button("English", EN_SITE_URL, use_container_width=True)
    with b3:
        st.link_button("快筛问卷", CN_FORM_URL, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# COPY BLOCKS (CN/EN)
# =========================
CN = {
    "hero_kicker": "结构诊断 / 立即出分 / 可升级为审计",
    "hero_title": "把“执行摩擦”变成可量化、可定价、可交付的结果。",
    "hero_sub": "GFI 不是咨询口号。它是一套可计算的“摩擦引擎”，用最少问题抓住组织损耗的结构性分母。",
    "cta_primary": "开始 8 题快筛（简体）",
    "cta_secondary": "机构合作入口",
    "cta_secondary_sub": "合作 / 联合交付 / 授权 / 白标",
    "sec1_title": "你正在失血，但你看不见。",
    "sec1_body": "当审批层级、流程回圈、跨部门对齐成本、隐性等待时间持续膨胀，组织资源不会“变慢”——而是直接蒸发。",
    "sec2_title": "GFI 的交付形态（模块化 / 可被 Big 4 销售）",
    "m1": ("模块 A：摩擦快筛（Lead Magnet）", "8 题 / 3 分钟 / 立即出分，用于筛选与建立基准。"),
    "m2": ("模块 B：结构映射（Workflow + Bottleneck）", "把“感觉很乱”变成可视化链路：节点、等待、返工、审批层级与失真点。"),
    "m3": ("模块 C：量化损耗模型（Capacity Loss）", "把摩擦转成金额与产能：吞吐量下降、工时损耗、延迟成本、风险外溢。"),
    "m4": ("模块 D：干预方案（低成本优先）", "按 ROI 排序的三条路径：减层、减回圈、减对齐成本（最小手术）。"),
    "sec3_title": "Big 4 合作定位（你卖“可复制的诊断部件”）",
    "sec3_body": "你不是在和 Big 4 竞争项目，你是在给他们“可加价的诊断模块”。他们需要：标准化、可复制、可审计、可承诺交付时间的产品化部件。",
    "sec4_title": "机构合作入口",
    "sec4_body": "如果你是：政府部门 / 国企央企 / 大型民企 / 咨询机构 / 内控审计团队 —— 你可以直接用 GFI 作为执行效率的量化入口。",
    "contact_line": f"合作邮箱：{CONTACT_EMAIL}",
    "footer": "© GFI Flow Intelligence | 结构摩擦诊断引擎",
}

EN = {
    "hero_kicker": "Structural Signal / Instant Score / Upgradeable Audit",
    "hero_title": "Turn execution friction into a quantifiable, sellable diagnostic asset.",
    "hero_sub": "GFI is not a slogan. It’s a calculation engine that captures denominator drift—approval layers, loopbacks, alignment cost, and latency.",
    "cta_primary": "Start 8-Question Snapshot (CN)",
    "cta_secondary": "Partnership Intake",
    "cta_secondary_sub": "Co-delivery / Licensing / White-label",
    "sec1_title": "You’re bleeding value—because friction is invisible on the balance sheet.",
    "sec1_body": "When layers, loopbacks, cross-team alignment cost, and waiting time inflate, resources don’t just slow down—they evaporate.",
    "sec2_title": "Delivery Modules (Big 4-Sellable Building Blocks)",
    "m1": ("Module A: Snapshot (Lead Magnet)", "8 questions / 3 minutes / instant score for baseline and qualification."),
    "m2": ("Module B: Structural Mapping", "Workflow + bottlenecks: nodes, waits, rework, approval depth, distortion points."),
    "m3": ("Module C: Quantified Capacity Loss", "Convert friction into dollars and throughput loss: time, delay cost, risk spillovers."),
    "m4": ("Module D: Intervention Playbook", "ROI-ranked moves: de-layer, de-loop, reduce alignment cost (minimum surgery)."),
    "sec3_title": "Big 4 Positioning (You sell a repeatable diagnostic component)",
    "sec3_body": "You don’t compete with Big 4 on projects. You give them a premium diagnostic module: standardized, repeatable, auditable, time-boxed.",
    "sec4_title": "Institutional Partnership Intake",
    "sec4_body": "If you are a government agency, SOE, enterprise, consulting firm, or internal audit team—use GFI as your execution performance entry point.",
    "contact_line": f"Email: {CONTACT_EMAIL}",
    "footer": "© GFI Flow Intelligence | Structural Friction Engine",
}

T = CN if st.session_state.lang == "中文" else EN

# =========================
# HERO
# =========================
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown(f"<div class='kicker'>{T['hero_kicker']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size:34px; font-weight:900; margin-top:6px;'>{T['hero_title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='muted' style='font-size:16px; margin-top:8px; line-height:1.6;'>{T['hero_sub']}</div>", unsafe_allow_html=True)

b1, b2 = st.columns([1, 1], vertical_alignment="center")
with b1:
    st.link_button(T["cta_primary"], CN_FORM_URL, use_container_width=True)
with b2:
    st.link_button(T["cta_secondary"], f"mailto:{CONTACT_EMAIL}?subject=GFI%20%E6%9C%BA%E6%9E%84%E5%90%88%E4%BD%9C%20%2F%20Partnership%20Intake", use_container_width=True)
st.markdown(f"<div class='small' style='margin-top:6px;'>{T['cta_secondary_sub']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: Core Claim
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"<h3>{T['sec1_title']}</h3>", unsafe_allow_html=True)
st.markdown(f"<div class='muted' style='line-height:1.7;'>{T['sec1_body']}</div>", unsafe_allow_html=True)

st.markdown("<div class='divline'></div>", unsafe_allow_html=True)

tags = ["Denominator", "Latency", "Approval Depth", "Loopback", "Alignment Cost"]
tag_html = " ".join([f"<span class='badge'>{x}</span>" for x in tags])
st.markdown(tag_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: Modules
# =========================
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"<h3>{T['sec2_title']}</h3>", unsafe_allow_html=True)

mcol1, mcol2 = st.columns(2)
with mcol1:
    st.markdown(f"**{T['m1'][0]}**  \n<div class='muted'>{T['m1'][1]}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divline'></div>", unsafe_allow_html=True)
    st.markdown(f"**{T['m2'][0]}**  \n<div class='muted'>{T['m2'][1]}</div>", unsafe_allow_html=True)
with mcol2:
    st.markdown(f"**{T['m3'][0]}**  \n<div class='muted'>{T['m3'][1]}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divline'></div>", unsafe_allow_html=True)
    st.markdown(f"**{T['m4'][0]}**  \n<div class='muted'>{T['m4'][1]}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: Big 4 Positioning
# =========================
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"<h3>{T['sec3_title']}</h3>", unsafe_allow_html=True)
st.markdown(f"<div class='muted' style='line-height:1.7;'>{T['sec3_body']}</div>", unsafe_allow_html=True)

st.markdown("<div class='divline'></div>", unsafe_allow_html=True)
if st.session_state.lang == "中文":
    bullets = [
        "对外口径：**“执行摩擦量化诊断”**（不是“流程优化建议”）",
        "交付形态：**可复制模块 + 可审计证据链**（Big 4 最爱）",
        "商业结构：**授权 / 联合交付 / 白标**（你拿分成或模块费）",
    ]
else:
    bullets = [
        "Messaging: **Execution-friction diagnostics** (not generic process advice)",
        "Deliverable: **repeatable module + auditable evidence trail**",
        "Commercial: **license / co-delivery / white-label** (module fee or rev share)",
    ]
for x in bullets:
    st.markdown(f"- {x}")
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SECTION: Partnership Intake
# =========================
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"<h3>{T['sec4_title']}</h3>", unsafe_allow_html=True)
st.markdown(f"<div class='muted' style='line-height:1.7;'>{T['sec4_body']}</div>", unsafe_allow_html=True)

p1, p2, p3 = st.columns([1, 1, 1])
with p1:
    st.link_button("📩 Email", f"mailto:{CONTACT_EMAIL}?subject=GFI%20%E6%9C%BA%E6%9E%84%E5%90%88%E4%BD%9C%20Intake", use_container_width=True)
with p2:
    st.link_button("🧾 快筛问卷", CN_FORM_URL, use_container_width=True)
with p3:
    st.link_button("🌐 中文站", CN_SITE_URL, use_container_width=True)

st.markdown(f"<div class='small' style='margin-top:8px;'>{T['contact_line']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
st.markdown(f"<div class='small' style='text-align:center;'>{T['footer']}</div>", unsafe_allow_html=True)
