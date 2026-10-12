# Google Pay Expense Sharing  System

A lightweight Python application designed to track shared group expenses and calculate simplified settlements between friends, mimicking peer-to-peer bill-splitting workflows.

---

## Features

- **Dynamic Group Setup**: Initialize balances for any number of friends.
- **Split Expense Management**: Automatically divide expenses equally among specific participants while crediting the payer.
- **Settlement Minimization**: Uses a greedy debtor–creditor algorithm to settle debts with fewer individual transactions.
- **Interactive CLI**: Easy-to-use command-line interface for inputting transactions dynamically.

---

## Workflow & Architecture

1. **Initialization**: Group members are registered with net balances initialized to zero.
2. **Expense Logging**:
   - Each transaction calculates `split_amount = total_amount / number_of_participants`.
   - Each participant's balance decreases by `split_amount`.
   - The payer's balance increases by `total_amount`.
3. **Settlement Resolution**:
   - Members with negative balances are marked as **debtors**.
   - Members with positive balances are marked as **creditors**.
   - The system pairs debtors and creditors iteratively, clearing debts by transferring `min(debt, credit)` until all balances reach zero.

---

## Tech Stack

- **Language:** Python 3.x

---


## Installation & Setup

1. **Clone the repository:**
   ```bash
   https://github.com/dhanush24-m/GooglepayExpenseSharing.git

2. **Install Dependencies:**
   ```bash
   pip install python 

3.**Run the program:**
   ```bash
python googlepay_expense_sharing.py
 






   cd <repo-folder>
