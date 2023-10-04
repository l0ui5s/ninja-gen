import string
import random
from colorama import Fore, Style, init

# inicia a biblioteca colorama
init()

# definindo as cores
title_color = Fore.RED
color_reset = Style.RESET_ALL


print(title_color + """                                                        
--                                          
--        _         _                       
--   ___ |_| ___   |_| ___    ___  ___  ___ 
--  |   || ||   |  | || .'|  | . || -_||   |
--  |_|_||_||_|_| _| ||__,|  |_  ||___||_|_|
--               |___|       |___|          

    - Non dvcor, dvco. 🦅                                                 


""" + color_reset)
# armazena os caracteres em lista
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


# pergunta quantos caracteres a senha vai possuir
user_input = input("Quantidade de letras para a senha: ")


# Vai checar o input e verificar se é um número e se é maior que 8, caso contrário irá repetir o processo
while True:

	try:

		characters_number = int(user_input)

		if characters_number < 8:

			print("O número mínimo é 8")

			user_input = input("Coloque a quantidade novamente: ")

		else:

			break

	except:

		print("A entrada é apenas de números")

		user_input = input("Quantos caracteres você quer na sua senha? ")


# embaralha as listas
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# calcula 30% & 20% dos números de caracteres 
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# gera a senha (60% letras and 40% digitos e pontuação)
result = []

for x in range(part1):

	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):

	result.append(s3[x])
	result.append(s4[x])


# embaralha o resultado
random.shuffle(result)


# resultado
password = "".join(result)
print("Stay safe 🎩: ", password)
