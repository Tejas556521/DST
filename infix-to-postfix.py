Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_operator(char):
...     return char in {'+', '-', '*', '/'}
... 
... def precedence(operator):
...     if operator == '+' or operator == '-':
...         return 1
...     elif operator == '*' or operator == '/':
...         return 2
...     else:
...         return 0
... 
... def infix_to_postfix(infix_expression):
...     stack = []
...     postfix_expression = []
... 
...     for char in infix_expression:
...         if char.isalnum():
...             postfix_expression.append(char)
...         elif char == '(':
...             stack.append(char)
...         elif char == ')':
...             while stack and stack[-1] != '(':
...                 postfix_expression.append(stack.pop())
...             stack.pop()  
...         elif is_operator(char):
...             while stack and precedence(stack[-1]) >= precedence(char):
...                 postfix_expression.append(stack.pop())
...             stack.append(char)
... 
...         postfix_expression.append(stack.pop())
... 
...     return ''.join(postfix_expression)
... 
... infix_expression = "(a+b)*c+d"
... postfix_expression = infix_to_postfix(infix_expression)
... print("Infix Expression:", infix_expression)
