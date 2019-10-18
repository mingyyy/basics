# implement a stack


class stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        else:
            x=self.stack.pop()
            return f"{x} was removed from the stack"

    def push(self, data):
        self.stack.append(data)
        return f'{data} was pushed to the stack'

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        else:
            x=self.stack[-1:]
            return f'{x} is on top of the stack'


class Queue:
    def __init__(self):
        self.q = []

    def __str__(self):
        return f'{self.q}'

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if len(self.q) == 0:
            return 'Empty queue'
        else:
            self.q.pop(0)

my_queue = Queue()
my_queue.enqueue('1')
my_queue.enqueue('2')
my_queue.enqueue('3')

print(my_queue)
my_queue.dequeue()
print(my_queue)



# Easy python solution
# import queue
#
# q = queue.Queue()
# for i in range(5):
#     q.put(i)
#
# while not q.empty():
#     print(q.get())

