import heapq

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):  # For min-heap ordering
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

# Priority Queue with min-heap
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_min(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def decrease_key(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                task.priority = new_priority
                heapq.heapify(self.heap)
                return

    def is_empty(self):
        return len(self.heap) == 0

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task("A", 3, 0, 10))
    pq.insert(Task("B", 1, 2, 12))
    pq.insert(Task("C", 2, 1, 11))

    print("Initial Queue:", pq.heap)
    print("Extracted:", pq.extract_min())
    print("Queue After Extraction:", pq.heap)
