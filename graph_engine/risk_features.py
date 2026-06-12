from backend.neo4j_client import neo4j_client


def build_risk_features():

    query = """
    MATCH (a:Account)

    OPTIONAL MATCH (a)-[t:TRANSFER]->()

    WITH
        a,
        count(t) AS tx_count,
        sum(t.amount) AS total_sent

    SET
        a.tx_count = tx_count,
        a.total_sent = coalesce(total_sent,0)
    """

    neo4j_client.execute(query)

    print("Risk Features Generated")


if __name__ == "__main__":
    build_risk_features()
