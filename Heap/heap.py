class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def delete(self, item):
        if len(self.heap) == 0:
            return False

        index = self.heap.index(item)
        self.heap[index] = self.heap[-1]
        self.heap.pop()

        if index < len(self.heap):
            self.heapify_down(index)

        return True

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def is_empty(self):
        return len(self.heap) == 0
    
    ### Heap testing code

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)

print(heap.get_min())  # Output: 1

heap.delete(3)
print(heap.get_min())  # Output: 1