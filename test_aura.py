from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(username, password))

try:
    with driver.session() as session:
        result = session.run("RETURN 1 AS value")
        print(result.single()["value"])
    print("✅ Connected successfully")
except Exception as e:
    print(type(e).__name__)
    print(e)
finally:
    driver.close()