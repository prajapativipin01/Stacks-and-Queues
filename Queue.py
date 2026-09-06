# Array implement of queue 

class Queue:

    def __init__(self):

        # decalre an array of finite size
        self.arr = [0] * 10

       
        self.start = -1    # track index of the front element 
        self.end  = -1     # track index of the end element 
        self.currsize = 0      # current no. of element in queue
        self.maxcapacity = 10 # max no of element can remain in queue



    # Enqueue : insert element at front : push

    def push(self, x):

        # check that if the queue is full 
        if self.currsize == self.maxcapacity:

            print(" queue is full \n exiting ")
            exit(1)

        # if queue is empty
        if self.end == -1:
            self.start = 0
            self.end = 0

        else:

            self.end = (self.end + 1) % self.maxcapacity # circular increase of end 

        self.arr[self.end] = x
        self.currsize = self.currsize + 1

    # Dequeue : delete element from queue : pop

    def pop(self):

        # check that if the queue is empty or not
        if self.currsize == 0:

            print(" queue is empty\n exiting")
            exit(1)

        popped = self.arr[self.start]

        # if there is one element in queue

        if self.currsize == 1:

            self.start = -1
            self.end  = -1

        else:

            self.start = (self.start + 1) % self.maxcapacity

        self.currsize = self.currsize - 1
        return popped

    # Peek operation 

    def peek(self):

        if self.start == -1: # if the queue is empty then return

            print("queue is empty\n existing")
            exit(1)

        else:

            return self.arr[self.start]


    # check that queue is empty

    def isEmpty(self):

        return self.currsize == 0

    def display(self):

        if self.currsize == 0:
            return "[]"

        elements = []

        idx = self.start

        for _ in range(self.currsize):

            elements.append(self.arr[idx])
            idx = (idx + 1) % self.maxcapacity

        print(elements)
        
        


if __name__ == "__main__":

    queue = Queue()

    queue.push(12)
    queue.push(133)
    queue.push("vipin")
    queue.push(78)
    queue.push(42)


    queue.display()

    queue.pop()
    queue.display()

    print(queue.peek())
    print(queue.isEmpty())