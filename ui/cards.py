"""
=========================================
File : cards.py
Purpose : Display Scheme Details
=========================================
"""

import streamlit as st
from ui.pdf_download import generate_pdf


def show_scheme_card(selected_scheme, schemes):

    if selected_scheme == "Select a Scheme":
        return

    scheme = next(
        (
            s for s in schemes
            if s["metadata"]["scheme_name"] == selected_scheme
        ),
        None
    )

    if not scheme:
        st.warning("Scheme not found.")
        return

    meta = scheme["metadata"]

    # -----------------------------
    # Display Scheme Card
    # -----------------------------

    st.markdown(
        f"""
<div class="card">

<h2 style="color:#2E7D32;">
🌾 {meta.get("scheme_name","")}
</h2>

<hr>

<b>🏛 Department</b>
<p>{meta.get("department","-")}</p>

<b>👨 Beneficiaries</b>
<p>{meta.get("beneficiaries","-")}</p>

<b>💰 Funding Pattern</b>
<p>{meta.get("funding_pattern","-")}</p>

<b>📌 Scheme Type</b>
<p>{meta.get("scheme_type","-")}</p>

<b>📝 Description</b>
<p>{meta.get("description","-")}</p>

<b>🛣 How to Apply</b>
<p>{meta.get("how_to_avail","-")}</p>

<b>🔗 Official Source</b>

<p>
<a href="{meta.get('source_url','#')}" target="_blank">
{meta.get("source_url","-")}
</a>
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    # -----------------------------
    # Generate PDF
    # -----------------------------

    pdf = generate_pdf(
        meta.get("scheme_name", "Scheme"),
        {
            "Department": meta.get("department", "-"),
            "Beneficiaries": meta.get("beneficiaries", "-"),
            "Funding Pattern": meta.get("funding_pattern", "-"),
            "Scheme Type": meta.get("scheme_type", "-"),
            "Description": meta.get("description", "-"),
            "How to Apply": meta.get("how_to_avail", "-"),
            "Source": meta.get("source_url", "-"),
        },
    )

    # -----------------------------
    # Download Button
    # -----------------------------

    st.download_button(
        label="📄 Download Scheme PDF",
        data=pdf,
        file_name=f"{meta.get('scheme_name','scheme')}.pdf",
        mime="application/pdf",
    )