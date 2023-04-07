class MyQueue:
    def __init__(self):
        self.arr = []
    
    def size(self):
        return len(self.arr)
    
    def push(self, n: int):
        self.arr.append(n)
        print('ok')
    
    def pop(self):
        if self.size() == 0:
            print('error')
            return
        val = self.arr.pop(0)
        print(val)
    
    def front(self):
        if self.size() == 0:
            print('error')
            return
        print(self.arr[0])
    
    def clear(self):
        self.arr = []
        print('ok')


if __name__ == "__main__":
    stack = MyQueue()

    while True:
        inp = input()
        if inp == 'exit':
            print('bye')
            break
        
        if inp.startswith('push'):
            stack.push(int(inp.split()[1]))
        elif inp == 'pop':
            stack.pop()
        elif inp == 'front':
            stack.front()
        elif inp == 'size':
            print(stack.size())
        elif inp == 'clear':
            stack.clear()