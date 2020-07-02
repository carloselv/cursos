import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade desejado?")
    print("1 - Facil")
    print("2 - Medio")
    print("3 - Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
      total_tentativas = 20
    elif(nivel == 2):
      total_tentativas = 10
    else:
      total_tentativas = 5

    for rodada in range(1,total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        tentativa_str = input("Digite o seu numero(entre 1 e 100): ")
        print("Você digitou o numero: ", tentativa_str)
        tentativa = int(tentativa_str)

        if(tentativa < 1 or tentativa > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == tentativa
        maior   = tentativa > numero_secreto
        menor   = tentativa < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Sua tentativa foi maior que o número")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Sua tentativa foi menor que o número")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos = pontos - pontos_perdidos
            

print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
