balance = 0

def addIncome(budgetData) :
    global balance
    amount = input("enter an amount")
    desc = input("enter a description")

    row = ("income", amount, desc)
    budgetData.append(row)
    balance += amount

    while True:
        choice = input("Do you want to add another ?(Y/n)")
        match choice:
            case "Y":
                return addIncome(budgetData)
            case "y":
                return addIncome(budgetData)
            case "n":
                break
            case _:
                print("invalid input")

    return budgetData




def addExpense(budgetData):
    global balance
    amount = input("enter an amount")
    desc = input("enter a description")

    row = ("expense", amount, desc)
    budgetData.append(row)
    balance -= amount

    while True:
        choice = input("Do you want to add another ?(Y/n)")
        match choice:
            case "Y":
                return addIncome(budgetData)
            case "y":
                return addIncome(budgetData)
            case "n":
                break
            case _:
                print("invalid input")
    return budgetData






def showBalance(budgetData):
    print(f"Your current balance is {balance}")
    return budgetData





def showTransactionHistory(budgetData):
    print(f"Your recent transactions: {budgetData}")
    return budgetData
