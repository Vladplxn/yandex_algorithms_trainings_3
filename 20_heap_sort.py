class MyHeap:
    def __init__(self):
        self.arr = []
    
    def insert(self, val):
        self.arr.append(val)
        pos = len(self.arr) - 1
        while pos > 0 and self.arr[pos] < self.arr[(pos - 1) // 2]:
            self.arr[pos], self.arr[(pos - 1) // 2] = self.arr[(pos - 1) // 2], self.arr[pos]
            pos = (pos - 1) // 2
    
    def extract(self):
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        pos = 0
        while 2 * pos + 2 < len(self.arr):
            min_son_idx = 2 * pos + 1
            if self.arr[2 * pos + 2] < self.arr[min_son_idx]:
                min_son_idx = 2 * pos + 2
            if self.arr[pos] > self.arr[min_son_idx]:
                self.arr[pos], self.arr[min_son_idx] = self.arr[min_son_idx], self.arr[pos]
                pos = min_son_idx
            else:
                break
        self.arr.pop()

        return ans


if __name__ == "__main__":
    heap = MyHeap()
    _ = int(input())
    vals = list(map(int, input().split()))

    for val in vals:
        heap.insert(val)
    
    for _ in range(len(vals)):
        print(heap.extract(), end=' ', sep='')