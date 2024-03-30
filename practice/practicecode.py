# oparator=input("enter the symbols + - * /: ")
# num1=int(input("enter the 1st number: "))  
# num2=int(input("enter the 2nd number: "))
# if oparator=="+":
#     result=num1+num2
#     print(round(result,3))
# elif oparator=="-":
#     result=num1-num2
#     print(round(result,3))
# elif oparator=="*":
#     result=num1*num2
#     print(round(result,3))
# elif oparator=="/":
#     result=num1/num2
#     print(round(result,3))
# else:
#     print(f"{oparator} is not defined")

#password generator
import random
import string

def genarate_password(lenght,uppercase,lowercase,number,symbol):
    character=' '
    if uppercase:
        character +=string.ascii_uppercase
    if lowercase:
        character += string.ascii_lowercase
    if number:
        character +=string.digits
    if symbol:
        character +=string.punctuation
    if not character:
        print("Error,it is not define")
    password=' '.join(random.choice(character)for ln in range(lenght))

    return password
    
lenght=int(input("enter the lenght of the password: "))
uppercase=input("include uppercase yes/no: ").lower()=="yes" 
lowercase=input("include lowercase yes/no: ").lower()=="yes" 
number=input("include number yes/no: ").lower()=="yes" 
symbol=input("include symbol yes/no: ").lower()=="yes" 

password=genarate_password(lenght,uppercase,lowercase,number,symbol)
print(password)