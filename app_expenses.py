class Expense:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

class UserExpensesApp:
    def __init__(self):
        self.expenses = []
        
    # إدخال المصاريف
    def add_expense(self, date, type, amount):
        expense = Expense(date, type, amount)
        self.expenses.append(expense)
    
    # عرض التقارير
    def display_reports(self, frequency='monthly'):
        if frequency == 'monthly':
            for expense in self.expenses:
                print("Date: ", expense.date)
                print("Type: ", expense.type)
                print("Amount: ", expense.amount)
                print("\n")
    
    # دعم التحليل
    def analyze_expenses(self):
        revenue = sum([e.amount for e in self.expenses if e.amount > 0])
        expenses = sum([abs(e.amount) for e in self.expenses])
        print("Total Revenue: ", revenue)
        print("Total Expenses: ", expenses)
``` 

تم تصميم التطبيق والكود به طريقة منظمة ومستمرة. لتحميل المصاريف، استخدم `add_expense` بالتنسيق (`date`, `type`, `amount`). لعرض التقارير، استخدم 'display_reports' ولتحليل المصاريف، استخدم `analyze_expenses`. تم تعريف الكلاس `Expense` لتنفيذ هذه المصاريف، و `UserExpensesApp` لتضمين جميع الميزات المطلوبة.