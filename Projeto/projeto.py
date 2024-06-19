import random
import nltk
from nltk.corpus import wordnet as wn
import time

# Baixando os dados necessários do WordNet
nltk.download('wordnet')
nltk.download('omw-1.4')

resultados = []

def obter_palavras_e_dicas(nivel_dificuldade):
    palavras_dicas = {}
    for synset in wn.all_synsets():
        if synset.lemmas('por'):
            for lemma in synset.lemmas('por'):
                palavra = lemma.name().lower().replace('_', ' ')
                definicao = synset.definition()
                if palavra not in palavras_dicas and definicao:
                    # Adicionar verificação de tamanho da palavra para o nível de dificuldade
                    if nivel_dificuldade == 'facil' and len(palavra) <= 5:
                        palavras_dicas[palavra] = definicao
                    elif nivel_dificuldade == 'medio' and 5 < len(palavra) <= 8:
                        palavras_dicas[palavra] = definicao
                    elif nivel_dificuldade == 'dificil' and len(palavra) > 8:
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

def jogar_palavras_cruzadas(nivel_dificuldade):
    palavras_dicas = obter_palavras_e_dicas(nivel_dificuldade)
    if not palavras_dicas:
        print("Nenhuma palavra disponível para jogar.")
        return

    palavra, dica = escolher_palavra(palavras_dicas)
    letras_corretas = set()
    tentativas = 0
    inicio_jogo = time.time()

    print(f"Bem-vindo ao jogo de Palavras Cruzadas! Nível: {nivel_dificuldade.capitalize()}\n")

    while True:
        exibir_tabuleiro(palavra, dica, letras_corretas)
        letra = input("Digite uma letra ou 'sair' para encerrar o jogo: ").lower()

        if letra == "sair":
            print("Obrigado por jogar! Até a próxima.")
            resultados.append({"Palavra": palavra, "Resultado": "Não completou", "Nível": nivel_dificuldade})
            break
        elif letra == "dica":
            print("Dica extra:", dica[:50])  # Mostrar apenas parte da dica
            continue

        tentativas += 1

        if letra in palavra.lower():
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            print("Letra incorreta. Tente novamente.")

        if letras_corretas == set(palavra.lower().replace(" ", "")):
            fim_jogo = time.time()
            tempo_total = round(fim_jogo - inicio_jogo, 2)
            print(f"Parabéns! Você acertou a palavra: {palavra}. Tempo total: {tempo_total} segundos. Tentativas: {tentativas}")
            resultados.append({"Palavra": palavra, "Resultado": "Completou", "Nível": nivel_dificuldade, "Tempo": tempo_total, "Tentativas": tentativas})
            break

def exibir_resultados():
    if not resultados:
        print("\nNenhum resultado para exibir.")
    else:
        print("\nHistórico de Resultados:")
        for idx, resultado in enumerate(resultados, start=1):
            print(f"Jogo {idx}: Palavra: {resultado.get('Palavra', '')}, Resultado: {resultado.get('Resultado', '')}, Nível: {resultado.get('Nível', '')}, Tempo: {resultado.get('Tempo', '')} segundos, Tentativas: {resultado.get('Tentativas', '')}")

while True:
    print("\nMenu:")
    print("1. Jogar Palavras Cruzadas (Fácil)")
    print("2. Jogar Palavras Cruzadas (Médio)")
    print("3. Jogar Palavras Cruzadas (Difícil)")
    print("4. Exibir Resultados")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogar_palavras_cruzadas('facil')
    elif escolha == "2":
        jogar_palavras_cruzadas('medio')
    elif escolha == "3":
        jogar_palavras_cruzadas('dificil')
    elif escolha == "4":
        exibir_resultados()
    elif escolha == "5":
        print("Obrigado por usar o programa! Até a próxima.")
        break
    else:
        print("Opção inválida. Tente novamente.")
