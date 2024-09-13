import random
import string

len=int(input("enter the length of the password: "))

char= string.ascii_letters
char+=string.digits
char+=string.punctuation

password=""

for i in range (len):
    new_char= random.choice(char)
    password+=new_char

print("your password is : " , password)
