# create a linked_list
# https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Linked_List:
    def __init__(self):
        self.length = 0
        self.head = None

    # def print_backward(self):
    #     print('[', end=' ')
    #     if self.head is not None:
    #         self.head.print_backward()

    def traverse_list(self):
        if self.head is None:
            return print('No element in the list.')
        else:
            n=self.head
            while n is not None:
                print(n)
                n=n.next

    def insert_at_start(self,data):
        if self.head is None:
            self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n=n.next
            n.next=new_node


