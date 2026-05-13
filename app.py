import streamlit as st
import pandas as pd

from dashboard import show_dashboard
from utils.log_parser import parse_logs
from agents.threat_agent import analyze_threats

# =========================
# PAGE CONFIG
# =========================

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
# DASHBOARD PAGE
# =========================

if page == "Dashboard":

    show_dashboard()

# =========================
# THREAT ANALYSIS PAGE
# =========================

elif page == "Threat Analysis":

    st.title("🔍 Threat Analysis System")

    uploaded_file = st.file_uploader(
        "Upload Log File",
        type=["log", "txt"]
    )

    if uploaded_file is not None:

        try:

            # Read uploaded log file
            log_text = uploaded_file.read().decode("utf-8")

            # =========================
            # RAW LOGS
            # =========================

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
            # THREAT SUMMARY
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

            # =========================
            # AI THREAT ANALYSIS
            # =========================

            st.subheader("🧠 AI Threat Intelligence")

            if st.button("Analyze Threats with AI"):

                with st.spinner("AI is analyzing security threats..."):

                    ai_response = analyze_threats(log_text)

                    st.success("AI Analysis Complete")

                    st.markdown(ai_response)

        except Exception as e:

            st.error(f"Error processing log file: {str(e)}")

# =========================
# CVE PAGE
# =========================

elif page == "CVE Intelligence":

    st.title("🧠 CVE Intelligence")

    st.info("CVE intelligence module coming soon...")

# =========================
# INCIDENT REPORT PAGE
# =========================

elif page == "Incident Reports":

    st.title("📄 Incident Reports")

    st.info("Incident report module coming soon...")