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