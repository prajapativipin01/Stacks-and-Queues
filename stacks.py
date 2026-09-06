# the operations in the stack
# Via defining array 
stack = []

stack.append(23)
stack.append(24)
stack.append("a")

print(stack)

# stack.clear()  clear the stack

# to check if the stack is empty or not 
stack.isEmpty()


# Object Oriented implementation

class Stack:

    def __init__(self):

        self._items = []  # create a private attribute to prevent external interference

    # insertion in stock 

    def insertion(self,item):

        # add item to the top 
        self._items.append(item)

    # Pop the element from the top
    def pop(self):

        if self.is_empty():  # condition if the stack is empty then return the index error
            raise IndexError
        return self._items.pop()

    # check that if the stack is empty or not

    def is_empty(self):

        return len(self._items) == 0  # no element in stack

    # get the peak element 

    def get_peak(self):
        # check that stack is empty or not 
        if self.is_empty():
            return None
        return self._items[-1]  # topmost element in the stack 

    # find the size of the stack
    def size(self):
         if self.is_empty():
             return 0
         return len(self._items)

    # for priniting
    def __str__(self):

        return f"stack :{self._items}"
    


stack = Stack()

stack.insertion(18)
stack.insertion(13)
stack.insertion(14)
stack.insertion(16)
stack.insertion(89)
stack.insertion(56)

# stack.pop()
# stack.pop()

# print(stack.is_empty())
print(stack)
print(stack.get_peak())
print(stack.size())



    


