import json
import requests
from bs4 import BeautifulSoup
from time import sleep

from config import PROCESSED_DATA

BASE_URL = "https://www.tn.gov.in/"


class DetailScraper:

    def __init__(self):

        self.input_file = PROCESSED_DATA / "schemes.json"

        self.output_file = PROCESSED_DATA / "detailed_schemes.json"

    def load_schemes(self):

        with open(self.input_file, "r", encoding="utf-8") as f:

            return json.load(f)

    def fetch_page(self, url):

        response = requests.get(

            url,

            headers={
                "User-Agent":"Mozilla/5.0"
            },

            timeout=30
        )

        response.raise_for_status()

        return response.text

    def extract_text(self, soup):

        """
        Extract all visible text from detail page.
        """

        content = soup.get_text("\n", strip=True)

        return content

    def scrape(self):

        schemes = self.load_schemes()

        detailed = []

        total = len(schemes)

        for index, scheme in enumerate(schemes, start=1):

            print(f"[{index}/{total}] {scheme['scheme_name']}")

            try:

                html = self.fetch_page(scheme["scheme_url"])

                soup = BeautifulSoup(html,"lxml")

                text = self.extract_text(soup)

                scheme["page_text"] = text

                detailed.append(scheme)

            except Exception as e:

                print(e)

            sleep(1)

        return detailed

    def save(self,data):

        with open(self.output_file,"w",encoding="utf-8") as f:

            json.dump(data,f,indent=4,ensure_ascii=False)

        print("\nSaved")

        print(self.output_file)

    def run(self):

        data=self.scrape()

        self.save(data)


if __name__=="__main__":

    DetailScraper().run()