import random 

Target = random.randint(1,100)

while True:
    uc = input("guess the number or QUIT(Q):")
    if(uc== "Q"):
          break
    uc = int(uc)      
    if(uc == Target):
        print("sucess: correct guess!!")
        break
    elif(uc < Target):
        print("guess a bigger number")
    else:
        print("guess a smaller number")

print("----GAME OVER ----")