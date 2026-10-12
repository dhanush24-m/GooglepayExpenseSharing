import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class ExpenseSharing:
    def __init__(self, friends):
        self.freinds = friends
        self.balances = {friend: 0 for friend in friends}
        self.transactions = pd.DataFrame(columns=[
            'Payer', 'Amount', 'Participants'
        ])
        self.transaction_counter = 1

    def add_expense(self, payer, amount, participants):
        split_amount = amount / len(participants)
        for participant in participants:
               self.balances[participant] -= split_amount
        self.balances[payer] += amount

        new_tx = pd.DataFrame([{
            'Payer': payer,
            'Amount': amount,
            'Participants': ", ".join(participants)
        }])
        
        self.transactions = pd.concat([self.transactions, new_tx], ignore_index=True)
        self.transaction_counter += 1
        
    def calculate_settlement(self):
        creditors = []
        debtors = []

        for friend, balance in self.balances.items():
            if balance > 0:
                creditors.append((friend, balance))
            elif balance < 0:
                debtors.append((friend, -balance))
        
        while debtors and creditors:
            debtor, debt_amount = debtors.pop()
            creditor, credit_amount = creditors.pop()

            payment = min(debt_amount, credit_amount)
            print(f"{debtor} owes {creditor}: rs. {payment:.2f}")


if __name__ == "main":
    
    friends = input("Enter the names of friends, sepearted by commas:").split(",")
    friends = [friend.strip() for friend in friends]

    expense_sharing = ExpenseSharing(friends)

    while True:
        payer = input("Enter the name of thr person who paid(of 'done' to finish:)")
        if payer.lower() == "done":
            break

        amount = float(input("Enter the amount Paid:"))

        participants  = input("Enter the names of partcipants for this expense, seperated by commas:").split(",")

        participants = [participants.strip() for participant in participants]

        expense_sharing.add_expense(payer, amount,participants)
        print("\n Final settelement")
        expense_sharing.calculate_settlement()
            if debt_amount > payment:
                debtors.append((debtor, debt_amount - payment))
            if credit_amount >payment:
                creditors.append((creditor, credit_amount - payment))
