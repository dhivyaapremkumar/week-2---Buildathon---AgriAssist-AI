"""
=========================================================
File : save_json.py
Project : AgriAssist AI

Purpose
-------
Generate the final Knowledge Base (schemes.json)

Workflow
--------
Website
    ↓
Parser
    ↓
Cleaner
    ↓
JSON

Author : Dhivyaa
=========================================================
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime

from parser import SchemeParser
from cleaner import DataCleaner


class KnowledgeBaseBuilder:

    def __init__(self):

        self.parser = SchemeParser()

        self.cleaner = DataCleaner()

        # Root Project Folder
        self.project_root = Path(__file__).resolve().parent.parent

        # data/
        self.data_folder = self.project_root / "data"

        # Create data folder automatically
        self.data_folder.mkdir(
            exist_ok=True
        )

        self.output_file = self.data_folder / "schemes.json"

    # -----------------------------------------------------

    def build(self):

        print("\n" + "=" * 70)
        print("AgriAssist AI Knowledge Base Builder")
        print("=" * 70)

        # Step 1
        print("\nStep 1 : Crawling website...")

        raw_dataset = self.parser.build_dataset()

        print(f"Collected {len(raw_dataset)} schemes")

        # Step 2
        print("\nStep 2 : Cleaning data...")

        cleaned_dataset = self.cleaner.clean_dataset(
            raw_dataset
        )

        print(f"Cleaned {len(cleaned_dataset)} schemes")

        # Step 3
        print("\nStep 3 : Saving JSON...")

        with open(
            self.output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                cleaned_dataset,
                f,
                indent=4,
                ensure_ascii=False
            )

        print("\nKnowledge Base Saved Successfully")

        print(self.output_file)

        return cleaned_dataset

    # -----------------------------------------------------

    def statistics(self):

        if not self.output_file.exists():

            print("Knowledge Base not found.")

            return

        with open(
            self.output_file,
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        print("\n" + "=" * 70)

        print("Knowledge Base Statistics")

        print("=" * 70)

        print(f"Total Schemes : {len(data)}")

        departments = {

            item.get("department", "")

            for item in data
        }

        print(f"Departments : {len(departments)}")

        print(
            "Generated On :",
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        )

        print("=" * 70)


# ----------------------------------------------------------

if __name__ == "__main__":

    builder = KnowledgeBaseBuilder()

    builder.build()

    builder.statistics()