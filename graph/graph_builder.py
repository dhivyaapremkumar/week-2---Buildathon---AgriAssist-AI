import json

from config import PROCESSED_DATA


class GraphBuilder:

    def __init__(self):

        self.input = PROCESSED_DATA / "structured_schemes.json"
        self.output = PROCESSED_DATA / "graph.json"

    def load(self):

        with open(self.input, encoding="utf8") as f:
            return json.load(f)

    def add_node(self, nodes, node_id, label):

        if node_id and node_id.strip():

            nodes.add((node_id.strip(), label))

    def build(self):

        schemes = self.load()

        nodes = set()
        relationships = []

        for s in schemes:

            scheme = s["scheme_name"]

            self.add_node(nodes, scheme, "Scheme")
            self.add_node(nodes, s["department"], "Department")
            self.add_node(nodes, s["beneficiaries"], "Beneficiary")
            self.add_node(nodes, s["benefit_type"], "Benefit")
            self.add_node(nodes, s["sponsored_by"], "Sponsor")

            relationships.extend([

                {
                    "source": scheme,
                    "target": s["department"],
                    "type": "ADMINISTERED_BY"
                },

                {
                    "source": scheme,
                    "target": s["beneficiaries"],
                    "type": "BENEFITS"
                },

                {
                    "source": scheme,
                    "target": s["benefit_type"],
                    "type": "OFFERS"
                },

                {
                    "source": scheme,
                    "target": s["sponsored_by"],
                    "type": "FUNDED_BY"
                }

            ])

        graph = {

            "nodes": [

                {
                    "id": node,
                    "label": label
                }

                for node, label in sorted(nodes)

            ],

            "relationships": relationships

        }

        with open(self.output, "w", encoding="utf8") as f:

            json.dump(graph, f, indent=4, ensure_ascii=False)

        print(f"Nodes : {len(graph['nodes'])}")
        print(f"Relationships : {len(graph['relationships'])}")
        print("Saved graph.json")


if __name__ == "__main__":

    GraphBuilder().build()