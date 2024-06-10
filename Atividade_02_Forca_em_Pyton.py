import random

def escolher_palavra():
    lista_palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias"]
    palavra = random.choice(lista_palavras)
    return palavra
def exibir_forca(tentativas):
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(estados[tentativas])
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_tentadas = set()
    
    print("Bem-vindo ao Jogo da Forca!")
    exibir_forca(tentativas)
    print("Palavra: " + " ".join(palavra_oculta))
    
    while tentativas < 6 and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue
        
        letras_tentadas.add(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
        
        exibir_forca(tentativas)
        print("Palavra: " + " ".join(palavra_oculta))
        print("Letras tentadas: " + ", ".join(letras_tentadas))
        
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
    
    if tentativas == 6:
        print("Você perdeu! A palavra era:", palavra)

    print("Obrigado por jogar!")
jogar()
