import streamlit as st
import pandas as pd

from dashboard import show_dashboard
from utils.log_parser import parse_logs
from agents.cve_agent import analyze_cve
from agents.rag_agent import process_document, ask_rag_question
from pypdf import PdfReader 
from utils.report_generator import generate_pdf_report

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
        "Security RAG Chatbot",
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
# CVE INTELLIGENCE PAGE
# =========================

elif page == "CVE Intelligence":

    st.title("🧠 CVE Intelligence System")

    st.markdown("""
Search and analyze cybersecurity vulnerabilities using AI-powered threat intelligence.
""")

    # =========================
    # CVE INPUT
    # =========================

    cve_id = st.text_input(
        "Enter CVE ID",
        placeholder="Example: CVE-2024-3094"
    )

    # =========================
    # ANALYZE BUTTON
    # =========================

    if st.button("Analyze CVE"):

        if cve_id.strip() == "":

            st.warning("Please enter a valid CVE ID.")

        else:

            with st.spinner("AI is analyzing CVE intelligence..."):

                cve_response = analyze_cve(cve_id)

                st.success("✅ CVE Analysis Completed")

                st.markdown(cve_response)

# =========================
# SECURITY RAG CHATBOT
# =========================

elif page == "Security RAG Chatbot":

    st.title("🧠 Security RAG Chatbot")

    st.markdown("""
Upload cybersecurity PDFs and ask AI security questions using RAG architecture.
""")

    # =========================
    # PDF UPLOAD
    # =========================

    uploaded_pdf = st.file_uploader(
        "Upload Cybersecurity PDF",
        type=["pdf"]
    )

    if uploaded_pdf is not None:

        try:

            pdf_reader = PdfReader(uploaded_pdf)

            extracted_text = ""

            for page_pdf in pdf_reader.pages:

                extracted_text += page_pdf.extract_text()

            st.success("✅ PDF Processed Successfully")

            # =========================
            # PROCESS DOCUMENT
            # =========================

            with st.spinner("Creating vector embeddings..."):

                process_document(extracted_text)

            st.success("✅ RAG Knowledge Base Created")

        except Exception as e:

            st.error(f"❌ PDF Processing Error: {str(e)}")

    # =========================
    # QUESTION INPUT
    # =========================

    question = st.text_input(
        "Ask Security Question",
        placeholder="Example: What are SQL injection attacks?"
    )

    if st.button("Ask AI"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("AI is searching cybersecurity knowledge base..."):

                answer = ask_rag_question(question)

                st.success("✅ AI Response Generated")

                st.markdown(answer)

# =========================
# INCIDENT REPORT PAGE
# =========================

# =========================
# INCIDENT REPORT PAGE
# =========================

elif page == "Incident Reports":

    st.title("📄 AI Incident Report Generator")

    st.markdown("""
Generate professional SOC incident reports and export them as PDF.
""")

    # =========================
    # INCIDENT INPUT
    # =========================

    incident_text = st.text_area(
        "Enter Security Incident Details",
        height=250,
        placeholder="Paste security incident details here..."
    )

    # =========================
    # GENERATE REPORT
    # =========================

    if st.button("Generate PDF Report"):

        if incident_text.strip() == "":

            st.warning("Please enter incident details.")

        else:

            try:

                # =========================
                # GENERATE PDF
                # =========================

                output_path = "incident_report.pdf"

                generate_pdf_report(
                    incident_text,
                    output_path
                )

                st.success("✅ PDF Report Generated Successfully")

                # =========================
                # DOWNLOAD BUTTON
                # =========================

                with open(output_path, "rb") as pdf_file:

                    st.download_button(
                        label="📥 Download Incident Report",
                        data=pdf_file,
                        file_name="SentinelAI_Incident_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(f"❌ PDF Generation Error: {str(e)}")