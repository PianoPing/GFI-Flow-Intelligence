import streamlit as st

st.set_page_config(
    page_title="GFI Flow Intelligence",
    page_icon="🛡️",
    layout="wide"
)

st.title("GFI Flow Intelligence")
st.caption("Independent Diagnostic Reports · Confidential · Non-Political")

st.divider()

# --------------------
# Sidebar Navigation
# --------------------
language = st.sidebar.radio("Language / 語言", ["EN", "中文"], index=0)

if language == "EN":
    page = st.sidebar.radio(
        "Section",
        ["Overview", "Methodology", "Case Studies", "Founder", "Contact"],
        index=0
    )

    if page == "Overview":
        st.header("Overview")
        st.write("GFI measures institutional friction and execution delay—so leaders can see where capacity evaporates.")
        st.markdown("- Independent\n- Confidential\n- Non-political")

    elif page == "Methodology":
        st.header("Methodology")
        st.write("Core constructs: Friction · Delay/Latency · Throughput · Evaporation.")
        st.info("This is a non-technical summary. Full formulas can be provided in the diagnostic report.")

    elif page == "Case Studies":
        st.header("Case Studies")
        st.markdown(
            "- Backlog Spiral: delay → more appeals → more delay\n"
            "- Eligibility Maze: small mismatches → cascading denials\n"
            "- Verification Bottleneck: one queue stalls the entire pipeline"
        )

    elif page == "Founder":
        st.header("Founder")
        st.write("Ping Xu (徐萍)")
        st.markdown("- Governance / Operational Friction diagnostic designer\n- Decision-grade reports")

    elif page == "Contact":
        st.header("Contact")
        st.markdown(
            "- Email: **pingshyu0@gmail.com**\n"
            "- LinkedIn: **linkedin.com/in/ping-shyu/**"
        )

else:
    page = st.sidebar.radio(
        "章節",
        ["概覽", "方法論", "案例研究", "創辦人", "聯絡"],
        index=0
    )

    if page == "概覽":
        st.header("概覽")
        st.write("GFI（Governance Flow Index）用來量化制度執行的摩擦與延遲，找出吞吐量下降與資源蒸發的位置。")
        st.markdown("- 獨立\n- 保密\n- 非政治化")

    elif page == "方法論":
        st.header("方法論")
        st.write("核心概念：摩擦 · 延遲/滯後 · 吞吐量 · 蒸發。")
        st.info("此頁為非技術摘要；完整公式可在正式診斷報告中提供。")

    elif page == "案例研究":
        st.header("案例研究")
        st.markdown(
            "- 積壓螺旋：延遲增加 → 上訴增加 → 延遲更嚴重\n"
            "- 資格迷宮：小小不一致 → 連鎖拒件\n"
            "- 驗證瓶頸：單一隊列卡死整條管線"
        )

    elif page == "創辦人":
        st.header("創辦人")
        st.write("Ping Xu（徐萍）")
        st.markdown("- 治理/流程摩擦診斷設計\n- 產出決策級報告")

    elif page == "聯絡":
        st.header("聯絡")
        st.markdown(
            "- Email：**pingshyu0@gmail.com**\n"
            "- LinkedIn：**linkedin.com/in/ping-shyu/**"
        )

st.divider()
st.caption("© GFI Flow Intelligence")
