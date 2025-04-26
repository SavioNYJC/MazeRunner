############################### 72 chars ###############################


class Node:
    """
    Represents a node in a linkedlist.

    Arguments
    ---------
    - data
      The data encapsulated in the node.

    Attributes
    ----------
    - next: Node | None
      The next node in the linkedlist, or None if the node is the tail.

    Methods
    -------
    - get() -> data
      Return the data stored in the node.
    """

    def __init__(self, data):
        # Replace the line below with your code
        self._data = data
        self.next = None 

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self):
        """Return the data stored in the node.

        Arguments
        ---------
        None

        Return: data
        """
        return self._data


class LinkedList:
    """
    Represents a sequence of data items.

    Arguments
    ---------
    None

    Attributes
    ----------
    None

    Methods
    -------
    - length() -> int
    - get(index) -> item
    - insert(index, item) -> None
    - append(item) -> None
    - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
        ---------
        None

        Return: int
        """
        # Replace the line below with your code
        
        node_count = 0
        current = self._head
        
        while current is not None:
          node_count += 1
          current = current.next
        
        return node_count
        

    def get(self, n: int) -> "item":
        """Returns item at n-th node.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: item

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        
        if n >= self.length():
          raise IndexError("Index out of range")

        current = self._head

        for i in range(n):
            current = current.next

        return current.get()
        

    def insert(self, n: int, item) -> None:
        """Insert item into linkedlist at position n.
        insert at head -> n == 0
        append -> n == length

        Arguments
        ---------
        - n: int
          sequence number of item to be inserted.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if n == self.length():
            append(item)
            return

        current = self._head

        if n == 0:
            new_node = Node(item)
            new_node.next = current
            self._head = new_node
            return

        if n == 1:
            new_node = Node(item)
            new_node.next = current.next
            current.next = new_node
            return

        
        for i in range(n - 1):
          current = current.next
        new_node = Node(item)
        new_node.next = current.next
        current.next = new_node

    def append(self, item) -> None:
        """Append item at the end of linkedlist.

        Arguments
        ---------
        - item
          The item to be appended.

        Returns: None
        """
        # Replace the line below with your code
        new_node = Node(item)
        
        if self._head == None:
            self._head = new_node
            return

        current = self._head

        while current.next is not None:
            current = current.next
        if self._head == None:
            self._head = new_node
        

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if n >= self.length():
            raise IndexError
        
        current = self._head

        for i in range(n):
            prev = current
            current = current.next
        
        prev.next = current.next
        current.next = None
        
       
    def contains(self, item) -> bool:
        """Checks whether an item is in the linkedlist and returns
        a boolean value to indicate the status of the search

        Arguments
        ---------
        - item
          The item to be searched for.

        Returns: True if item is found in the linkedlist,
        otherwise False
        """
        # Replace the line below with your code
        current = self._head
        for i in range(self.length()):
            if current.get() == item:
                return true
            current = current.next
        return False

    def index

list = LinkedList()
list.append("HI")
print(list.get(0))