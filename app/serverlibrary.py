

def mergesort(arr, key):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    print(arr)
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left, key)
    mergesort(right, key)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


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

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  operator = '+-*/()'
  
  def __init__(self, string=""):
        self._expression = string
  @property
  def expression(self):
        return self._expression
  @expression.setter
  def expression(self,expr):        
        for char in self._expression:
            if char not in EvaluateExpression.valid_char:
                self._expression = ""
            else:
                self._expression = expr
        pass
    
  def insert_space(self):
    self._expression = " ".join(self._expression)
    list1 = self._expression.split()
    for i in range(len(list1)):
        if list1[i] in EvaluateExpression.operator:
            new_length  =len(list1[i]) + 2
            list1[i] = list1[i].center(new_length)
    self._expression = "".join(list1)          
    pass

  def process_operator(self, operand_stack, operator_stack):
    op1= operand_stack.pop()
    op2= operand_stack.pop()
    if operator_stack.peek() == "+":
        operator_stack.pop()
        return operand_stack.push(op2 + op1)
    
    elif operator_stack.peek() == "-":
        operator_stack.pop()
        return operand_stack.push(op2 - op1)
    
    elif operator_stack.peek() == "*":
        operator_stack.pop()
        return operand_stack.push(op2 * op1)
    
    elif operator_stack.peek() == "/":
        operator_stack.pop()
        return operand_stack.push(op2 // op1)
    else: return 0
    


class EvaluateExpression:
    # copy the other definitions
    # from the previous parts
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self.expression = string

    @property
    def expression(self):
        return self._expr

    @expression.setter
    def expression(self, new_expr):
        if isinstance(new_expr, str):
            x = ''.join([i for i in new_expr if i in self.valid_char])
            if x == new_expr:
                self._expr = x
            else:
                self._expr = ""

    def insert_space(self):
        e = "+-*/()"
        r = list(map(lambda x: ' '+x+' ' if x in e else x, self.expression))
        return ''.join(r)

    def process_operator(self, operand_stack, operator_stack):
        #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items}")
        
        opr = operator_stack.pop()
        #print(f"opr={opr}")
        if opr == "(":
            return
        
        op1 = operand_stack.pop()
        op2 = operand_stack.pop()
        #print(f"{op1} {opr} {op2}")
        #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items}")
        
        if opr == "+":
            operand_stack.push(op2 + op1)
        elif opr == "-":
            operand_stack.push(op2 - op1)
        elif opr == "*":
            operand_stack.push(op2 * op1)
        elif opr == "/":
            operand_stack.push(op2 // op1)


    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        #print(f"{tokens} | {expression}")
        #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items}")
        
        for i in tokens:
            #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items} for {i}")
            if i in "0123456789":
                #print("number")
                operand_stack.push(int(i))
            if i in "+-":
                #print("+-")
                while not operator_stack.is_empty and operator_stack.peek() not in ['(', ')', None]:
                    #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items} for {i} +- while")
                    #print(f"{operator_stack.is_empty} | {operand_stack.peek()} for {i} +- while")
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(i)
                #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items} for {i} +-")
                
            if i in "*/":
                #print("*/")
                op = operator_stack.peek()
                #print(f"op={op}")
                while op in ['*', '/'] and op != "(" and op != None:
                    #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items} for {i} */ while")
                    self.process_operator(operand_stack, operator_stack)
                    op = operator_stack.peek()
                    #print(f"op={op} while")
                operator_stack.push(i)
                #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items} for {i} */ aft while")
            if i == '(':
                #print("(")
                operator_stack.push(i)
            if i == ')':
                #print(")")
                
                while operator_stack.peek() not in ['(', None] or not operator_stack.is_empty:
                    #print(f"{operator_stack._Stack__items} | {operand_stack._Stack__items} for {i} ) while")
                    #print(f"{operator_stack.peek()} | {not operator_stack.is_empty} || {operator_stack.peek() != '(' or not operator_stack.is_empty}")
                    self.process_operator(operand_stack, operator_stack)
                    operator_stack.pop()
        
        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        
        return operand_stack.pop()
    

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:100]









