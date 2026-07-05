import datetime
class Expense:
    def __init__(self, type, date, amount):
        self.type = type
        self.date = date
        self.amount = amount

class MonthlyExpensesApp:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def daily_expenses(self):
        today = datetime.date.today()
        daily_expenses = [e for e in self.expenses if e.date == today]
        
        total_daily_expenses = 0
        for expense in daily_expenses:
            total_daily_expenses += expense.amount
            
        return total_daily_expenses
    
    def categorize_expenses(self, category):
        cat_expenses = [e for e in self.expenses if e.type == category]
        
        total_cat_expenses = 0
        for expense in cat_expenses:
            total_cat_expenses += expense.amount
            
        return total_cat_expenses