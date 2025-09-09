# 1 decima para corte 1

a = 1
value = int(input("Enter the value: "))

while a == 1:
    for i in range(1, value + 1):
        count = 0
        for n in range(1, i + 1):
            resid = i%n
            if resid == 0:
                count = count + 1
    
    if count == 2:
        print(f"{i} es un primo")
        print("/n")
    else:
        print(f"{i} NOO es un primo")
        print("/n")
    
    print("Do you want continue?. Press 1 to do that")
    a = input()
    a = int(a)
    
    if a != 1:
        break
    
    value = int(input("Enter a value: "))
