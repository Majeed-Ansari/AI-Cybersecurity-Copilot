import streamlit as st
from dashboard import show_dashboard
from utils.log_parser import parse_logs
import pandas as pd

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

    st.title("🔍 Threat Analysis System")

    uploaded_file = st.file_uploader(
        "Upload Log File",
        type=["log", "txt"]
    )

    if uploaded_file is not None:

        log_text = uploaded_file.read().decode("utf-8")

        st.subheader("📄 Raw Logs")

        st.text_area(
            "Log Content",
            log_text,
            height=200
        )

        # =========================
        # PARSE LOGS
        # =========================

        parsed_df = parse_logs(log_text)

        st.subheader("🛡️ Parsed Security Events")

        st.dataframe(
            parsed_df,
            use_container_width=True
        )

        # =========================
        # THREAT COUNTS
        # =========================

        st.subheader("📊 Threat Summary")

        threat_counts = parsed_df["Threat Type"].value_counts()

        st.bar_chart(threat_counts)

        # =========================
        # SUSPICIOUS IPS
        # =========================

        suspicious_ips = parsed_df[
            parsed_df["Threat Type"] != "Normal Activity"
        ]["IP Address"].value_counts()

        st.subheader("🚨 Suspicious IP Activity")

        st.dataframe(
            suspicious_ips.reset_index(),
            use_container_width=True
        )

elif page == "CVE Intelligence":
    st.title("🧠 CVE Intelligence")
    st.info("CVE intelligence module coming soon...")

elif page == "Incident Reports":
    st.title("📄 Incident Reports")
    st.info("Incident report module coming soon...")