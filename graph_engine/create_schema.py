from backend.neo4j_client import neo4j_client


def create_schema():

    query = """
    CREATE CONSTRAINT account_id_unique IF NOT EXISTS
    FOR (a:Account)
    REQUIRE a.account_id IS UNIQUE
    """

    neo4j_client.execute(query)

    print("Schema created")


if __name__ == "__main__":
    create_schema()
