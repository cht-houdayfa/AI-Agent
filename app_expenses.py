## كود بايثون لتطبيق الحساب المصرفي
```python
class Expense:
    def __init__(self, date, type_of_expense, value):
        self.date = date
        self.type_of_expense = type_of_expense
        self.value = value

class UserAccount:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, expense):
        self.expenses.append(expense)
        
    def get_expenses(self):
        return self.expenses

class Analytics:
    @staticmethod
    def total_spendings(userAccount):
        total = 0
        for expense in userAccount.get_expenses():
            total += expense.value
        return total
    
    @staticmethod
    def analyze_by_date(userAccount, date):
        count = 0
        for expense in userAccount.get_expenses():
            if expense.date == date:
                count += 1
        return count
        
    @staticmethod
    def analyze_by_type(userAccount, type_of_expense):
        total = 0
        count = 0
        for expense in userAccount.get_expenses():
            if expense.type_of_expense == type_of_expense:
                total += expense.value
                count += 1
        return total, count
```
## كود الاستخدام
```python
user = UserAccount()
user.add_expense(Expense('2022-04-05', 'food', 20))
user.add_expense(Expense('2022-04-06', 'rent', 100))
print("Total spendings: ", Analytics.total_spendings(user)) # يطلع المبلغ الكلى للمصروفات
print("Number of food expenses on '2022-04-05': ", Analytics.analyze_by_type(user, 'food')) # عدد المصروفات الطبيخى للتاريخ