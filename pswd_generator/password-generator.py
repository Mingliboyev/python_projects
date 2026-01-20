import random
import string

def generate_password(min_length, numbers=False, specials=False):
    letters=string.ascii_letters
    digits=string.digits
    chars=string.punctuation
    
    needs=letters
    if numbers:
        needs+=digits
    if specials:
        needs+=chars
    
    pswd=""
    meets_criteria=False
    has_number=False
    has_char=False
    while len(pswd)<min_length or not meets_criteria:
        char=random.choice(needs)
        pswd+=char
        if char in digits:
            has_number=True
        elif char in chars:
            has_char=True
        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if specials:
            meets_criteria=meets_criteria and has_char        
    return pswd


length=int(input("Enter the minimum length of the password: "))
digits=input("Should we inclde digits (y/n): ").lower()=="y"
chars=input("Should we inclde special characters (y/n): ").lower()=="y"

print(generate_password(length, digits, chars))

