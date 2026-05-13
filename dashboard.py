import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time

# =========================
# DASHBOARD
# =========================

def show_dashboard():

    st.title("🛡️ SentinelAI Security Operations Center")

    st.markdown("""
Real-time AI-powered cybersecurity monitoring dashboard.
""")

    st.markdown("---")

    # =========================
    # METRICS
    # =========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Critical Threats",
            random.randint(5, 20),
            "+2"
        )

    with col2:

        st.metric(
            "Suspicious IPs",
            random.randint(20, 80),
            "+5"
        )

    with col3:

        st.metric(
            "Logs Processed",
            f"{random.randint(10,50)}K",
            "+3K"
        )

    with col4:

        st.metric(
            "Threat Score",
            f"{random.randint(70,95)}%",
            "-1%"
        )

    st.markdown("---")

    # =========================
    # CHARTS
    # =========================

    colA, colB = st.columns(2)

    # =========================
    # BAR CHART
    # =========================

    with colA:

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

        fig_bar = px.bar(
            threat_data,
            x="Threat Type",
            y="Count",
            title="Threat Categories"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

    # =========================
    # PIE CHART
    # =========================

    with colB:

        severity_data = pd.DataFrame({
            "Severity": [
                "Critical",
                "High",
                "Medium",
                "Low"
            ],
            "Count": [15, 30, 25, 10]
        })

        fig_pie = px.pie(
            severity_data,
            names="Severity",
            values="Count",
            title="Threat Severity Distribution"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

    st.markdown("---")

    # =========================
    # LIVE ATTACK FEED
    # =========================

    st.subheader("🚨 Live Threat Feed")

    live_feed = pd.DataFrame({
        "Time": [
            "10:15 AM",
            "10:18 AM",
            "10:22 AM",
            "10:30 AM",
            "10:35 AM"
        ],
        "Attack Type": [
            "SQL Injection",
            "Malware",
            "Brute Force",
            "Phishing",
            "DDoS"
        ],
        "Severity": [
            "Critical",
            "High",
            "High",
            "Medium",
            "Critical"
        ],
        "Status": [
            "Blocked",
            "Investigating",
            "Mitigated",
            "Monitoring",
            "Blocked"
        ]
    })

    st.dataframe(
        live_feed,
        use_container_width=True
    )

    st.markdown("---")

    # =========================
    # REAL-TIME STATUS
    # =========================

    st.subheader("🟢 System Status")

    status_placeholder = st.empty()

    statuses = [
        "Monitoring network traffic...",
        "Scanning suspicious IP activity...",
        "Analyzing malware signatures...",
        "Detecting brute force attacks...",
        "AI agents operational..."
    ]

    for status in statuses:

        status_placeholder.info(status)

        time.sleep(0.5)