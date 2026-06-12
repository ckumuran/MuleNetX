import random
import time
import uuid

from backend.neo4j_client import neo4j_client


def create_transaction():

    source = f"LIVE_{random.randint(1,500)}"
    target = f"LIVE_{random.randint(501,1000)}"

    amount = random.randint(
        100,
        100000
    )

    fraud = 1 if amount > 75000 else 0

    query = """
    MERGE (s:Account {
        account_id:$source
    })

    MERGE (t:Account {
        account_id:$target
    })

    CREATE (s)-[:TRANSFER {
        transaction_id:$tx_id,
        amount:$amount,
        timestamp:datetime(),
        isFraud:$fraud
    }]->(t)
    """

    neo4j_client.execute(
        query,
        {
            "source": source,
            "target": target,
            "amount": amount,
            "fraud": fraud,
            "tx_id": str(uuid.uuid4())
        }
    )

    print(
        source,
        "->",
        target,
        amount
    )


while True:

    create_transaction()

    time.sleep(1)
