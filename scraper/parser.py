"""
=========================================================
File : parser.py
Project : AgriAssist AI

Purpose
-------
Extract all Agriculture Scheme information from
https://www.tn.gov.in

Responsibilities
----------------
1. Read Scheme List Page
2. Collect Scheme URLs
3. Visit every Scheme
4. Extract all details
5. Return structured dictionaries

Author : Dhivyaa
=========================================================
"""

from __future__ import annotations

from urllib.parse import urljoin, urlparse, parse_qs

from scraper import scraper, BASE_URL, SCHEME_LIST_URL


class SchemeParser:

    def __init__(self):

        self.scheme_links = []

    # --------------------------------------------------

    def get_scheme_links(self):

        """
        Extract all Scheme URLs from list page
        """

        soup = scraper.get_soup(SCHEME_LIST_URL)

        if soup is None:
            return []

        content = soup.find("ul", id="content")

        if content is None:
            return []

        links = []

        for tag in content.find_all("a", href=True):

            href = tag["href"]

            name = tag.get_text(strip=True)

            full_url = urljoin(BASE_URL + "/", href)

            links.append(
                {
                    "scheme_name": name,
                    "url": full_url
                }
            )

        return links

    # --------------------------------------------------

    def parse_detail_page(self, url):

        """
        Extract every field from one scheme page
        """

        soup = scraper.get_soup(url)

        if soup is None:
            return None

        table = soup.find(
            "table",
            class_="table"
        )

        if table is None:
            return None

        scheme = {}

        rows = table.find_all("tr")

        for row in rows:

            columns = row.find_all("td")

            if len(columns) != 2:
                continue

            key = (
                columns[0]
                .get_text(" ", strip=True)
                .replace(":", "")
            )

            value = columns[1].get_text(
                " ",
                strip=True
            )

            scheme[key] = value

        scheme["Source URL"] = url

        return scheme

    # --------------------------------------------------

    def build_dataset(self):

        """
        Visit every Scheme Page
        """

        print("\nCollecting Scheme Links...")

        links = self.get_scheme_links()

        print(f"{len(links)} schemes found.\n")

        dataset = []

        for index, scheme in enumerate(links, start=1):

            print(
                f"[{index}/{len(links)}] "
                f"{scheme['scheme_name']}"
            )

            details = self.parse_detail_page(
                scheme["url"]
            )

            if details:

                dataset.append(details)

            scraper.wait(0.5)

        return dataset


# ----------------------------------------------------------

if __name__ == "__main__":

    parser = SchemeParser()

    data = parser.build_dataset()

    print()

    print("=" * 60)

    print("Total Schemes")

    print(len(data))

    print("=" * 60)