from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)

def pop():
    return fifo.pop()


push(3)
push(10)
push(9)

print(pop())
print(pop())
print(pop())
