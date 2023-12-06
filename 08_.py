from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)

def pop():
    return lifo.popleft()



push(3)
push(10)
push(9)

print(pop())
print(pop())
print(pop())
