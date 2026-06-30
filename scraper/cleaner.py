"""
=========================================================
File : cleaner.py
Project : AgriAssist AI

Purpose
-------
Clean and standardize parsed scheme data
for LangChain and RAG.

Responsibilities
----------------
1. Standardize field names
2. Remove empty values
3. Create page_content
4. Create metadata

Author : Dhivyaa
=========================================================
"""

from __future__ import annotations


class DataCleaner:

    def __init__(self):

        self.field_mapping = {

            "Scheme Title/Name": "scheme_name",
            "Concerned Department": "department",
            "Concerned District": "district",
            "Organisation Name": "organisation",
            "Associated Scheme": "associated_scheme",
            "Sponsered By": "sponsored_by",
            "Funding Pattern": "funding_pattern",
            "Beneficiaries": "beneficiaries",
            "Types of Benefits": "benefit_type",
            "Income": "income",
            "Age From": "age_from",
            "Age To": "age_to",
            "Community": "community",
            "How To avail": "how_to_avail",
            "Introduced On": "introduced_on",
            "Description": "description",
            "Scheme Type": "scheme_type",
            "Uploaded File": "uploaded_file",
            "Source URL": "source_url"
        }

    # --------------------------------------------------

    def rename_fields(self, scheme: dict) -> dict:

        cleaned = {}

        for old_key, value in scheme.items():

            new_key = self.field_mapping.get(
                old_key,
                old_key.lower().replace(" ", "_")
            )

            cleaned[new_key] = value

        return cleaned

    # --------------------------------------------------

    def remove_empty_values(self, scheme: dict) -> dict:

        cleaned = {}

        for key, value in scheme.items():

            if value is None:
                continue

            value = str(value).strip()

            if value == "":
                continue

            cleaned[key] = value

        return cleaned

    # --------------------------------------------------

    def create_page_content(self, scheme: dict) -> str:

        lines = []

        preferred_order = [

            "scheme_name",
            "department",
            "organisation",
            "beneficiaries",
            "benefit_type",
            "funding_pattern",
            "description",
            "how_to_avail"
        ]

        # Add important fields first
        for key in preferred_order:

            if key in scheme:

                title = key.replace("_", " ").title()

                lines.append(f"{title}:")
                lines.append(scheme[key])
                lines.append("")

        # Add remaining fields
        for key, value in scheme.items():

            if key in preferred_order:
                continue

            title = key.replace("_", " ").title()

            lines.append(f"{title}:")
            lines.append(str(value))
            lines.append("")

        return "\n".join(lines)

    # --------------------------------------------------

    def create_metadata(self, scheme: dict) -> dict:

        return {

       "scheme_name": scheme.get("scheme_name", ""),
    "department": scheme.get("department", ""),
    "beneficiaries": scheme.get("beneficiaries", ""),
    "funding_pattern": scheme.get("funding_pattern", ""),
    "scheme_type": scheme.get("scheme_type", ""),
    "description": scheme.get("description", ""),
    "how_to_avail": scheme.get("how_to_avail", ""),
    "source_url": scheme.get("source_url", "")
        }

    # --------------------------------------------------

    def clean_scheme(self, scheme: dict) -> dict:

        scheme = self.rename_fields(scheme)

        scheme = self.remove_empty_values(scheme)

        scheme["page_content"] = self.create_page_content(
            scheme
        )

        scheme["metadata"] = self.create_metadata(
            scheme
        )

        return scheme

    # --------------------------------------------------

    def clean_dataset(self, dataset: list) -> list:

        cleaned = []

        for scheme in dataset:

            cleaned.append(

                self.clean_scheme(scheme)

            )

        return cleaned
