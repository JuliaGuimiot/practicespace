import json

with open("RWE_Emails.json", "r") as f:
    data = json.load(f)
    for user in data["new_emails"]:
        print(data["new_emails"][user])
