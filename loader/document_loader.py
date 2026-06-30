import requests
from pathlib import Path
from config import RAW_DATA, URL


class DocumentLoader:

    def __init__(self):
        self.url = URL

    def fetch_page(self):
        """Download webpage HTML."""
        print("Downloading webpage...")

        response = requests.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.text

    def save_html(self, html):
        """Save HTML to local file."""

        file_path = RAW_DATA / "agriculture_schemes.html"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html)

        print(f"Saved HTML to: {file_path}")

    def run(self):
        html = self.fetch_page()
        self.save_html(html)
        print("Document Loader completed successfully.")


if __name__ == "__main__":
    loader = DocumentLoader()
    loader.run()