balance = 500
while True:
    
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance_anq")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
      try:
         amount = int(input("enter credit amount: "))
         def credit():
          global balance
          if amount <=0 :
            int(input("your balnc nill "))
          else:
            balance += amount
            print(f"${balance} credited to your account.")
         credit()
      except:
         print("please enter numbers 0-9")

    elif choice == '2':
        try:
           amount = int(input("Enter amount to debit: "))
           def Debit():
              global balance
           if amount <= 0:
              print("Please enter a positive amount.")
           elif balance <= 500:
              print("minimum maintanance 500.00 balance")
        #  elif amount > balance:
        #     print("Insufficient balance.")
           else:
              balance -= amount
              print(f"${balance} debited from your account.")
           Debit()
        except:
           print("plase enter amount means numbers 0-9")

    elif choice == '3':
        def balance_anq():
         print(f"Your current balance is: ${balance}") 
        balance_anq()
    elif choice == '4':
        def exit():
            print("Thank you for using the ATM. Goodbye!")
        exit()  
        break        



