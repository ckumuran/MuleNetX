import pandas as pd
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "password"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

CSV_PATH = "../datasets/raw/paysim.csv"

df = pd.read_csv(CSV_PATH)

# start small
df = df.head(10000)

query = """
MERGE (s:Account {account_id:$sender})

MERGE (r:Account {account_id:$receiver})

MERGE (s)-[t:TRANSFERRED {
    amount:$amount,
    txn_type:$txn_type,
    step:$step,
    isFraud:$isFraud
}]->(r)
"""

with driver.session() as session:

    for _, row in df.iterrows():

        session.run(
            query,
            sender=row["nameOrig"],
            receiver=row["nameDest"],
            amount=float(row["amount"]),
            txn_type=row["type"],
            step=int(row["step"]),
            isFraud=int(row["isFraud"])
        )

print("Import Complete")

driver.close()
