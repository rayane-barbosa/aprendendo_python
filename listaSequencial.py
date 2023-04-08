class ListaSequencial:
  def __init__(self):
    #Inicializa uma lista vazia e o tamanho da lista
    self.lista = []
    self.tamanho = 0

  def __str__(self):
    #Retorna uma string que representa a lista
    return str(self.lista)
  
  def adiciona(self, valor):
    #Adiciona um valor no final da lista e incrementa o tamanho
    self.lista.append(valor)
    self.tamanho +=1

  def remove(self, valor):
    # Remove a primeira ocorrência de um valor na lista e decrementa o tamanho
    if valor in self.lista:
      self.lista.remove(valor)
      self.tamanho -=1

  def contem(self, valor):
    #Verifica se um valor está presente na lista
    return valor in self.lista


  def indice(self, valor):
    # Retorna o índice da primeira ocorrência de um valor na lista
    if valor in self.lista:
      return self.lista.index(valor)
    # Se o valor não está presente na lista, retorna -1
    return -1

  def tamanho_lista(self):
  #Retorna o tamanho da lista
    return self.tamanho
  
  def obtem_elemento(self, posicao):
    if posicao >=0 and posicao < self.tamanho:
      return self.lista[posicao]
    #Se a posição não é válida, levanta um erro de índice fora do intervalo válido
    raise IndexError("índice fora do intervalo válido")

  def limpa_lista(self):
    #Remove todos os elementos da lista e zera o tamanho
    self.lista.clear()
    self.tamanho =0


    def main():
    # Cria uma nova lista sequencial
    lista = ListaSequencial()

    # Adiciona alguns valores à lista
    lista.adiciona('a')
    lista.adiciona('b')
    lista.adiciona('c')
    lista.adiciona('d')
    lista.adiciona('e')
    
    # Imprime a lista
    print("Lista: ", lista)

    # Verifica se um valor está presente na lista
    print("A lista contém o valor a?", lista.contem('a'))
    print("A lista contém o valor 4?", lista.contem(4))

    # Obtém o índice de um valor na lista
    print("O índice do valor a é", lista.indice('a'))
    print("O índice do valor 4 é", lista.indice(4))

    # Obtém o tamanho da lista
    print("O tamanho da lista é", lista.tamanho_lista())

    # Obtém um elemento da lista
    print("O elemento na posição 1 é", lista.obtem_elemento(1))

    # Remove um valor da lista
    lista.remove('c')

    # Imprime a lista atualizada
    print("Lista atualizada: ", lista)

    # Verifica o tamanho atual
    print("O tamanho atual da lista", lista.tamanho_lista())

    # Limpa a lista
    lista.limpa_lista()

     # Verifica o tamanho da lista após limpar
    print("O tamanho da lista após limpar é", lista.tamanho_lista())