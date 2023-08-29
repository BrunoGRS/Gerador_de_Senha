import string, random

i = 0
senhafinal = []
caracter = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!','@','#','$','%'
'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h',
'I','i','J','j','k','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r',
'S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']

tamanho_senha = int(input("Digite o tamanho da sua senha ( Número ): "))

for i in range(0, tamanho_senha):
    rand = random.choice(caracter)
    senhafinal.append(rand)
    i =+ 1

for i in range(0, len(senhafinal)):
    if i == 0:
        print(f'Sua senha é: {senhafinal[i]}', end="")
    else:
        print(senhafinal[i], end="")