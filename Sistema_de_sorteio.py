"""
Crie um programa que ajude um jogador na MEGA SENA
a dar palpites. O programa irá perguntar, quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta.
"""


from random import randint
from time import sleep

def linha():
    print('=' * 30)

lista_de_palpites = []
jogos = []

linha()
print(f'{"JOGA NA MEGA SENA":^30}')
linha()


quantidade_de_jogos = int(input('Quantos jogos quer que eu sorteie?'))
total_de_jogos = 1


while total_de_jogos <= quantidade_de_jogos:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista_de_palpites:
            lista_de_palpites.append(numero)
            contador += 1

        if contador > 6:
            break

    lista_de_palpites.sort()
    jogos.append(lista_de_palpites[:])
    lista_de_palpites.clear()
    total_de_jogos += 1

print('=' * 10, f' SORTEANDO {quantidade_de_jogos} JOGOS', '=' * 10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
linha()
print('=' * 5, '< BOA SORTE!>', '=' * 5)