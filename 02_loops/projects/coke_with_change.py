def coke_machine():
    
    amount = 50
        
    while amount > 0:

        print(f"Amount Due: {amount}")            
        coins = int(input("Insert Coins: "))

        if coins in (25, 10, 5):        
            amount -= coins

        else:
            print("Accepted denominations: 5, 10, 25")

    print(f"Change Given: {0 - amount}")
    
coke_machine()





