class Expense:
    def __init__(self, expense_type, amount, date):
        self.expense_type = expense_type
        self.amount = amount
        self.date = date

class AccountingApp:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self):
        print("Enter your expenses below.")
        expense_type = input("Expense type: ")
        amount = float(input("Amount: "))
        date = input("Date (dd/mm/yyyy): ")
        
        self.expenses.append(Expense(expense_type, amount, date))
    
    def report(self):
        print("\n-----EXPENSE REPORT-----\n")
        for expense in sorted(self.expenses, key=lambda e: e.date):
            print("Type: ", expense.expense_type)
            print("Amount: ", expense.amount)
            print("Date: ", expense.date)
            print("\n------------------------\n")
            
    def run(self):
        while True:
            action = input('Enter "add" to add an expense, "report" to generate a report or "quit" to quit the app: ')
            
            if action == "add":
                self.add_expense()
            elif action == "report":
                self.report()
            elif action == "quit":
                break
                
app = AccountingApp()
app.run()