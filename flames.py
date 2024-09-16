def Flames(name1, name2):
    
    namestr = name1 + name2

    
    for c in set(name1): 
        if c in name2:  
            common_count = min(name1.count(c), name2.count(c))
            namestr = namestr.replace(c, "", common_count)  
    for c in set(name2):
        if c in name1:
            common_count = min(name2.count(c), name1.count(c))
            namestr = namestr.replace(c, "", common_count)
    print("FLAMES....")
    print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")

    number = len(namestr) % 6 
    rel = ""

    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection"
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 0:
        rel += "Siblings"

    return rel


n1 = input("Enter your name : ").upper()
n2 = input("Enter name of your crush : ").upper()
print(f"Your Relationship is : {Flames(n1, n2)}")
