## Section Data Structure and Algorithm (AEiE0701)

## 📖 1. Introduction
Data structures and algorithms form the foundation of computer science and software engineering. Understanding how data is organized, stored, and manipulated is crucial for writing efficient programs. For the NEC license exam, this section tests your fundamental knowledge of linear and non-linear data structures, abstract data types (ADTs), and their practical implementations and applications.

## 2. Basic Concepts: Data Types, Data Structures, and ADTs

### Data Types
A data type defines a set of values and the operations that can be performed on those values. Examples include integers, floating-point numbers, characters, and booleans.

### Data Structures
A data structure is a specialized format for organizing, processing, retrieving, and storing data. It provides a way to manage large amounts of data efficiently.

### Abstract Data Types (ADT)
An ADT is a theoretical concept that defines a data type mathematically, specifying the data and operations but not the implementation details.

> [!NOTE] Definition
> **Abstract Data Type (ADT)**: A mathematical model for data types where a data type is defined by its behavior (semantics) from the point of view of a user, specifically in terms of possible values, possible operations on data of this type, and the behavior of these operations.

## 3. Linear Data Structures: Stack and Queue Implementation

Linear data structures organize data elements in a sequential manner, where each element is connected to its previous and next element.

### Stacks
A stack follows the **Last In, First Out (LIFO)** principle.

**Core Operations:**
- `push(item)`: Adds an item to the top of the stack.
- `pop()`: Removes and returns the item from the top of the stack.
- `peek()`: Returns the top item without removing it.
- `isEmpty()`: Checks if the stack is empty.

**Array Implementation of Stack:**
```c
#define MAX 100
int stack[MAX];
int top = -1;

void push(int item) {
    if (top >= MAX - 1) {
        printf("Stack Overflow\n");
    } else {
        stack[++top] = item;
    }
}

int pop() {
    if (top < 0) {
        printf("Stack Underflow\n");
        return -1;
    } else {
        return stack[top--];
    }
}
```

### Queues
A queue follows the **First In, First Out (FIFO)** principle.

**Core Operations:**
- `enqueue(item)`: Adds an item to the rear of the queue.
- `dequeue()`: Removes and returns the item from the front of the queue.
- `front()`: Returns the front item without removing it.

**Array Implementation of Queue:**
```c
#define MAX 100
int queue[MAX];
int front = -1, rear = -1;

void enqueue(int item) {
    if (rear == MAX - 1) {
        printf("Queue Overflow\n");
        return;
    }
    if (front == -1) front = 0;
    queue[++rear] = item;
}

int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow\n");
        return -1;
    }
    return queue[front++];
}
```

## 4. Stack Application: Infix to Postfix Conversion & Evaluation

### Infix vs. Postfix
- **Infix**: Operator is between operands (e.g., $A + B$).
- **Postfix (Reverse Polish Notation)**: Operator follows operands (e.g., $A B +$).

### Infix to Postfix Conversion Algorithm
1. Initialize an empty stack for operators and an empty list for output.
2. Scan the infix expression from left to right.
3. If operand, add to output.
4. If `(`, push to stack.
5. If `)`, pop from stack to output until `(` is found.
6. If operator, pop from stack to output until an operator with lower precedence is at the top of the stack. Then push the current operator.
7. Pop remaining operators to output.

**Example:**
Convert $A * (B + C) / D$ to Postfix.
- Output: $A B C + * D /$

### Evaluation of Postfix Expression
1. Initialize an empty stack.
2. Scan postfix expression from left to right.
3. If operand, push to stack.
4. If operator, pop two operands, apply operator, and push result back to stack.
5. Final result is the only item left in the stack.

## 5. Array Implementation of Lists
Lists can be implemented using arrays, providing $O(1)$ time complexity for accessing elements by index but $O(n)$ time complexity for insertions and deletions (due to shifting).

## 6. Basic Operations on Linked List
A linked list is a linear data structure where elements are not stored at contiguous memory locations. Elements are linked using pointers.

### Node Structure (C Example)
```c
struct Node {
    int data;
    struct Node* next;
};
```

### Insertion
1. **At Beginning:** Time Complexity $O(1)$.
2. **At End:** Time Complexity $O(n)$ (or $O(1)$ if a tail pointer is maintained).
3. **At Specific Position:** Time Complexity $O(n)$.

### Deletion
1. **From Beginning:** Time Complexity $O(1)$.
2. **From End:** Time Complexity $O(n)$.
3. **From Specific Position:** Time Complexity $O(n)$.

## 7. Concept of Tree and Binary Tree Operations
A tree is a non-linear hierarchical data structure consisting of nodes connected by edges.

> [!NOTE] Definition
> **Binary Tree**: A tree data structure in which each node has at most two children, referred to as the left child and the right child.

### Terminology
- **Root**: Topmost node.
- **Leaf**: Node with no children.
- **Height**: Number of edges on the longest path from root to leaf.

### Operations in Binary Tree
1. **Insertion**: Adding a new node.
2. **Deletion**: Removing a node (requires handling cases with 0, 1, or 2 children).
3. **Traversal**:
   - **Inorder (Left, Root, Right)**: Visits left subtree, root, right subtree.
   - **Preorder (Root, Left, Right)**: Visits root, left subtree, right subtree.
   - **Postorder (Left, Right, Root)**: Visits left subtree, right subtree, root.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> A common mistake is forgetting to handle edge cases like empty stacks/queues (underflow) or full static structures (overflow) in array-based implementations.

> [!TIP]
> For tree traversals, memorize the sequence:
> - Preorder = Root first
> - Inorder = Root in middle (gives sorted order for Binary Search Trees)
> - Postorder = Root last

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Stack Time Complexity: $O(1)$ for Push/Pop.
> - Queue Time Complexity: $O(1)$ for Enqueue/Dequeue.
> - Maximum nodes in a binary tree of height $h$ is $2^{h+1} - 1$.
> - Minimum height of a binary tree with $n$ nodes is $\lfloor \log_2 n \rfloor$.

## ✏️ Practice Problems
1. Convert the infix expression `A + B * C - (D / E ^ F) * G` to postfix notation.
   - *Sketch:* Apply precedence rules. Stack operators and output operands.
2. Write a C function to delete a node from the nth position in a singly linked list.
   - *Sketch:* Traverse to $(n-1)$th node, adjust its `next` pointer to skip the $n$th node, free the $n$th node.
3. Perform a preorder traversal of a binary tree where root is 10, left child is 5, right child is 20, and left child's left child is 2.
   - *Sketch:* Result is `10, 5, 2, 20`.
</Section 7.1: Data Structure and Algorithm (AEiE0701)>
