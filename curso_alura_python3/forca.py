import random


def jogar():

    imprimir_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
   
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        tentativa = pedir_tentativa()
        
        if(tentativa in palavra_secreta):
            marcar_tentativa_correta(tentativa,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)        

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7      
        print(letras_acertadas)
        

    if(acertou):
        imprimir_mensagem_vencedor()        
    else:
        imprimir_mensagem_perdedor(palavra_secreta)
 


def imprimir_mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de Forca      ")
    print("********************************")


def carregar_palavra_secreta():    
    #arquivo = open("palavras.txt", "r")
    arquivo = open("palavras.txt", "r",encoding="UTF-8")
    palavras = []    

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pedir_tentativa():
    tentativa = input("Qual a letra?")
    tentativa = tentativa.strip().upper()
    return tentativa

def marcar_tentativa_correta(tentativa,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(tentativa == letra):
            letras_acertadas[index] = letra
        index += 1

def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
