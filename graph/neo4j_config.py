import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"),
        os.getenv("NEO4J_PASSWORD"),
    ),
)


class Neo4jDB:
    def __init__(self):
        self.driver = driver

    def query(self, cypher_query, parameters=None):
        with self.driver.session(
            database=os.getenv("NEO4J_DATABASE")
        ) as session:
            result = session.run(cypher_query, parameters or {})
            return [record.data() for record in result]

    def close(self):
        self.driver.close()


neo4j_db = Neo4jDB()