import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():

    st.title("🛡️ SentinelAI Security Dashboard")

    st.markdown("---")

    # =========================
    # TOP METRICS
    # =========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Critical Threats",
            value="12",
            delta="+3"
        )

    with col2:
        st.metric(
            label="Suspicious IPs",
            value="48",
            delta="+10"
        )

    with col3:
        st.metric(
            label="Logs Processed",
            value="15K",
            delta="+2K"
        )

    with col4:
        st.metric(
            label="Threat Score",
            value="87%",
            delta="-2%"
        )

    st.markdown("---")

    # =========================
    # THREAT CHART
    # =========================

    threat_data = pd.DataFrame({
        "Threat Type": [
            "Malware",
            "Phishing",
            "Brute Force",
            "SQL Injection",
            "DDoS"
        ],
        "Count": [35, 20, 45, 15, 28]
    })

    fig = px.bar(
        threat_data,
        x="Threat Type",
        y="Count",
        title="Detected Threat Categories"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # =========================
    # RECENT ALERTS TABLE
    # =========================

    alerts_data = pd.DataFrame({
        "Timestamp": [
            "10:15 AM",
            "10:30 AM",
            "11:00 AM",
            "11:20 AM"
        ],
        "Threat": [
            "Brute Force Attack",
            "Suspicious Login",
            "SQL Injection",
            "Malware Activity"
        ],
        "Severity": [
            "High",
            "Medium",
            "Critical",
            "High"
        ],
        "Status": [
            "Investigating",
            "Blocked",
            "Critical",
            "Resolved"
        ]
    })

    st.subheader("🚨 Recent Security Alerts")

    st.dataframe(
        alerts_data,
        use_container_width=True
    )