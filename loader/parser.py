from bs4 import BeautifulSoup
import json

from config import RAW_DATA, PROCESSED_DATA


class SchemeParser:

    def __init__(self):
        self.input_file = RAW_DATA / "agriculture_schemes.html"
        self.output_file = PROCESSED_DATA / "schemes.json"

    def load_html(self):

        with open(self.input_file, "r", encoding="utf-8") as f:
            return f.read()

    def parse(self):

        html = self.load_html()

        soup = BeautifulSoup(html, "lxml")

        department = soup.find(id="content1").get_text(strip=True)

        scheme_list = soup.find("ul", id="content")

        schemes = []

        for i, li in enumerate(scheme_list.find_all("li"), start=1):

            a = li.find("a")

            if not a:
                continue

            schemes.append(
                {
                    "id": i,
                    "department": department,
                    "scheme_name": a.get_text(strip=True),
                    "scheme_url": "https://www.tn.gov.in/" + a["href"]
                }
            )

        return schemes

    def save(self, schemes):

        with open(self.output_file, "w", encoding="utf-8") as f:

            json.dump(
                schemes,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"\nSaved {len(schemes)} schemes")

        print(self.output_file)

    def run(self):

        schemes = self.parse()

        self.save(schemes)


if __name__ == "__main__":

    parser = SchemeParser()

    parser.run()