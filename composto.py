import string, random
from PySimpleGUI import PySimpleGUI as sg


# Layout
sg.theme('reddit')
layout = ([sg.Text('Digite o tamanho da senha ( Número ):'), sg.Input(key='tamanho_senha', size=(5,1))],
          [sg.Text('Sua senha é:'), sg.Text('', key='senha_gerada')],
          [sg.Button('Gerar')])

#Janela
janela = sg.Window('Gerador de Senha', layout)

#eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Gerar':
        i = 0
        senhafinal = []
        caracter = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!','@','#','$','%'
        'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h',
        'I','i','J','j','k','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r',
        'S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']

        tamanho_senha = int(valores['tamanho_senha'])

        for i in range(0, tamanho_senha):
            rand = random.choice(caracter)
            senhafinal.append(rand)
            i =+ 1

        senha_gerada = ''.join(senhafinal)
        janela['senha_gerada'].update(senha_gerada)
