# Interview

Q&A

<!--more-->

## Puzzles

### 1. Poison and Rat

There are 1000 wine bottles. One of the bottles contains poisoned wine. A rat dies after one hour of drinking the poisoned wine. How many minimum rats are needed to figure out which bottle contains poison in hour.

Solution:
We need to figure out in hour. We need 10 rats to figure out the poisoned bottle. The result is based on binary number system. We get 10 using $log_{2}{1000}$

The idea is to number bottles from 1 to 1000 and write their corresponding binary numbers on the bottle. Each rat is assigned a position in the binary numbers written on bottles. Let us take an example. Rat 1 represents first bit in every bottle, rat 2 represents second bit and so on. If rat numbers 5, 7 and 9 die, then bottle number 42 (Binary 0000101010) is poisoned.

------

## Concurrency Programming

// low-cost

Concurrency programming involves various techniques to manage multiple tasks simultaneously;

Choosing the right approach depends on the specific requirements of the application;

Three common approaches that offer different trade-offs in terms of performance, complexity, and resource usage:

- multi-processing
- multi-threading
- coroutines

------

English Version

## Interview Answers

#### **1. Self-introduction**

- Mention the familiar technology stack (Golang, data structure algorithm, network, operating system, etc.).
- Briefly describe project experience (such as course design, open source projects, internship experience, etc.).

#### **2. Introduce your project**

- **Project name** + **Core functions** (such as high-performance server).
- **Technology stack** (such as Golang coroutine, Redis cache, etc.).
- **Personal contribution** (such as optimizing algorithms, solving concurrency problems, designing architecture, etc.).
- **Challenges encountered** + **How to solve** (such as memory leaks, performance bottlenecks, etc.).

#### **3. Verbal reverse list algorithm**
**Method 1: Iterative method (C++)**
```cpp
ListNode* reverseList(ListNode* head) {
ListNode *prev = nullptr, *curr = head;
while (curr) {
ListNode *next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}
return prev;
}
```
**Method 2: Recursive method (Golang)**
```go
func reverseList(head *ListNode) *ListNode {
if head == nil || head.Next == nil {
return head
}
newHead := reverseList(head. Next)
head.Next.Next = head
head. Next = nil
return newHead
}
```

#### **4. Depth-first (DFS) vs Breadth-first (BFS)**
| **Features** | **DFS (stack/recursion)** | **BFS (queue)** |
|--------------|---------------------------|--------------------------|
| **Traversal order** | Go to the end of a road and then backtrack | Traverse layer by layer |
| **Space complexity** | O(h) (h=tree height) | O(w) (w=number of nodes in the widest layer of the tree) |
| **Applicable scenarios** | Topological sorting, connectivity, backtracking problems | Shortest path, hierarchical traversal |

#### **5. Hash Table**

- **Underlying principle**: array + hash function (such as modulus), conflict resolution (open addressing, chain address method).
- **Time complexity**:
- Insert/delete/search: average O(1), worst O(n) (when hash conflict is serious).
- **Golang's `map`**: use the zipper method and dynamically expand capacity.
- **C++'s `unordered_map`**: implemented based on hash buckets.

#### **6. What is deadlock? **

- **Definition**: Multiple processes/threads wait for each other due to competing resources, resulting in inability to continue execution.
- **Necessary conditions** (none of which can be missing):
1. **Mutually exclusive condition**: Resources can only be occupied by one process at a time.
2. **Possess and wait**: The process holds resources and waits for other resources.
3. **Non-preemptive condition**: Allocated resources cannot be forcibly deprived.
4. **Loop wait**: There is a waiting loop for a process.
- **Solution**:
- Destroy necessary conditions (such as timeout mechanism, resource pre-allocation).
- Banker's algorithm (avoid deadlock).

#### **7. Process vs Thread vs Coroutine**
| **Dimension** | **Process** | **Thread** | **Coroutine (Goroutine)** |
|------------|-----------------------|-----------------------|-----------------------|
| **Resource Allocation** | Independent Memory Space (High Overhead) | Shared Process Memory (Low Overhead) | User Mode Scheduling (Extremely Lightweight) |
| **Switching Cost** | High (Kernel Intervention Required) | Medium (Kernel Scheduling) | Low (User Mode Switching) |
| **Concurrency** | Multi-core Parallelism | Multi-core Parallelism | High Concurrency in a Single Thread |
| **Example** | Chrome Multi-tabs | Java Multi-threading | Golang's Goroutine |

#### **8. TCP vs UDP**
| **Features** | **TCP (Reliable)** | **UDP (Unreliable)** |
|--------------|------------------------|-----------------------|
| **Connection Method** | Connection-oriented (three-way handshake) | Connectionless |
| **Reliability** | Guarantee data order and no loss | Possible packet loss and disorder |
| **Speed** | Slow (retransmission, congestion control) | Fast (no additional control) |
| **Application scenarios** | HTTP, FTP, database | Video streaming, games, DNS |

