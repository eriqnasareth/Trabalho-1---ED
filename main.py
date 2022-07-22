############# Priority queue ########
class Deque:
  
  # Construtor da lista 
  def __init__(self): 
    self.fila = list()

    
  # Adiciona o valor na lista com relacao a sua prio
  def enqueue(self, value, priority):
    #Se o tam for 0, adiciona o primeiro valor
    priority = int(priority)
    if len(self.fila) == 0: 
      self.fila.append([priority, value])

    #Else, adiciona no local seguindo ordem
    else:
      for i in range(len(self.fila)):
        if self.fila[i][0] <= priority:
          self.fila.insert(i, [priority, value])
          return

          
  # Retorna o tamanho atual da lista
  def size(self):
    return len(self.fila)

  
  def dequeue(self):
    #Remove o prox valor da fila
    return self.fila.pop()

  def teste(self):
    print(self.fila)
    

################# dekey ##############
    
def dekey(S):
  chave = S[0]
  S = S[1:]
  newS = str()
  
  for i in range(int(chave)):
    #A < B
    if S[0] < S[1]:
      S.append(S.pop(0))
    #B >= A
    else:
      S.append(S.pop(1))

  for i in S:
    newS += i
  return newS

################## scramble #############
def scramble(C):
  
  newC = str()
  listC = list()
  ordem = "("
  
  for i in C:
    if i == "(" or i == ")":
      ordem = i
    if ordem == "(" and (i != "(" and i != ")"):
      listC.insert(0, i)
    elif ordem == ")" and (i != "(" and i != ")"):
      listC.append(i)

  for i in listC:
    newC += i
    
  return newC

  
################ MAIN #################
processos = Deque()

while True:
  comando = input()
  print()
  #Stop
  if comando == "stop":
    print(processos.size(), "processo(s) órfão(s).")
    break

  #Go
  if comando == "go":
    if processos.size() != 0:
      print(processos.dequeue()[1])      
    
  #Enqueue
  else:
    comando = comando.split(" ")
    
    for i in range(int(comando[1])):
      x = input().split(" ")
      #Dekey
      if x[1] == "dekey":
        processos.enqueue(dekey(x[2:]), x[0])

      elif x[1] == "scramble":
        processos.enqueue(scramble(x[2:]), x[0])
      
      