class MyStack:
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
        val = self.arr.pop()
        print(val)
    
    def back(self):
        if self.size() == 0:
            print('error')
            return
        print(self.arr[-1])
    
    def clear(self):
        self.arr = []
        print('ok')


if __name__ == "__main__":
    stack = MyStack()

    while True:
        inp = input()
        if inp == 'exit':
            print('bye')
            break
        
        if inp.startswith('push'):
            stack.push(int(inp.split()[1]))
        elif inp == 'pop':
            stack.pop()
        elif inp == 'back':
            stack.back()
        elif inp == 'size':
            print(stack.size())
        elif inp == 'clear':
            stack.clear()