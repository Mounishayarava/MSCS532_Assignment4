# Heapsort Implementation
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    # See if left child exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l
    # See if right child exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)
def heapsort(arr):
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
# Example 
if __name__ == "__main__":
    sample = [15, 3, 17, 10, 84, 19, 6, 22, 9]
    print("Original array:", sample)
    heapsort(sample)
    print("Sorted array:  ", sample)
