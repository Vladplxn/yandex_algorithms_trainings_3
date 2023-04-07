class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def size(self):
        return self.len
    
    def push_front(self, n: int):
        node = Node(n)
        if self.size() == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.len += 1
        print('ok')
    
    def push_back(self, n: int):
        node = Node(n)
        if self.size() == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.len += 1
        print('ok')
    
    def pop_front(self):
        if self.size() == 0:
            print('error')
            return
        val = self.head.val
        self.head = self.head.next
        self.len -= 1
        print(val)
    
    def pop_back(self):
        if self.size() == 0:
            print('error')
            return
        val = self.tail.val
        self.tail = self.tail.prev
        self.len -= 1
        print(val)

    def front(self):
        if self.size() == 0:
            print('error')
            return
        val = self.head.val
        print(val)
    
    def back(self):
        if self.size() == 0:
            print('error')
            return
        val = self.tail.val
        print(val)

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0
        print('ok')


if __name__ == "__main__":
    deque = MyDeque()

    while True:
        inp = input()
        if inp == 'exit':
            print('bye')
            break
        
        if inp.startswith('push_front'):
            deque.push_front(int(inp.split()[1]))
        elif inp.startswith('push_back'):
            deque.push_back(int(inp.split()[1]))
        elif inp == 'pop_front':
            deque.pop_front()
        elif inp == 'pop_back':
            deque.pop_back()
        elif inp == 'front':
            deque.front()
        elif inp == 'back':
            deque.back()
        elif inp == 'size':
            print(deque.size())
        elif inp == 'clear':
            deque.clear()