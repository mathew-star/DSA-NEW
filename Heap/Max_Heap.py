class MaxHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self._max_heapify(i)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._max_heapify(0)
        return max_val

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _max_heapify(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._max_heapify(largest)

# Example usage:
max_heap = MaxHeap()
max_heap.build_heap([4, 10, 3, 5, 1])
max_heap.insert(7)
print(max_heap.heap)  # Output: [10, 7, 3, 5, 1, 4]
print(max_heap.remove_max())  # Output: 10
print(max_heap.heap)  # Output: [7, 5, 3, 4, 1]
