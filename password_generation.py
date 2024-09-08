import random 
import string
l = int(input("enter length of password"))
charv = string.ascii_letters + string.digits + string.punctuation
res = "".join([random.choice(charv) for i in range(l)])
print(res)