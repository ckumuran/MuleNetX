import pandas as pd
from tqdm import tqdm

from backend.neo4j_client import neo4j_client


BATCH_SIZE = 5000


def create_batch(records):

    query = """
    UNWIND $rows AS row

    MERGE (sender:Account {
        account_id: row.nameOrig
    })

    MERGE (receiver:Account {
        account_id: row.nameDest
    })

    CREATE (sender)-[:TRANSFER {
        amount: row.amount,
        transaction_type: row.type,
        step: row.step,
        isFraud: row.isFraud,
        isFlaggedFraud: row.isFlaggedFraud
    }]->(receiver)
    """

    neo4j_client.execute(query, {"rows": records})


def ingest(df):

    total_rows = len(df)

    for start in tqdm(
        range(0, total_rows, BATCH_SIZE)
    ):

        end = start + BATCH_SIZE

        batch = df.iloc[start:end]

        create_batch(
            batch.to_dict("records")
        )


if __name__ == "__main__":

    df = pd.read_csv(
        "datasets/PS_20174392719_1491204439457_log.csv"
    )

    ingest(df)

    print("Ingestion Complete")
