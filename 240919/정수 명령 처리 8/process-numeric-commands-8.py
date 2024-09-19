class Node:
    def __init__(self, prv, nxt, value):
        self.prv = prv
        self.nxt = nxt
        self.value = value


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, value):
        if not self.length:
            node = Node(None, None, value)
            self.head = node
            self.tail = node
        else:
            node = Node(None, self.head, value)
            self.head.prv = node
            self.head = node

        self.length += 1
        return None

    def push_back(self, value):
        if not self.length:
            node = Node(None, None, value)
            self.head = node
            self.tail = node
        else:
            node = Node(self.tail, None, value)
            self.tail.nxt = node
            self.tail = node

        self.length += 1
        return None

    def pop_front(self):
        ex_head = self.head

        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.nxt

        self.length -= 1
        return ex_head.value

    def pop_back(self):
        ex_tail = self.tail

        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prv
            self.tail.nxt = None

        self.length -= 1
        return ex_tail.value


    def size(self):
        return self.length


    def empty(self):
        if not self.length:
            return 1

        return 0

    def front(self):
        return self.head.value

    def back(self):
        return self.tail.value


N = int(input())
dll = DLL()
for _ in range(N):
    _input = input().split()
    result = None

    if len(_input) > 1:
        instruction, value = _input
        value = int(value)

        result = getattr(dll, instruction)(value)
    else:
        instruction = _input[0]
        result = getattr(dll, instruction)()

    if result or result == 0:
        print(result)