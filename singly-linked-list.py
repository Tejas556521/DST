class Node:
  def __init__(self, data):
    self.data = data
    self.ref = None
node1 = Node (10)

# traversal of linked list
class Linkedlist:
  def __init__(self):
    self.head = None
  def print_LL(self):
    if self.head is None:
      print("linked list is empty")
    else:
      n = self.head
      while n is not None:
        print(n.data,"-->", end="")
        n = n.ref
# insertion at the beginning
  def add_begin(self, data):
   new_node = Node(data)
   new_node.ref = self.head
   self.head = new_node
# insertion at the end
  def add_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      n = self.head
      while n.ref is not None:
       n = n.ref
      n.ref = new_node
# insertion inbetween
  def add_after(self, data, X):
   n = self.head
   while n is not None:
    if X == n.data:
      break
    n= n.ref
   if n is None:
    print("node is not present in LL")
   else:
    new_node = Node(data)
    new_node.ref = n.ref
    n.ref = new_node
# deletion at beginning
  def delete_begin(self):
   if self.head is None:
    print("LL is empty so we can't delete nodes")
   else:
    self.head = self.head.ref
# deletion at end
  def delete_end(self):
   if self.head is None:
    print("LL is empty can't delete nodes")
   else:
    n = self.head
    while n.ref.ref is not None:
      n = n.ref
    n.ref = None
LL1 = Linkedlist()
LL1.add_begin(20)
LL1.add_begin(10)
LL1.add_after(50,10)
LL1.add_end(100)
LL1.delete_begin()
LL1.delete_end()
LL1.print_LL()
