# Google Pay Expense Sharing  System

A Python-based expense tracking and debt settlement tool inspired by Google Pay's group bill split functionality. The application tracks shared group expenditures and calculates optimal settlements to clear all debts.

---

## Key Features

- **Group Initialization:** Create custom groups with multiple participants.
- **Dynamic Expense Splitting:** Split bills equally among specified subsets of group members.
- **Transaction Logging:** Store transaction history (Payer, Amount, Participants) in structured Pandas DataFrames.
- **Automated Debt Settlement:** Calculate net balances and resolve inter-member debts using a greedy balance-offset algorithm.

---

## Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `pandas` (transaction tracking and tabular logging)
  - `numpy` (numerical calculations)
  - `matplotlib.pyplot` (data visualization)

---

## System Architecture & Workflow

1. **Initialization:** The `ExpenseSharing` class initializes a dictionary mapping each friend to a zero net balance and creates an empty transactions table.
2. **Expense Addition:** 
   - When a user pays for an expense, the total cost is divided equally across all participants.
   - Each participant's balance decreases by `amount / N`.
   - The payer's balance increases by `amount`.
   - The transaction details are appended to the DataFrame log.
3. **Settlement Calculation:**
   - Members are partitioned into **creditors** (net positive balance) and **debtors** (net negative balance).
   - A greedy loop matches debtors with creditors to settle payments until all net balances are cleared.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   https://github.com/dhanush24-m/GooglepayExpenseSharing.git

2. **Install Dependencies:**
   ```bash
   pip install pandas numpy matplotlib

3.**Run the program:**
   ```bash
python GooglePay_Expense_Sharing.py
 






   cd <repo-folder>
