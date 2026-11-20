# B+ Tree in Database

MySQL’s InnoDB engine uses B-tree indexes for common primary-key and secondary indexes. Their B+ tree layout keeps leaf entries in key order. Specialized indexes, such as spatial and full-text indexes, use different structures. [MySQL reference manual](https://dev.mysql.com/doc/refman/8.4/en/innodb-physical-structure.html)

<!--more-->

The core reasons why arrays are not suitable as the core structure of indexes are:

- If the array is **unordered**: Queries require full traversal (time complexity $O(n)$), which completely defeats the purpose of an index;
- If the array is **ordered**: Queries can use binary search ($O(\log n)$), but inserts/deletions require moving a large number of elements ($O(n)$), which is less efficient than B+ Trees.

### Why Do B+ Trees Speed Up Queries?

The structural characteristics of B+ Trees are perfectly suited to database query scenarios:

1. **Orderliness + Hierarchical Indexing**: Internal nodes contain ordered separator keys. The hierarchical structure from root node → branch node → leaf node can quickly locate data positions (e.g., to find data with `id=100`, there is no need to traverse the entire table; you only need to search down from the root node, with a stable time complexity of $O(\log n)$);
2. **Leaf Nodes Linked in a Chain**: InnoDB’s clustered index leaves store row data. Secondary index leaves store the secondary key and the primary-key value, which can be used to look up the row. Linked leaf pages allow efficient sequential scans after locating the start of a range. [Clustered and secondary indexes](https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html)
3. **Disk-Friendly**: The node size of a B+ Tree is adapted to disk blocks, reducing the number of disk I/O operations (the bottleneck of database operations is mainly disk I/O, not in-memory computation).

An ordered array also supports efficient range searches. Its main disadvantage for a frequently updated disk-backed index is that inserting or deleting an entry can move many elements. B+ trees normally update a small number of pages and use a high fan-out to keep the tree shallow.

### Why Do Inserts/Updates Slow Down?

The "side effect" of indexes is essentially **"data modifications require synchronous maintenance of the integrity of the B+ Tree"**, not a characteristic of arrays:

1. When inserting/updating data, you need to do two things:
   - Step 1: Modify the row data of the MySQL data table itself (this step is the same as without indexes);
   - Step 2: Synchronously update the corresponding index B+ Tree — because B+ Trees require maintaining order and balance at all times. Inserting a new value may require **splitting nodes**, deleting a value may require **merging nodes**, and updating a value may require adjusting node positions. These operations all add additional computational and I/O overhead.
2. The more indexes there are, the greater the overhead: An insert typically adds an entry to each applicable index. An update to a non-indexed column generally does not require changing secondary index entries.

Supplement: Arrays Are Only Used for "Local Storage" in Indexes, Not as the Core Structure
Inside a single node of a B+ Tree, an **ordered array** is used to store key values (e.g., storing index values such as `[10,20,30]` in one node). However, this is only a detail inside the node. The core logic of the entire index is the "balanced multi-way search" of the B+ Tree, not the linear storage of arrays.
