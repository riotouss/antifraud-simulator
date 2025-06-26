import csv

def evaluate_transaction(tx):
    risk_score = 0

    if float(tx['amount']) > 1000:
        risk_score += 2
    if tx['country'] in ["RU", "NG", "CN"]:
        risk_score += 2
    if tx['device'] == "new":
        risk_score += 1
    if tx['card_verified'].strip().lower() == "false":
        risk_score += 1
    if tx['vpn'].strip().lower() == "true":
        risk_score += 1
    if tx['kyc_verified'].strip().lower() == "false":
        risk_score += 2
    if tx['payment_method'].strip().lower() == "crypto":
        risk_score += 2
    elif tx['payment_method'].strip().lower() == "e-wallet":
        risk_score += 1
    
    

    if risk_score >= 6:
        return "HIGH RISK"
    elif risk_score >= 3:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

with open('generated_transactions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        result = evaluate_transaction(row)
        print(f"Transaction {row['id']} - ({row['user_id']}) - {result}")