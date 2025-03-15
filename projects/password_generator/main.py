import random
import string

length=int(input("enter length for ur password: "))

x=string.ascii_letters
y=string.digits
z=string.punctuation
all = x+y+z

password="".join(random.choices(all,k=length))
print("Generated Password:", password)



