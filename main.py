#priority queue

class Queue:
  def __init__(self):
    self.fila = list()

  def enqueue(self, value, priority):
    if self.item.size() == 0:
      self.fila.append([priority, value])
    else:
      for i in range(self.item.size()):
        if self.fila[i][0] <= priority:
          self.fila.insert(i, [priority, value])
          return
    
  def size(self):
    return len(self.fila)


filinha = Queue() #MUDA ESSE NOME


while True:
  entradinha = input() #MUDA ESSE NOME
  if entradinha  == "stop":
    print(filinha.size(), " processo(s) órfão(s).")
    break

  elif entradinha == 