import random
import nltk
from nltk.corpus import wordnet as wn

# Baixando os dados necessários do WordNet
nltk.download('wordnet')
nltk.download('omw-1.4')

resultados = []

def obter_palavras_e_dicas():
    palavras_dicas = {}
    for synset in wn.all_synsets():
        if synset.lemmas('por'):
            for lemma in synset.lemmas('por'):
                palavra = lemma.name().lower().replace('_', ' ')
                definicao = synset.definition()
                if palavra not in palavras_dicas and definicao:
                    palavras_dicas[palavra] = definicao
    return palavras_dicas

def escolher_palavra(palavras_dicas):
    if not palavras_dicas:
        raise ValueError("Nenhuma palavra disponível para jogar.")
    palavra = random.choice(list(palavras_dicas.keys()))
    dica = palavras_dicas[palavra]
    return palavra, dica

def exibir_tabuleiro(palavra, dica, letras_corretas):
    print("\nDica:", dica)
    print("Palavra:")
    for letra in palavra:
        if letra.lower() in letras_corretas or letra == " ":
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")

def jogar_palavras_cruzadas():
    palavras_dicas = obter_palavras_e_dicas()
    if not palavras_dicas:
        print("Nenhuma palavra disponível para jogar.")
        return

    palavra, dica = escolher_palavra(palavras_dicas)
    letras_corretas = set()

    print("Bem-vindo ao jogo de Palavras Cruzadas!\n")

    while True:
        exibir_tabuleiro(palavra, dica, letras_corretas)
        letra = input("Digite uma letra ou 'sair' para encerrar o jogo: ").lower()

        if letra == "sair":
            print("Obrigado por jogar! Até a próxima.")
            resultados.append({"Palavra": palavra, "Resultado": "Não completou"})
            break
        elif letra in palavra.lower():
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            print("Letra incorreta. Tente novamente.")

        if letras_corretas == set(palavra.lower().replace(" ", "")):
            print("Parabéns! Você acertou a palavra:", palavra)
            resultados.append({"Palavra": palavra, "Resultado": "Completou"})
            break

def exibir_resultados():
    print("\nHistórico de Resultados:")
    for idx, resultado in enumerate(resultados, start=1):
        print(f"Jogo {idx}: Palavra: {resultado['Palavra']}, Resultado: {resultado['Resultado']}")

while True:
    print("\nMenu:")
    print("1. Jogar Palavras Cruzadas")
    print("2. Exibir Resultados")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogar_palavras_cruzadas()
    elif escolha == "2":
        exibir_resultados()
    elif escolha == "3":
        print("Obrigado por usar o programa! Até a próxima.")
        break
    else:
        print("Opção inválida. Tente novamente.")
