import os
from datetime import datetime

import streamlit as st
from fpdf import FPDF

# =========================
# App Config
# =========================
st.set_page_config(
    page_title="GL Framework v2.1",
    page_icon="📈",
    layout="centered",
)

APP_TITLE = "治理物理學診斷引擎 v2.1（GL Framework）"
FORMULA_TEXT = "GL = (Fs × Vn) / (Pd × Cf)"
FONT_PATH = os.path.join("assets", "fonts", "NotoSansCJKtc-Regular.otf")


# =========================
# GL Core (MVP)
# =========================
def compute_gl(fs: float, vn: float, pd: float, cf: float) -> float:
    """MVP formula: GL = (Fs * Vn) / (Pd * Cf)"""
    eps = 1e-9
    pd = max(pd, eps)
    cf = max(cf, eps)
    return (fs * vn) / (pd * cf)


def interpret_gl(gl: float) -> str:
    """Simple bands (tune later)."""
    if gl < 1:
        return "GL < 1：摩擦過高／流程對使用者不友善（合法性脆弱）"
    if gl < 3:
        return "1 ≤ GL < 3：可運作但摩擦偏高（建議優化）"
    return "GL ≥ 3：流動良好／摩擦較可控（相對健康）"


def _row_pack(name, base_gl, base_value, better_value, better_gl, worse_value, worse_gl):
    def pct_delta(x):
        return (x / base_gl - 1) * 100 if base_gl > 0 else 0.0

    return {
        "變數": name,
        "基準值": base_value,
        "改善值（±30%）": better_value,
        "GL（改善）": round(better_gl, 6),
        "改善幅度%": round(pct_delta(better_gl), 2),
        "惡化值（±30%）": worse_value,
        "GL（惡化）": round(worse_gl, 6),
        "惡化幅度%": round(p