#### **9. Virtual memory**

- **Function**:
- Expand available memory (through disk swap).
- Isolate process address space (improve security).
- **Core mechanism**:
- **Paging**: Memory is divided into fixed-size pages (such as 4KB), managed by MMU.
- **Page table**: Records the mapping of virtual pages to physical pages.
- **Page fault interrupt**: Triggered when accessing an unloaded page, loaded from disk.
- **Advantages**:
- Allows running programs larger than physical memory.
- Avoid memory conflicts between processes.

---

Chinese Version

#### **1. Self-introduction**

- Mention the familiar technology stack (Golang, data structures and algorithms, networking, operating systems, etc.).
- Briefly describe project experience (such as course projects, open-source projects, internships, etc.).

#### **2. Introduce your project**

- **Project name** + **Core functions** (e.g., high-performance server).
- **Technology stack** (e.g., Golang coroutines, Redis cache, etc.).
- **Personal contribution** (e.g., algorithm optimization, solving concurrency issues, designing architecture, etc.).
- **Challenges encountered** + **How to solve** (e.g., memory leaks, performance bottlenecks, etc.).

#### **3. Verbal reverse linked list algorithm**
**Method 1: Iterative method (C++)**
```cpp
ListNode* reverseList(ListNode* head) {
    ListNode *prev = nullptr, *curr = head;
    while (curr) {
        ListNode *next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```
**Method 2: Recursive method (Golang)**
```go
func reverseList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    newHead := reverseList(head. Next)
    head.Next.Next = head
    head. Next = nil
    return newHead
}
```

#### **4. Depth-first (DFS) vs Breadth-first (BFS)**
| **Features** | **DFS (stack/recursion)** | **BFS (queue)** |
|--------------|---------------------------|--------------------------|
| **Traversal order** | Go all the way down one path, then backtrack | Traverse layer by layer |
| **Space complexity** | O(h) (h = tree height) | O(w) (w = number of nodes in the widest layer of the tree) |
| **Applicable scenarios** | Topological sorting, connectivity, backtracking problems | Shortest path, hierarchical traversal |

#### **5. Hash Table**

- **Underlying principle**: array + hash function (e.g., modulo), conflict resolution (open addressing, separate chaining).
- **Time complexity**:
  - Insert/delete/search: average O(1), worst O(n) (when hash collisions are severe).
- **Golang's `map`**: uses the zipper method (separate chaining) and dynamically expands capacity.
- **C++'s `unordered_map`**: implemented based on hash buckets.

#### **6. What is deadlock?**

- **Definition**: Multiple processes/threads wait for each other due to competition for resources, resulting in the inability to continue execution.
- **Necessary conditions** (none can be missing):
  1. **Mutual exclusion condition**: A resource can only be occupied by one process at a time.
  2. **Hold and wait**: A process holds resources while waiting for other resources.
  3. **No preemption condition**: Allocated resources cannot be forcibly taken away.
  4. **Circular wait**: There exists a waiting cycle among processes.
- **Solutions**:
  - Break the necessary conditions (e.g., timeout mechanisms, resource pre-allocation).
  - Banker's algorithm (to avoid deadlock).

#### **7. Process vs Thread vs Coroutine**
| **Dimension** | **Process** | **Thread** | **Coroutine (Goroutine)** |
|------------|-----------------------|-----------------------|-----------------------|
| **Resource allocation** | Independent memory space (high overhead) | Shared process memory (low overhead) | User-mode scheduling (extremely lightweight) |
| **Switching cost** | High (requires kernel intervention) | Medium (kernel scheduling) | Low (user-mode switching) |
| **Concurrency** | Multi-core parallelism | Multi-core parallelism | High concurrency within a single thread |
| **Example** | Chrome multi-tabs | Java multi-threading | Golang's Goroutine |

#### **8. TCP vs UDP**
| **Features** | **TCP (reliable)** | **UDP (unreliable)** |
|--------------|------------------------|-----------------------|
| **Connection method** | Connection-oriented (three-way handshake) | Connectionless |
| **Reliability** | Guarantees data order and no loss | Possible packet loss and disorder |
| **Speed** | Slow (retransmission, congestion control) | Fast (no additional control) |
| **Application scenarios** | HTTP, FTP, database | Video streaming, games, DNS |

#### **9. Virtual memory**

- **Functions**:
  - Expand available memory (through disk swapping).
  - Isolate process address spaces (improve security).
- **Core mechanisms**:
  - **Paging**: Memory is divided into fixed-size pages (e.g., 4KB), managed by the MMU.
  - **Page table**: Records the mapping from virtual pages to physical pages.
  - **Page fault interrupt**: Triggered when accessing an unloaded page; loaded from disk.
- **Advantages**:
  - Allows running programs larger than physical memory.
  - Avoids memory conflicts between processes.

---
