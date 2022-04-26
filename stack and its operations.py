# last in first out(lifo)
# push to insect the element and pop to delete the element

def stack_using_list():
    stack = []
    stack.append("Data Structures")
    stack.append("using")
    stack.append("python by list")
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)


# stack_using_list()


def stack_using_deque():
    from collections import deque
    stack = deque()
    stack.append("Data Structures")
    stack.append("using")
    stack.append("python by deque")
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)


# stack_using_deque()


def stack_using_queue():
    from queue import LifoQueue
    stack = LifoQueue(maxsize=5)
    stack.put(1)
    stack.put(2)
    stack.put(3)
    stack.put(4)
    stack.put(5)
    print(stack.full())
    stack.get()
    stack.get()
    print(stack.full())


stack_using_queue()
