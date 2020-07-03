
def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Forca      ")
    print("********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        tentativa = input("Qual a letra?")
        tentativa = tentativa.strip().upper()

        if(tentativa in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(tentativa == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1        

        acertou = "_" not in letras_acertadas
        enforcou = erros == 6      
        print(letras_acertadas)
        

    if(acertou):
        print("Voce Ganhou!!!")
    else:
        print("Voce perdeu!!")
    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar()