print("\033c")

ap = int(input("enter actual price: "))
sp = int(input("enter selling price: "))

if ap < sp:
    profit = sp - ap
    print(f"profit: {profit}")
    
else:
    loss = ap - sp
    print(f"loss: {loss}")