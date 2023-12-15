print("ESCAPE DA PRINCIPAL OFFICE!")
print("Three doors ahead of you, and principal behind one of them")
print("Which door do you want to open?")
door = input("1, 2, or 3? : ")
score = 0

if door == "1":
    print("You escaped!")
    score += 10

elif door == "2":
    print("AAAA principal!!! Run!!!")
    score = 0

elif door == "3":
    print("This Door Is Damn Locked!")
    score += 0

print("Your score: "+ str(score))
