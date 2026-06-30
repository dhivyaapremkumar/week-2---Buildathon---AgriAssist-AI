import json
from neo4j import GraphDatabase

from config import (
    PROCESSED_DATA,
    NEO4J_URI,
    NEO4J_USER,
    NEO4J_PASSWORD
)


class Neo4jLoader:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

        self.graph_file = PROCESSED_DATA / "graph.json"

    def load_graph(self):

        with open(self.graph_file, "r", encoding="utf8") as f:

            return json.load(f)

    def clear_database(self):

        with self.driver.session() as session:

            session.run("MATCH (n) DETACH DELETE n")

        print("Database cleared.")

    def create_nodes(self, session, nodes):

        for node in nodes:

            query = f"""
            MERGE (n:{node['label']} {{name:$name}})
            """

            session.run(query, name=node["id"])

    def create_relationships(self, session, relationships):

        for rel in relationships:

            query = f"""
            MATCH (a {{name:$source}})
            MATCH (b {{name:$target}})
            MERGE (a)-[:{rel['type']}]->(b)
            """

            session.run(
                query,
                source=rel["source"],
                target=rel["target"]
            )

    def upload(self):

        graph = self.load_graph()

        with self.driver.session() as session:

            self.clear_database()

            self.create_nodes(
                session,
                graph["nodes"]
            )

            self.create_relationships(
                session,
                graph["relationships"]
            )

        print("Graph uploaded successfully.")

    def close(self):

        self.driver.close()


if __name__ == "__main__":

    loader = Neo4jLoader()

    loader.upload()

    loader.close()