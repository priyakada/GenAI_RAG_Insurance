import pandas as pd
import random
import os

os.makedirs("data", exist_ok=True)

customers = [
    "John", "Emma", "David", "Sophia", "Michael",
    "Olivia", "James", "Priya", "Rahul", "Aisha"
]

hospitals = [
    "Apollo Hospital",
    "Fortis Hospital",
    "Manipal Hospital",
    "Aster Hospital",
    "Narayana Health"
]

diagnosis = [
    "Diabetes",
    "Heart Disease",
    "Fracture",
    "Cancer",
    "Fever",
    "Kidney Stone",
    "Asthma"
]

status = ["Approved", "Rejected", "Pending"]

policies = ["Gold", "Silver", "Platinum"]

rows = []

for i in range(1, 101):
    rows.append({
        "claim_id": f"C{i:03}",
        "customer_name": random.choice(customers),
        "policy_type": random.choice(policies),
        "claim_amount": random.randint(5000, 200000),
        "claim_status": random.choice(status),
        "hospital_name": random.choice(hospitals),
        "diagnosis": random.choice(diagnosis),
        "city": random.choice(["Bangalore", "Hyderabad", "Chennai", "Mumbai"])
    })

df = pd.DataFrame(rows)

df.to_csv("data/gold_claims.csv", index=False)

print("Gold dataset created successfully!")
print(df.head())