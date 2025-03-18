import functions

runProgram = True
while runProgram:
    print(f"\nWelcome To Store Inventory Manager\n")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show transaction history")
    print("5. Exit the program")


    choice = input("\nPlease enter your choice: ")

    match choice:
        case "1":                       
          #DS = functions.addIncome(budgetData)              
        case "2":                          
          #DS = functions.addExpense(budgetData)                          
        case "3":
          #functions.showBalance(budgetData)
        case "4":
          #functions.showTransactionHistory(budgetData)                             
        case "5":
          #print("\nExiting the program...")
          break
        case _:
          print("\nInvalid choice!! please choose again..")

