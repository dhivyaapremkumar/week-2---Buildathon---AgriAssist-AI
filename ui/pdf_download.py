"""
=========================================
File : pdf_download.py
Purpose : Generate PDF Reports
=========================================
"""

from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_pdf(title: str, content: dict):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # -------------------------
    # Title
    # -------------------------

    story.append(
        Paragraph(
            "<b>🌾 AgriAssist AI</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "Tamil Nadu Agricultural Scheme Assistant",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>{title}</b>",
            styles["Heading1"]
        )
    )

    story.append(Spacer(1, 15))

    # -------------------------
    # Fields
    # -------------------------

    for key, value in content.items():

        story.append(

            Paragraph(

                f"<b>{key}</b>",

                styles["Heading3"]

            )

        )

        story.append(

            Paragraph(

                str(value),

                styles["BodyText"]

            )

        )

        story.append(

            Spacer(1, 10)

        )

    # -------------------------
    # Footer
    # -------------------------

    story.append(Spacer(1, 20))

    story.append(

        Paragraph(

            f"Generated on : {datetime.now().strftime('%d-%m-%Y %H:%M')}",

            styles["Italic"]

        )

    )

    doc.build(story)

    buffer.seek(0)

    return buffer