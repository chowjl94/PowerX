class Stack:
  def __init__(self):
    self.__items = []
        
  def push(self, item):
    self.__items.append(item)
    pass

  def pop(self):
    if not self.is_empty:
      return self.__items.pop()
    pass

  def peek(self):
    if not self.is_empty:
      return self.__items[-1]
    pass

  @property
  def is_empty(self):
    return self.__items == []
  pass

  @property
  def size(self):
    return len(self.__items)

obj =Stack()
obj.push(4)
#print(obj.__items)
print(obj._Stack__items)
