import streamlit as st

st.title("Case Studies")
st.subheader("Common friction patterns the scan detects")

st.divider()

st.markdown("## Patterns")
st.markdown("""
- **Approval bottleneck:** one gate accumulates the queue  
- **Rework loop:** repeated corrections due to unclear rules  
- **Handoff loss:** information resets across teams  
- **Latency drift:** small delays compound into systemic slowdown  
""")

st.markdown("## What the signal report highlights")
st.markdown("""
- where friction concentrates
- where delays accumulate
- where overload becomes structural
""")
