import pandas as pd

from backend.neo4j_client import neo4j_client


def build_feature_dataset():

    query = """
    MATCH (a:Account)

    OPTIONAL MATCH (a)-[t:TRANSFER]->()

    WITH
        a,
        count(t) AS tx_count,
        sum(t.amount) AS total_sent,
        max(t.isFraud) AS fraud

    RETURN
        a.account_id AS account_id,
        coalesce(a.pagerank,0) AS pagerank,
        coalesce(a.degree,0) AS degree,
        coalesce(a.betweenness,0) AS betweenness,
        coalesce(a.community,-1) AS community,
        coalesce(tx_count,0) AS tx_count,
        coalesce(total_sent,0) AS total_sent,
        coalesce(fraud,0) AS label
    """

    result = neo4j_client.execute(query)

    rows = [dict(r) for r in result]

    return pd.DataFrame(rows)


if __name__ == "__main__":

    df = build_feature_dataset()

    df.to_csv(
        "datasets/account_features.csv",
        index=False
    )

    print(df.head())
