import json
with open("data/accounts.json") as f:
    accounts = json.load(f)
for account in accounts:
    velocity = account["velocity"]
    connections = account["connections"]
    score = (velocity * 0.6) + (connections * 0.4)
    account["risk"] = min(100, round(score))
print(accounts)
