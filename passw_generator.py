import random
from time import sleep
#Entrada do texto a ser convertido
letters = ""
num = 0
special_char = ""

while True:
    letters = input('Por favor informe uma palavra chave: ')
    if 4 <= len(letters) and letters.isalpha():
        letters = letters.lower()
        print("A palavra selecionada é ", letters)
        break
    else:
        print('Por favor, informe uma palavra com 4 a 6 digitos. Não são validos caracteres especiais ou números. ')


while True:
    num = input('Por favor defina dois algarimos chave: ')
    if len(num) >= 2 and num.isdigit():
        print('Você selecionou o número: ', num)
        break
    else:
        print('Favor informar pelo menos, dois números válidos. Algarismos de 0 a 9')

def lets_leet(text):
    """Leet the letters"""
    replacement = {
        'a' or 'A' : '@',
        'e' or 'E' : '3',
        'i' or 'I' : '1',
        'o' or 'O' : '0',
        's' or 'S' : '$'
    }

    for old, new in replacement.items():
        text = text.replace(old, new)    
    return text

def specializator(text):
    """randomizator"""
    characters = ["!","#", "%", "&", "*"]
    random_special = random.choice(characters)
    numero = random_special 
    return random_special

    

special_char = specializator(special_char)
print(num)
passwd_leeted = lets_leet(letters)
passwd_leeted = (passwd_leeted + str(special_char)+ str(num)).capitalize()
print("Sua senha é : ", passwd_leeted)


sleep(5)

