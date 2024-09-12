print("\033c")

num = int(input("enter a integer: "))

if num > 0:
    print(f"{num} is a positive number")
    print(f"i am in if block")
    
else:
    print(f"{num} is a negative number")
    print(f"i am in else block")
    
print("i am outside everything")