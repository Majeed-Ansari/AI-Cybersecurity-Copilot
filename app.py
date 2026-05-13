import streamlit as st
from dashboard import show_dashboard

st.set_page_config(
    page_title="SentinelAI",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🛡️ SentinelAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Threat Analysis",
        "CVE Intelligence",
        "Incident Reports"
    ]
)

# =========================
# PAGE ROUTING
# =========================

if page == "Dashboard":
    show_dashboard()

elif page == "Threat Analysis":
    st.title("🔍 Threat Analysis")
    st.info("Threat analysis module coming soon...")

elif page == "CVE Intelligence":
    st.title("🧠 CVE Intelligence")
    st.info("CVE intelligence module coming soon...")

elif page == "Incident Reports":
    st.title("📄 Incident Reports")
    st.info("Incident report module coming soon...")