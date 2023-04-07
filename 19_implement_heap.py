class MyHeap:
    def __init__(self):
        self.arr = []
    
    def insert(self, val):
        self.arr.append(val)
        pos = len(self.arr) - 1
        while pos > 0 and self.arr[pos] > self.arr[(pos - 1) // 2]:
            self.arr[pos], self.arr[(pos - 1) // 2] = self.arr[(pos - 1) // 2], self.arr[pos]
            pos = (pos - 1) // 2
    
    def extract(self):
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        pos = 0
        while 2 * pos + 2 < len(self.arr):
            max_son_idx = 2 * pos + 1
            if self.arr[2 * pos + 2] > self.arr[max_son_idx]:
                max_son_idx = 2 * pos + 2
            if self.arr[pos] < self.arr[max_son_idx]:
                self.arr[pos], self.arr[max_son_idx] = self.arr[max_son_idx], self.arr[pos]
                pos = max_son_idx
            else:
                break
        self.arr.pop()

        return ans


if __name__ == "__main__":
    heap = MyHeap()
    n = int(input())
    for _ in range(n):
        inp = input()
        if inp.startswith('0'):
            heap.insert(int(inp.split()[1]))
        elif inp == '1':
            print(heap.extract())