"""
==========================================================
File: scraper.py
Project: AgriAssist AI
Author: Dhivyaa

Purpose
-------
This module is responsible ONLY for downloading web pages.

Responsibilities:
✔ Create HTTP session
✔ Retry failed requests
✔ Set browser headers
✔ Download HTML
✔ Convert HTML to BeautifulSoup object

It DOES NOT:
✘ Parse schemes
✘ Extract data
✘ Save JSON

This follows the Single Responsibility Principle (SRP).
==========================================================
"""

from __future__ import annotations

import logging
import time
from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ==========================================================
# Logging
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================================
# Constants
# ==========================================================

BASE_URL = "https://www.tn.gov.in"

SCHEME_LIST_URL = (
    "https://www.tn.gov.in/scheme_list.php?dep_id=Mg=="
)

REQUEST_TIMEOUT = 30


# ==========================================================
# Scraper Class
# ==========================================================

class WebScraper:
    """
    Downloads webpages and returns BeautifulSoup objects.
    """

    def __init__(self):

        self.session = requests.Session()

        retry_strategy = Retry(
            total=5,
            connect=5,
            read=5,
            backoff_factor=1,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504
            ],
            allowed_methods=["GET"]
        )

        adapter = HTTPAdapter(
            max_retries=retry_strategy
        )

        self.session.mount(
            "http://",
            adapter
        )

        self.session.mount(
            "https://",
            adapter
        )

        self.session.headers.update(
            {
                "User-Agent":
                    (
                        "Mozilla/5.0 "
                        "(Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 "
                        "(KHTML, like Gecko) "
                        "Chrome/137.0 Safari/537.36"
                    )
            }
        )

    # ======================================================
    # Download HTML
    # ======================================================

    def fetch(self, url: str) -> Optional[str]:
        """
        Download page HTML.

        Parameters
        ----------
        url : str

        Returns
        -------
        HTML string
        """

        try:

            logger.info(f"Downloading : {url}")

            response = self.session.get(
                url,
                timeout=REQUEST_TIMEOUT
            )

            response.raise_for_status()

            logger.info(
                "Download successful."
            )

            return response.text

        except Exception as e:

            logger.error(
                f"Failed downloading {url}"
            )

            logger.error(e)

            return None

    # ======================================================
    # Convert HTML -> BeautifulSoup
    # ======================================================

    def get_soup(
        self,
        url: str
    ) -> Optional[BeautifulSoup]:

        html = self.fetch(url)

        if html is None:
            return None

        return BeautifulSoup(
            html,
            "lxml"
        )

    # ======================================================
    # Check URL
    # ======================================================

    def url_exists(
        self,
        url: str
    ) -> bool:

        try:

            response = self.session.head(
                url,
                allow_redirects=True,
                timeout=10
            )

            return response.status_code == 200

        except Exception:

            return False

    # ======================================================
    # Delay (polite crawling)
    # ======================================================

    @staticmethod
    def wait(seconds: float = 1.0):

        time.sleep(seconds)


# ==========================================================
# Singleton
# ==========================================================

scraper = WebScraper()


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    soup = scraper.get_soup(
        SCHEME_LIST_URL
    )

    if soup:

        print("=" * 70)

        print("Title")

        print(soup.title.text)

        print("=" * 70)

        print("Downloaded Successfully")

    else:

        print("Download Failed")