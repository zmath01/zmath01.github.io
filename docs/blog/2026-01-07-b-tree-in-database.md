# B+ Tree in Database

In databases (such as MySQL), the underlying implementation of the vast majority of indexes (including primary key indexes, ordinary indexes, and composite indexes) is the **B+ Tree (B+ Tree)**, a **balanced multi-way search tree**, rather than an array.

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

The core reasons why arrays are not suitable as the core structure of indexes are:

- If the array is **unordered**: Queries require full traversal (time complexity $O(n)$), which completely defeats the purpose of an index;
- If the array is **ordered**: Queries can use binary search ($O(logn)$), but inserts/deletions require moving a large number of elements ($O(n)$), which is less efficient than B+ Trees.

### Why Do Queries Run Faster?

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
