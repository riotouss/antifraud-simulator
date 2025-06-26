Simulated Antifraud System — Rule-Based Engine

This project demonstrates a basic simulation of a rule-based antifraud engine using Python.  
It evaluates the risk level of financial transactions based on various behavioral and technical indicators.

---

Features

- Parses CSV file with 100 randomly generated transactions.
- Calculates a risk score for each transaction using simple rules.
- Classifies transactions as `LOW`, `MEDIUM`, or `HIGH RISK`.
- Uses real-world fraud markers like:
  - Country of origin
  - Device status (new/known)
  - KYC verification
  - VPN usage
  - Payment method (card, crypto, e-wallet)
  - Card verification status
  - Amount threshold
    
    --- 
     
Risk Scoring Logic

| Indicator                        | Score |
|----------------------------------|--------|
| Amount > 1000                    | +2     |
| Country in RU/NG/CN              | +2     |
| New device                       | +1     |
| Card not verified                | +1     |
| VPN used                         | +1     |
| KYC not passed                   | +2     |
| Payment method: Crypto           | +2     |
| Payment method: E-wallet         | +1     |

---

Project Structure


├── Antifraud_Simulator.py # Main logic for scoring transactions
├── generated_transactions.csv # Test data with 100 random transactions
├── README.md # This documentation


 --- 

Example Output

Transaction 1 - (user188) - HIGH RISK
Transaction 2 - (user185) - HIGH RISK
Transaction 3 - (user885) - HIGH RISK
Transaction 4 - (user549) - MEDIUM RISK
Transaction 5 - (user885) - HIGH RISK
Transaction 6 - (user299) - MEDIUM RISK
Transaction 7 - (user938) - HIGH RISK


---
