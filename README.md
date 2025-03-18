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
                      
          addIncome(budgetData)              
            function will receive the above data structure, ask the user to enter new income, (amount,description)
            add the new income to the data structure and return the new data structure   
          addExpense(budgetData)                          
             function will receive the above data structure, ask the user to enter new expense, (amount,description)
             add the new expense to the data structure and return the new data structure  
          showBalance(budgetData)
             will receive the DS, do over it one by one, sum the total balance and print it, doesnt return anything
          showTransactionHistory(budgetData)                             
             will receive the DS, prinintg each transaction one by one, doesnt return anything

