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

#### **1. 自我介绍**

- 提及熟悉的技术栈（Golang、数据结构算法、网络、操作系统等）。
- 简要说明项目经验（如课程设计、开源项目、实习经历等）。

#### **2. 介绍一下你的项目**

- **项目名称** + **核心功能**（如高性能服务器）。
- **技术栈**（如 Golang 协程、Redis 缓存等）。
- **个人贡献**（如优化算法、解决并发问题、设计架构等）。
- **遇到的挑战** + **如何解决**（如内存泄漏、性能瓶颈等）。

#### **3. 口述反转链表算法**
**方法 1：迭代法（C++）**
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
**方法 2：递归法（Golang）**
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

#### **4. 深度优先（DFS） vs 广度优先（BFS）**
| **特性**       | **DFS（栈/递归）**          | **BFS（队列）**            |
|--------------|---------------------------|--------------------------|
| **遍历顺序**   | 一条路走到底，再回溯         | 逐层遍历                 |
| **空间复杂度** | O(h)（h=树高）             | O(w)（w=树最宽层的节点数） |
| **适用场景**   | 拓扑排序、连通性、回溯问题   | 最短路径、层级遍历       |

#### **5. 哈希表（Hash Table）**

- **底层原理**：数组 + 哈希函数（如取模），冲突解决（开放寻址、链地址法）。
- **时间复杂度**：
  - 插入/删除/查找：平均 O(1)，最坏 O(n)（哈希冲突严重时）。
- **Golang 的 `map`**：使用拉链法，动态扩容。
- **C++ 的 `unordered_map`**：基于哈希桶实现。

#### **6. 什么是死锁？**

- **定义**：多个进程/线程因竞争资源而互相等待，导致无法继续执行。
- **必要条件**（缺一不可）：
  1. **互斥条件**：资源一次只能被一个进程占用。
  2. **占有并等待**：进程持有资源并等待其他资源。
  3. **非抢占条件**：已分配的资源不能被强制剥夺。
  4. **循环等待**：存在一个进程的等待环。
- **解决方法**：
  - 破坏必要条件（如超时机制、资源预分配）。
  - 银行家算法（避免死锁）。

#### **7. 进程 vs 线程 vs 协程**
| **维度**     | **进程**               | **线程**               | **协程（Goroutine）**  |
|------------|-----------------------|-----------------------|-----------------------|
| **资源分配** | 独立内存空间（开销大）  | 共享进程内存（开销小）  | 用户态调度（极轻量）   |
| **切换成本** | 高（需内核介入）        | 中（内核调度）         | 低（用户态切换）       |
| **并发性**   | 多核并行               | 多核并行               | 单线程内高并发         |
| **示例**     | Chrome 多标签页        | Java 多线程            | Golang 的 Goroutine   |

#### **8. TCP vs UDP**
| **特性**       | **TCP（可靠）**          | **UDP（不可靠）**       |
|--------------|------------------------|-----------------------|
| **连接方式**   | 面向连接（三次握手）     | 无连接                |
| **可靠性**     | 保证数据顺序、不丢失     | 可能丢包、乱序        |
| **速度**       | 慢（重传、拥塞控制）     | 快（无额外控制）      |
| **应用场景**   | HTTP、FTP、数据库        | 视频流、游戏、DNS     |

#### **9. 虚拟内存**

- **作用**：
  - 扩展可用内存（通过磁盘交换）。
  - 隔离进程地址空间（提高安全性）。
- **核心机制**：
  - **分页**：内存划分为固定大小的页（如 4KB），由 MMU 管理。
  - **页表**：记录虚拟页到物理页的映射。
  - **缺页中断**：访问未加载的页时触发，从磁盘调入。
- **优点**：
  - 允许运行比物理内存更大的程序。
  - 避免进程间内存冲突。

---
