############################### 72 chars ###############################


class CircularQueue:
    """
    Circular Queue implemented as Array.

    Methods
    -------
    - enqueue(item)
      Adds item at the end of the queue.
    
    - dequeue()
      Returns the first item in the queue.
    """

    def __init__(self, size: int):
        # Delete the line below and write your code here
        self.data = [None] * size
        self.head = -1
        self.tail = -1
        self.size = size


    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, data) -> None:
        """
        Add item at the end of the queue.

        Arguments
        ---------
        - item
        The item to be added.

        Return: None
        """
        # Delete the line below and write your code here
        if self.isfull():
            raise ValueError('Queue is full')
        if self.isempty():
            self.head = 0
            self.tail = 0

        self.data[self.tail] = data
        if self.tail + 1 == self.size:
            self.tail = 0
        else:
            self.tail += 1
        return
            

    def dequeue(self) -> "item":
        """
        Return the item at the head of the queue.

        Arguments
        ---------
        None

        Return: item
        """
        # Delete the line below and write your code here
        if self.isempty():
          raise Exception("Queue is empty!")
        
        data = self.data[self.head]
        self.data[self.head] = None
        if self.head + 1 == self.size:
            self.head = 0
        else:
            self.head += 1
        return data

    def contains(self, item):
        for i in range(self.size):
            if self.data[i] == item:
                return True
        return False
    
    def isfull(self):
        return (self.tail + 1) % self.size == self.head
    def isempty(self):
        return self.head == -1
      
option = CircularQueue(5)
option.enqueue("hi")
option.enqueue("hi")
print(option.data[0])
option.dequeue()
print(option.data[0])