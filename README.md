# github_exercise
Choosen DS
   Single list (list) with computed balance
   Example:
    transactions = [
     ("income", 1000, "Salary"),
     ("expense", 500, "Rent"),
     ("expense", 200, "Groceries")
    ]

example how to compute balance
  balance = sum(item[1] if item[0] == "income" else -item[1] for item in transactions)  
  
