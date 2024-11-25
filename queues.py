user_input = "yes"

class Queue(): # A class is basically a blueprint / a template.
  
  def __init__(self,size): # We take self beause it just needs it as every object has attributes.
    # Instantiation is the process of creating an object instance from a class template.
    # This init method is a constructor method.
    # The size attribute will set the size of the list.
    self.front = 0
    self.rear = -1
    self.size = 0
    self.maxSize = size # The maximum length of the queue will be equal to its size.
    self.q = [-1] * size

  def isEmpty(self): # We must use self.
    return self.size == 0 # True will be returned if the size is equal to zero.

  def isFull(self):
    return self.size == self.maxSize # True will be returned if the size is equal to the maaxsize of the list.

  #Pseudocode for a procedure
  def enqueue(self, newItem):
    if self.isFull():
      print("Queue full")
    else:
      self.rear = (self.rear + 1) % self.maxSize
      self.q[self.rear] = newItem
      size = self.size + 1

  def dequeue(self):
    if self.size == 0:
      print("The queue is empty")
    else:
      print("hi")

  def print_queue():
    print(myQ.q)
    print(myQ.rear)


myQ = Queue(5) # init an instance of a queue

while user_input != "no":
  user_input = input("Say yes to print the queue and the rear pointer")
  if user_input == "yes" or "Yes":
    print_queue()
  else:
    user_input == "no"
  