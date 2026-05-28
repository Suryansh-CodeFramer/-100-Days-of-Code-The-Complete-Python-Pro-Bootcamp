import random

pAlpha = int(input("How many letters would you like?\n"))
pSym = int(input("How many symbols would you like?\n"))
pNum = int(input("How many numbers would you like?\n"))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '<', '>', '?', '/']

password_list = []

for i in range(0, pAlpha):
    random_char = alphabets[random.randint(0, len(alphabets) - 1)]
    password_list.append(random_char)

for i in range(0, pSym):
    random_sym = symbols[random.randint(0, len(symbols) - 1)]
    password_list.append(random_sym)

for i in range(0, pNum):
    random_num = numbers[random.randint(0, len(numbers) - 1)]
    password_list.append(random_num)

random.shuffle(password_list)

password_string = ""
for character in password_list:
    password_string += character

print(f"Your secure password is: {password_string}")