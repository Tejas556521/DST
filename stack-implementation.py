class Node:
  def __init__(self,x):
    self.data=x
    self.next=None

class Stack:
  def __init__(self):
    self.top=None

  def push(self):
    x=int(input("enter the element to be inserted into the stack"))
    new=Node(x)
    if self.top is None:
      self.top=new
      self.top.next=None
    else:
      new.next=self.top
      self.top=new
  def pop(self):
    if self.top is None:
      print("stack is empty")
    elif self.top.next is None:
     print("Popped Element is ",self.top.data)
     print("-------------------")
     self.top=None
    else:
     temp=self.top
     print("popped element is ",self.top.data)
     print("--------------------")
     self.top=temp.next
     temp=None

  def display(self):
    if self.top is None:
      print("stack is empty")
      print("----------------")
    else:
      print("elements of the stack are:")
      temp=self.top
      while temp:
        print(temp.data)
        temp=temp.next
      print("top of the stack is ",self.top.data)
      print("---------------")
s=Stack()
while(1):
  print("enter the operation:")
  print("1.Push Operation\n2.Pop Operation\n3.Display\n4.Exit")
  option=int(input())
  if option==1:
    print("push operation")
    s.push()
  elif option==2:
    print("pop operation")
    s.pop()
  elif option==3:
    print("display operation")
    s.display()
  elif option==4:
    print("exiting")
    break
  else:
    print("enter correct operation please")
