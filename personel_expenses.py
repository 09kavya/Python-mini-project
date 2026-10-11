expenses=[]

while True:
    
    menu=input("Choose menu : \n 1. Add menu \n 2. Show expenses \n 3. total \n 4. exit \n")
    if menu=="1":
        expense=input("Enter the expense: ")
        amount=int(input('Enter the amount: '))
        expenses.append([expense,amount])
        print("Successfully entered")
    elif menu=="2":
        print("\n your expenses :")
        for i in range (len(expenses)):
            print(expenses[i][0],"- Rs.",expenses[i][1])

    elif menu=="3":
        total=0
        for i in range(len(expenses)): 
            total += expenses[i][1]       
        print(f"\ntotal is : {total}")

        max_expense=expenses[0]
        for i in (expenses):
            if i[1]>max_expense[1]:
                max_expense=i
        print("\nMaximum expense:", max_expense[0], "- Rs.", max_expense[1])

    elif menu=="4":
        break