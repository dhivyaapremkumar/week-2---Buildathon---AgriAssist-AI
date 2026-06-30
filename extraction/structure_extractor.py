import json
import re

from config import PROCESSED_DATA


class StructureExtractor:

    def __init__(self):

        self.input_file = PROCESSED_DATA / "detailed_schemes.json"

        self.output_file = PROCESSED_DATA / "structured_schemes.json"

    def load(self):

        with open(self.input_file,"r",encoding="utf-8") as f:

            return json.load(f)

    def extract_field(self,text,start,end=None):

        try:

            pattern = re.escape(start)

            if end:

                pattern += r"(.*?)" + re.escape(end)

            else:

                pattern += r"(.*)"

            match = re.search(pattern,text,re.S)

            if match:

                return match.group(1).strip()

        except:
            pass

        return ""

    def process(self):

        data = self.load()

        output=[]

        for scheme in data:

            text=scheme["page_text"]

            item={

                "id":scheme["id"],

                "scheme_name":scheme["scheme_name"],

                "department":scheme["department"],

                "scheme_url":scheme["scheme_url"],

                "sponsored_by":
                    self.extract_field(
                        text,
                        "Sponsered By:",
                        "Funding Pattern:"
                    ),

                "funding_pattern":
                    self.extract_field(
                        text,
                        "Funding Pattern:",
                        "Beneficiaries:"
                    ),

                "beneficiaries":
                    self.extract_field(
                        text,
                        "Beneficiaries:",
                        "Types of Benefits:"
                    ),

                "benefit_type":
                    self.extract_field(
                        text,
                        "Types of Benefits:",
                        "Eligibility criteria:"
                    ),

                "eligibility":
                    self.extract_field(
                        text,
                        "Eligibility criteria:",
                        "How To avail:"
                    ),

                "application_process":
                    self.extract_field(
                        text,
                        "How To avail:",
                        "Validity of the Scheme:"
                    ),

                "description":
                    self.extract_field(
                        text,
                        "Description:",
                        "Scheme Type:"
                    )

            }

            output.append(item)

        return output

    def save(self,data):

        with open(self.output_file,"w",encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"\nSaved {len(data)} schemes")

    def run(self):

        data=self.process()

        self.save(data)


if __name__=="__main__":

    StructureExtractor().run()