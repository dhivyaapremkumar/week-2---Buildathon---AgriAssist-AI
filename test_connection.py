from graph.neo4j_config import neo4j_db

query = "RETURN 1 AS value"

try:
    result = neo4j_db.query(query)
    print(result)
    print("✅ AuraDB Connected Successfully")
except Exception as e:
    print(type(e).__name__)
    print(e)