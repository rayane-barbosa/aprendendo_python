#SistemaDeSatisfação


#Função Menu, vai mostrar as opções de filmes que serão solicitados ao cliente realizar sua classificação de Satisfação
def menu():

    print("Escolha uma opção:")
    print("1. Titanic")
    print("2. Harry Potter e o Prizioneiro de Azkaban")
    print("3. Pokémon. O filme!")
    print("4. Death Note")
    print("5. Crepúsculo")
    print("6. Corra!")
    print("7. Taxi-driver")
    print("8. O poderoso Chefão")
    print("9. Donnie Darko")
 
#Dicionario com as opções de filmes para seleçao

filme = {
    1: "Titanic",
    2: "Harry Potter e o Prizioneiro de Azkaban",
    3: "Pokémon. O filme!",
    4: "Death Note",
    5: "Crepúsculo",
    6: "Corra",
    7: "Taxi-driver",
    8: "O poderoso Chefão",
    9: "Donnie Darko",
        
}

#Função será selecionado um dos filmes para realizar a classificação 
def escolha_filme():
  opcaoFilme = int(input('Escolha o filme que deseja avaliar: '))
  escolha = filme.get(opcaoFilme)
  if escolha:
    print('Você escolheu o fime:  ' + escolha + ' para a sua avaliação!!')
  else:
    print("Não foi possível localizar a opção desejada!!!")
    escolha_filme()
  
#Dicionário para validar as Classificações 
avaliacoes = {
    1: "Você classificou esse filme como RUIM!!",
    2: "Você classificou esse filme como BOM!!",
    3: "Você classificou esse filme como ÓTIMO!!!"

 }

def avalia():
  respostaAvaliacao = int(input('Classifique o filme escolhido (1-3): '))
  escolhaSatisfacao = avaliacoes.get(respostaAvaliacao)
  if escolhaSatisfacao:
    print(escolhaSatisfacao)
  else:
    print('Não foi possível identificar sua opção!!')
    # avalia()


def conta_avaliacao(avaliacao):
  cont = 0 
  avaliacaoRuim = 0
  avaliacaoBom = 0
  avaliacaoOtimo = 0

  if avaliacao == 1:
    avaliacaoRuim += 1
  elif avaliacao == 2:
    avaliacaoBom +=1
  else:
    avaliacaoOtimo += 1
  # else:
    # avalia()


while True:
    menu()
    escolha_filme() 
    #avalia()     

    avaliacao = avalia() 
    continuar = input("Você deseja avaliar outro filme? (sim/não) ")
    if continuar.lower() != "sim":
        break
