def coke_machine():
    
    amount = 50
        
    while amount != 0:
        print(f"Amount Due: {amount}")            
        coins = int(input("Insert Coins: "))

        if amount % coins == 0:
            amount = amount - coins
        

coke_machine()



