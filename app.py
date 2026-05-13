import streamlit as st
import pandas as pd

from dashboard import show_dashboard
from utils.log_parser import parse_logs

from agents.threat_agent import analyze_threats
from agents.mitigation_agent import generate_mitigation
from agents.incident_agent import generate_incident_report

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

            # =========================
            # READ LOG FILE
            # =========================

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

            # =========================
            # PARSED EVENTS
            # =========================

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
            # MULTI-AGENT AI ANALYSIS
            # =========================

            st.subheader("🤖 Multi-Agent AI Security Analysis")

            if st.button("Run AI Security Agents"):

                with st.spinner("AI agents are analyzing security threats..."):

                    # =========================
                    # THREAT AGENT
                    # =========================

                    st.subheader("🧠 Threat Detection Agent")

                    threat_response = analyze_threats(log_text)

                    st.markdown(threat_response)

                    st.markdown("---")

                    # =========================
                    # MITIGATION AGENT
                    # =========================

                    st.subheader("🛡️ Mitigation Agent")

                    mitigation_response = generate_mitigation(log_text)

                    st.markdown(mitigation_response)

                    st.markdown("---")

                    # =========================
                    # INCIDENT REPORT AGENT
                    # =========================

                    st.subheader("📄 Incident Report Agent")

                    incident_response = generate_incident_report(log_text)

                    st.markdown(incident_response)

                    st.success("✅ Multi-Agent Security Analysis Completed")

        except Exception as e:

            st.error(f"❌ Error processing log file: {str(e)}")

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