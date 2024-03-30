#password generator
import random
import string

def generate_password(lenght,uppercase,lowercase,number,symbols):
    characters=' '
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if number:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        print("Error ,no characters found")
    password=' '.join(random.choice(characters) for ln in range(lenght))

    return password

lenght=int(input("enter the password lenght: "))
uppercase=input('include uppercase yes/no: ').lower()=='yes'
lowercase=input('include lowercasae yes/no: ').lower()=='yes'
number=input('include number yes/no: ').lower()=='yes'
symbols=input('include symbols yes/no: ').lower()=='yes'

password=generate_password(lenght,uppercase,lowercase,number,symbols)
print(password)
    
