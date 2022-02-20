#!/usr/bin/env python
# coding: utf-8
1. What is the distinction between a list and an array?
2. What are the qualities of a binary tree?
3. What is the best way to combine two balanced binary search trees?
4. How would you describe Heap in detail?
5. In terms of data structure, what is a HashMap?
6. How do you explain the complexities of time and space?
7. How do you recursively sort a stack?
Q. 1 What is the distinction between a list and an array?

Ans:List: A list in Python is a collection of items which can contain elements of multiple data types, which may be either numeric, character logical values, etc. ... 

Array: An array is a vector containing homogeneous elements i.e. belonging to the same data type.Q. 2. What are the qualities of a binary tree?


Sol: A binary tree consists of a number of nodes that contain the data to be stored (or pointers to the data), and the following structural characteristics : Each node has up to two direct child nodes. There is exactly one node, called the root of the tree, that has no parent node. All other nodes have exactly one parent.Q. 3. What is the best way to combine two balanced binary search trees?
Sol: 
   1. Perform inorder traversal of tree1 and store each node's value in arr1.
2. Perform inorder traversal of tree2 and store each node's value in arr2.
3. Combine arr1 and arr2 using merge function of merge sort to create result array.
4. Return result array.Q.  4. How would you describe Heap in detail?
Sol : A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority, or when insertions need to be interspersed with removals of the root node. A common implementation of a heap is the binary heap, in which the tree is a binary tree Q. 5. In terms of data structure, what is a HashMap?


Sol: A HashMap is a data structure that is able to map certain keys to certain values. The keys and values could be anything. For example, if I were making a game, I might link every username to a friends list, represented by a List of Strings.Q. 6. How do you explain the complexities of time and space?
Sol:
    Time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. Similarly, Space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run as a function of the length of the inputQ. 7. How do you recursively sort a stack?

Sol: 
    This problem is mainly a variant of Reverse stack using recursion. The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one in sorted order. Here sorted order is important