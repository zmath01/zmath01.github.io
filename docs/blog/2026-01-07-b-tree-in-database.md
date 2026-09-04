# B+ Tree in Database

数据库 ( 比如 MySQL ) 中绝大多数索引（包括主键索引、普通索引、联合索引）的底层实现都是 **B+ 树（B+ Tree）**，一种**平衡多路查找树**，而非数组。

<!--more-->

-

The Core Data Structure of Indexes is B+ Tree (Not Array)

The underlying implementation of most indexes in MySQL (including primary key indexes, normal indexes, and composite indexes) is a **B+ Tree**, a **balanced multi-way search tree** specifically designed for database indexes, not an array. 

The core reasons why arrays are not suitable as the core structure of indexes are:

- If the array is **unordered**: Queries require full traversal (time complexity $O(n)$), which completely defeats the purpose of an index;
- If the array is **ordered**: Queries can use binary search ($O(logn)$), but inserts/deletions require moving a large number of elements ($O(n)$), which is less efficient than B+ Trees.

### Why Do B+ Trees Speed Up Queries?

The structural characteristics of B+ Trees are perfectly suited to database query scenarios:

1. **Orderliness + Hierarchical Indexing**: All nodes of a B+ Tree are arranged in order by key values (index field values). The hierarchical structure from root node → branch node → leaf node can quickly locate data positions (e.g., to find data with `id=100`, there is no need to traverse the entire table; you only need to search down from the root node, with a stable time complexity of $O(logn)$);
2. **Leaf Nodes Linked in a Chain**: Pointers (or values) to all data rows are stored in leaf nodes, and leaf nodes are connected in a linked list, which is ideal for range queries (e.g., `create_time > '2024-01-01'`);
3. **Disk-Friendly**: The node size of a B+ Tree is adapted to disk blocks, reducing the number of disk I/O operations (the bottleneck of database operations is mainly disk I/O, not in-memory computation).

In comparison with arrays: Even an ordered array has binary search efficiency close to that of a B+ Tree, but arrays cannot efficiently support range queries and cannot adapt to the block storage characteristics of disks. They are completely unsuitable for index scenarios with millions or tens of millions of data entries.

### Why Do Inserts/Updates Slow Down?

The "side effect" of indexes is essentially **"data modifications require synchronous maintenance of the integrity of the B+ Tree"**, not a characteristic of arrays:

1. When inserting/updating data, you need to do two things:
   - Step 1: Modify the row data of the MySQL data table itself (this step is the same as without indexes);
   - Step 2: Synchronously update the corresponding index B+ Tree — because B+ Trees require maintaining order and balance at all times. Inserting a new value may require **splitting nodes**, deleting a value may require **merging nodes**, and updating a value may require adjusting node positions. These operations all add additional computational and I/O overhead.
2. The more indexes there are, the greater the overhead: If a table has 5 indexes, inserting a single piece of data requires maintaining 5 independent B+ Trees simultaneously, resulting in even slower speed.

Supplement: Arrays Are Only Used for "Local Storage" in Indexes, Not as the Core Structure
Inside a single node of a B+ Tree, an **ordered array** is used to store key values (e.g., storing index values such as `[10,20,30]` in one node). However, this is only a detail inside the node. The core logic of the entire index is the "balanced multi-way search" of the B+ Tree, not the linear storage of arrays.

------

数组之所以不适合作为索引的核心结构，核心原因是：

- 数组如果是**无序的**：查询需要全量遍历（时间复杂度 $O(n)$），完全失去索引的意义；
- 数组如果是**有序的**：查询可以用二分法（$O(logn)$），但插入/删除需要移动大量元素（$O(n)$），效率比 B+ 树更低。

### 为什么查询更快？

1. **有序性 + 分层索引**：B+ 树的所有节点按关键字（索引字段值）有序排列，根节点→分支节点→叶子节点的分层结构，能快速定位数据位置（比如查 `id=100` 的数据，不需要遍历全表，只需从根节点向下找，时间复杂度稳定在 $O(logn)$）；
2. **叶子节点链式相连**：所有数据行的指针（或值）都存在叶子节点，且叶子节点用链表串联，非常适合范围查询（比如 `create_time > '2024-01-01'`）；
3. **磁盘友好**：B+ 树的节点大小适配磁盘块，减少磁盘 I/O 次数（数据库操作的瓶颈主要是磁盘 I/O，而非内存计算）。

对比数组：哪怕是有序数组，二分查询的效率虽然接近 B+ 树，但数组无法高效支持范围查询，且无法适配磁盘的块存储特性，完全不适合百万/千万级数据的索引场景。

### 为什么插入/更新会变慢？

索引的“副作用”本质是 **“数据修改需要同步维护 B+ 树的完整性”**，而非数组的特性：

1. 插入/更新数据时，你需要做两件事：
   - 第一步：修改 MySQL 数据表本身的行数据（这一步和无索引时一样）；
   - 第二步：同步更新对应的索引 B+ 树——因为 B+ 树要求始终有序且平衡，插入新值可能需要**分裂节点**，删除值可能需要**合并节点**，更新值可能需要调整节点位置，这些操作都会增加额外的计算和 I/O 开销。
2. 索引越多，开销越大：如果一张表有 5 个索引，插入一条数据时，需要同时维护 5 棵独立的 B+ 树，速度会更慢。

补充：数组在索引中仅作为“局部存储”，而非核心结构
B+ 树的单个节点内部，会用**有序数组**存储关键字（比如一个节点里存 `[10,20,30]` 这些索引值），但这只是节点内部的细节，整个索引的核心逻辑是 B+ 树的“平衡多路查找”，而非数组的线性存储。
