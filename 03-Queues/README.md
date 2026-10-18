# Introduction to Queues

## 💡 Concept
A **Queue** is a linear data structure that follows a particular order in which operations are performed. The order is **FIFO (First-In-First-Out)**.

**Think of it like this:** Imagine a line of people waiting for a movie ticket. 
- The person who arrives first is at the front of the line.
- The first person in line is the first one to get the ticket and leave.
- New people join the line at the back.

Unlike a Stack (LIFO), where you interact only with the top, a Queue has two ends: the **Front** (where you remove elements) and the **Rear** (where you add elements).

### Why do we need Queues?
Queues are essential for managing tasks that need to be processed in the order they arrived:
- **Printer Spooling**: Documents sent to a printer are placed in a queue.
- **CPU Scheduling**: Processes waiting for CPU time are often managed in a queue.
- **Web Server Requests**: When thousands of people visit a website, the server processes requests in the order they were received.
- **Breadth-First Search (BFS)**: A fundamental graph algorithm that uses a queue to explore nodes level by level.

## ⚙️ Core Operations
A queue primarily supports these operations:
1. **Enqueue**: Adding an element to the rear (back) of the queue.
2. **Dequeue**: Removing the element from the front of the queue.
3. **Peek (Front)**: Looking at the element at the front without removing it.
4. **IsEmpty**: Checking if the queue has any elements.
5. **IsFull**: Checking if the queue has reached its maximum capacity (relevant for array-based queues).

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | We only add to the rear. |
| **Dequeue** | $O(1)$ | We only remove from the front. |
| **Peek** | $O(1)$ | Immediate access to the front element. |
| **Search** | $O(n)$ | In the worst case, we must check every element. |

**Space Complexity:** $O(n)$ to store $n$ elements.

---

## 🚀 Learning Path for Queues
In this section, we will cover:
1. **Operations**: Detailed look at Enqueue and Dequeue.
2. **Types**: Special queues like Circular, Double-Ended (Deque), and Priority Queues.
3. **Implementation**: How to build a queue using Arrays vs. Linked Lists.
