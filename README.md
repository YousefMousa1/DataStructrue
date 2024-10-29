This repository contains two foundational data structure projects I implemented from scratch: 
an AVL Tree and a Fibonacci Heap. Both projects showcase my skills in coding efficient data structures with a focus on balancing, optimal operations,
and deep understanding of algorithmic design. 

Project 1: AVL Tree
Overview
An AVL Tree is a self-balancing binary search tree where the difference between heights of left and right subtrees is at most one. This project involved implementing an AVL Tree from scratch, focusing on essential operations like insertion, deletion, and balancing.

Features 
Insertion: Automatically balances the tree after every insertion to maintain O(log n) height.
Deletion: Handles rebalancing as nodes are removed.
Rotations: Implements left, right, left-right, and right-left rotations for rebalancing.
Height Maintenance: Tracks heights of subtrees to enable quick, efficient balancing.


Project 2: Fibonacci Heap
Overview
A Fibonacci Heap is a more complex, amortized data structure offering faster heap operations and widely used in algorithms such as Dijkstra's shortest path. This project involved implementing a Fibonacci Heap from scratch, with careful attention to the structure’s potential for merging and cascading cuts.

Features
Insertion: Adds new nodes in constant time, with minimal impact on the tree structure.
Minimum Extraction: Efficiently finds and removes the minimum node.
Decrease Key: Supports reducing the key value of a node and cascading cuts to maintain optimal structure.
Merge Heaps: Combines two heaps in constant time, preserving the heap properties.


