class MinHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self._min_heapify(i)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._min_heapify(0)
        return min_val

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _min_heapify(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._min_heapify(smallest)

min_heap = MinHeap()
min_heap.build_heap([4, 10, 3, 5, 1])
min_heap.insert(2)
print(min_heap.heap)  # Output: [2, 4, 3, 5, 1, 10]
print(min_heap.remove_min())  # Output: 2
print(min_heap.heap)  # Output: [3, 4, 10, 5, 1]
