from . import Expense

expenses = Expense.Expense
Expense.read_expenses(expenses, "data\\spending_data.csv")
