from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

# =========================
# GENERATE PDF REPORT
# =========================

def generate_pdf_report(content, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    story = []

    # =========================
    # TITLE
    # =========================

    title = Paragraph(
        "SentinelAI Security Incident Report",
        styles['Title']
    )

    story.append(title)

    story.append(Spacer(1, 20))

    # =========================
    # REPORT CONTENT
    # =========================

    paragraphs = content.split("\n")

    for para in paragraphs:

        if para.strip() != "":

            p = Paragraph(
                para,
                styles['BodyText']
            )

            story.append(p)

            story.append(Spacer(1, 10))

    # =========================
    # BUILD PDF
    # =========================

    doc.build(story)