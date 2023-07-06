import time
import random 
import os 

def limparterminal():
    os.system("cls")

def apresentacao():
    print("Seja bem vindo ao jogo de papel e tesoura, um jogo simples mas que vai fazer você se divertir muito")
    print()
    time.sleep(1)
    print("Regras do jogo:")
    print("""
    1 - Papel
    2 - Tesoura 
    3 - Pedra 

O seu adversario será a maquina e será jogado de maneira aleatoria pelo computador.
    """)
    time.sleep(2)
    enter = input("Aperte o ENTER para iniciar o jogo.")
    time.sleep (2)
    print("Iniciando...")
    time.sleep(1)

limparterminal()

apresentacao()

limparterminal()

jogorodando = True
contador = 0
vitorias = 0 
empates = 0 
derrotas = 0 

while jogorodando:
    jogada = input("Qual será a sua jogada? ")
    listadejogadas = ["papel", "tesoura", "pedra"]
    jogadapc = random.choice(listadejogadas)
    
    jogadaa = jogada.lower()

    if jogadaa != "papel" and jogadaa != "pedra" and jogadaa != "tesoura":
        print("Jogada invalida, tente novamente!")

    else:
        if jogadaa == jogadapc:
            empates += 1
            print("O computador jogou " + jogadapc + "\nO resultado do jogo deu Empate!")

        elif jogadaa == "papel" and jogadapc == "tesoura":
            derrotas += 1
            print("O computador jogou " + jogadapc + "\nVocê perdeu!")

        elif jogadaa == "papel" and jogadapc == "pedra":
            vitorias += 1
            print("O computador jogou " + jogadapc + "\nVocê ganhou!")

        elif jogadaa == "tesoura" and jogadapc == "papel":
            vitorias += 1
            print("O computador jogou " + jogadapc + "\nVocê ganhou!")

        elif jogadaa == "tesoura" and jogadapc == "pedra":
            derrotas += 1
            print("O computador jogou " + jogadapc + "\nVocê perdeu!")

        elif jogadaa == "pedra" and jogadapc == "papel":
            derrotas += 1
            print("O computador jogou " + jogadapc + "\nVocê perdeu!")

        elif jogadaa == "pedra" and jogadapc == "tesoura":
            vitorias += 1
            print("O computador jogou " + jogadapc + "\nVocê ganhou!")

        contador += 1
        time.sleep(2)
        a = input("Deseja jogar novamente? (S/N) ")
        aa = a.lower()
        if aa == "n" or aa == "não":
            jogorodando = False
        elif aa == "s" or aa == "sim":
            print()
            jogorodando


contadortext = str(contador) #Convertendo o tipo da variável para string 
derrotatext = str(derrotas) 
empatestext = str(empates) 
vitoriastext = str(vitorias)

time.sleep(2)
limparterminal()

print("""Fim de jogo!
Muito obrigado por ter participado desse jogo e 
espero que tenha gostado desse algoritmo simples.""")
print()
time.sleep(3)
limparterminal()
print("O numero de jogadas durante o jogo foi igual a " + contadortext)

print("Classificação do jogo:")
print()
print("Vitorias = " + vitoriastext)  
print("Empates = " + empatestext)
print("Derrotas = " + derrotatext)
