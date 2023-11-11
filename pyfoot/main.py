def LerArquivo():
  # Inicialize uma lista para armazenar as informações
  informacoes = []
  # Abra o arquivo em modo de leitura
  with open("copadomundo.txt", "a") as arquivo:
      for linha in arquivo:
          

          # Divida a linha em elementos usando a vírgula como separador
          elementos = linha.strip().split(',')
          # Adicione os elementos à lista de informações
          informacoes.append(elementos)
  return informacoes

print("Olá! Você está buscando informações sobre o mundo do futebol? Siga o passo a passo e torne-se um gênio da bola!\n")

while True:
  print("Digite 1 para: UEFA Champions League")
  print("Digite 2 para: Libertadores")
  print("Digite 3 para: Copa do Mundo")
  print()

  camp = int(input("Escolha um dos campeonatos acima: "))
  print()

  if camp == 1:
      print("Vejo que você é um amante do futebol europeu. Que ótimo!")
      ano_pesquisa = int(input("Agora, digite o ano da temporada que você deseja saber: "))
      torneio= "UEFA Champions League"
      # Você pode implementar a pesquisa para a UEFA Champions League aqui
  elif camp == 2:
      print("Vejo que você é um apreciador do futebol sul-americano. Excelente escolha!")
      ano_pesquisa = int(input("Agora, digite o ano da temporada que você deseja saber: "))
      torneio = "Libertadores"
      # Você pode implementar a pesquisa para a Libertadores aqui
  elif camp == 3:
      print("Vejo que você é um admirador do futebol mundial. Ótimo gosto!")
      ano_pesquisa = str(input("Agora, digite o ano da temporada que você deseja saber: "))
      
      with open(f"copadomundo.txt", "r", encoding="utf-8") as file:
         arquivo = file.read()
         linhas = arquivo.split(f"\n")
         anos = dict()
         for l in linhas:
 
            ANO, CAMPEAO, VICE, ART, PART, GOLS, SEDE, CURIO, PLACAR = l.split(",")
            anos[ANO] = (CAMPEAO, VICE, ART, PART, GOLS, SEDE, CURIO, PLACAR)
            encontrou = True
     

  if ano_pesquisa in anos:
     print()
     print("********************************************")
     print(f"No ano de {ano_pesquisa}, o país sede foi{anos[ano_pesquisa][5]}, o{anos[ano_pesquisa][0]} foi campeão e o{anos[ano_pesquisa][1]} foi o vice-campeão. O artilheiro foi{anos[ano_pesquisa][2]} do país{anos[ano_pesquisa][3]} com{anos[ano_pesquisa][4]} gols.")
     print(f"Curiosidade:{anos[ano_pesquisa][6]}")
     print(f"Placar final:{anos[ano_pesquisa][7]}")
     print("********************************************")
     print()
  else:
    print()
    print("Infelizmente não foi possívem encontrar as informações.")
    print()
    
  denovo = input("Você deseja fazer uma nova pesquisa? Digite sim ou não: ").upper()
  if denovo != "SIM":
      break

