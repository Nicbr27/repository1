def LerArquivo():
  # Inicialize uma lista para armazenar as informações
  informacoes = []
  # Abra o arquivo em modo de leitura
  with open('copadomundo.txt', 'a') as arquivo:
      for linha in arquivo:
          # Divida a linha em elementos usando a vírgula como separador
          elementos = linha.strip().split(',')
          # Adicione os elementos à lista de informações
          informacoes.append(elementos)
  return informacoes

print("Olá! Você está buscando informações sobre o mundo do futebol? Siga o passo a passo e torne-se um gênio da bola!\n")

while True:
  encontrou = False
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
      ano_pesquisa = int(input("Agora, digite o ano da temporada que você deseja saber: "))

      torneio = "Copa do Mundo"
      camp = ('copadomundo.txt')

      for info in camp:
          if info[0] == str(ano_pesquisa):
              ano_pesquisa = int(info[0])
              campeao = info[1]
              vicecampeao = info[2]
              artilheiro = info[3]
              pais = info[4]
              gols = info[5]
              sede = info[6]
              curiosidade = info[7]
              encontrou = True

  if encontrou == True:
    print()
    print("********************************************")
    print(f"No ano de {ano_pesquisa}, o país sede foi {pais}, o {campeao} foi campeão da {torneio} e o {vicecampeao} foi o vice-campeão. O artilheiro foi {artilheiro} com {gols} gols.")
    print(f"Sede: {sede}")
    print(f"Curiosidade: {curiosidade}")
    print("********************************************")
    print()
  else:
    print()
    print("Infelizmente não foi possívem encontrar as informações.")
    print()
    
  denovo = input("Você deseja fazer uma nova pesquisa? Digite sim ou não: ").upper()
  if denovo != "SIM":
      break

