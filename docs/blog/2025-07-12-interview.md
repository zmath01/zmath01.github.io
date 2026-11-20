# Interview

Q&A

<!--more-->

## Puzzles

### 1. Poison and Rat

In this idealized coding puzzle, one of 1,000 bottles is poisoned, and each test has two possible outcomes after one hour. How many simultaneous tests distinguish all the bottles?

Ten tests are necessary and sufficient because $2^9<1000\le 2^{10}$. Label the bottles 1 through 1,000 and assign one test to each bit position. Include a bottle in a test when its corresponding bit is set. For example, positive results at zero-based bit positions 1, 3, and 5 identify bottle $2^1+2^3+2^5=42$.

------

## Concurrency Programming

Concurrent programming lets tasks make progress during overlapping periods. Parallel execution additionally runs work at the same time.

Three common approaches that offer different trade-offs in terms of performance, complexity, and resource usage:

- multi-processing
- multi-threading
- coroutines

------

## Interview Answers

#### **1. Self-introduction**

- Mention the familiar technology stack (Go, data structure algorithm, network, operating system, etc.).
- Briefly describe project experience (such as course design, open source projects, internship experience, etc.).

#### **2. Introduce your project**

- **Project name** + **Core functions** (such as high-performance server).
- **Technology stack** (such as Go coroutine, Redis cache, etc.).
- **Personal contribution** (such as optimizing algorithms, solving concurrency problems, designing architecture, etc.).
- **Challenges encountered** + **How to solve** (such as memory leaks, performance bottlenecks, etc.).

#### **3. Reverse a linked list**

The snippets assume a conventional singly linked `ListNode` type.
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
**Method 2: Recursive method (Go)**
```go
func reverseList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    newHead := reverseList(head.Next)
    head.Next.Next = head
    head.Next = nil
    return newHead
}
```

#### **4. Depth-first (DFS) vs Breadth-first (BFS)**
| **Features** | **DFS (stack/recursion)** | **BFS (queue)** |
|--------------|---------------------------|--------------------------|
| **Traversal order** | Go to the end of a road and then backtrack | Traverse layer by layer |
| **Space complexity** | $O(h)$ stack for recursive tree DFS, where $h$ is height | $O(w)$ queue for tree BFS, where $w$ is maximum level width |
| **Applicable scenarios** | Topological sorting, connectivity, backtracking problems | Shortest path in an unweighted graph, hierarchical traversal |

For general graph traversal, visited-node bookkeeping can take $O(V)$ space.

#### **5. Hash Table**

- **Underlying principle**: array + hash function (such as modulus), conflict resolution (open addressing, chain address method).
- **Time complexity**:
- Insert/delete/search: average O(1), worst O(n) (when hash conflict is serious).
- Go’s built-in `map` is a hash table. The runtime introduced a [Swiss Table implementation in Go 1.24](https://go.dev/blog/swisstable).
- **C++'s `unordered_map`**: implemented based on hash buckets.

#### **6. What is deadlock?**

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
| **Parallelism** | Multiple processes can run on separate cores | Multiple threads can run on separate cores | Go can schedule goroutines across multiple OS threads |
| **Example** | Chrome Multi-tabs | Java Multi-threading | Go's Goroutine |

#### **8. TCP vs UDP**

| **Features** | **TCP (Reliable)** | **UDP (Unreliable)** |
|--------------|------------------------|-----------------------|
| **Connection Method** | Connection-oriented (three-way handshake) | Connectionless |
| **Reliability** | Reliable, ordered byte stream. A failed connection can interrupt delivery. | Possible packet loss and disorder |
| **Speed** | Retransmission and congestion control add overhead | Low protocol overhead. Applications can add reliability or congestion control. |
| **Application scenarios** | HTTP/1.1, HTTP/2, FTP | QUIC (including HTTP/3), games, most DNS queries |

#### **9. Virtual memory**

- **Function**:
- Expand available memory (through disk swap).
- Isolate process address space (improve security).
- **Core mechanism**:
- **Paging**: Memory is divided into fixed-size pages (such as 4KB), managed by MMU.
- **Page table**: Records the mapping of virtual pages to physical pages.
- **Page fault interrupt**: A fault can require allocating a new page, loading a page from storage, or rejecting an invalid access.
- **Advantages**:
- Allows running programs larger than physical memory.
- Avoid memory conflicts between processes.
