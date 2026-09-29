## Section Sorting, Searching, and Graphs (AEiE0702)

## 📖 1. Introduction
Sorting and searching are fundamental operations that determine the efficiency of software applications. Graphs model networks of information, and mastering graph algorithms is essential for routing, scheduling, and optimizing network flows. This section prepares you for exam questions targeting algorithmic efficiency and graph theory.

## 2. Types of Sorting: Internal and External

> [!NOTE] Definition
> **Internal Sorting**: Sorting algorithms that require all data to be loaded into the main memory (RAM) at once (e.g., Quick Sort, Merge Sort).
> **External Sorting**: Sorting algorithms used when data is too large to fit into RAM, requiring auxiliary storage like disk drives (e.g., External Merge Sort).

## ⚖️ 3. Sorting Algorithms Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stable? |
|-----------|-----------|--------------|------------|-------------------|---------|
| Insertion | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| Selection | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| Bubble (Exchange)| $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| Merge Sort| $O(n \log n)$| $O(n \log n)$| $O(n \log n)$| $O(n)$ | Yes |
| Heap Sort | $O(n \log n)$| $O(n \log n)$| $O(n \log n)$| $O(1)$ | No |
| Radix Sort| $O(nk)$ | $O(nk)$ | $O(nk)$ | $O(n+k)$ | Yes |
| Shell Sort| $O(n \log n)$| $O(n^{4/3})$ | $O(n^{3/2})$ | $O(1)$ | No |

### Selection Sort and Insertion Sort
- **Selection Sort**: Repeatedly finds the minimum element from the unsorted part and places it at the beginning.
- **Insertion Sort**: Builds the final sorted array one item at a time by inserting elements into their proper position.

### Merge Sort
A Divide and Conquer algorithm that divides the array into two halves, recursively sorts them, and merges the two sorted halves.

### Radix Sort
A non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

### Heap Sort as a Priority Queue
Heap Sort uses a binary heap data structure. A Priority Queue is an abstract data type where each element has a priority, and elements with higher priority are served before those with lower priority. A max-heap or min-heap directly implements a priority queue efficiently.

## 4. Search Techniques

### Sequential (Linear) Search
- Checks every element in the list until the target is found.
- Time Complexity: $O(n)$.

### Binary Search
- Works on sorted arrays by repeatedly dividing the search interval in half.
- Time Complexity: $O(\log n)$.

```c
int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (arr[m] == x) return m;
        if (arr[m] < x) l = m + 1;
        else r = m - 1;
    }
    return -1;
}
```

### Tree Search & General Search Tree
Searching in a Binary Search Tree (BST) takes $O(\log n)$ on average but can degrade to $O(n)$ if the tree is skewed. General search trees like B-Trees optimize disk accesses.

## 5. Graphs: Undirected and Directed

> [!NOTE] Definition
> **Graph**: $G = (V, E)$ consists of a set of vertices $V$ and a set of edges $E$.
> **Undirected Graph**: Edges have no direction (pairs are unordered).
> **Directed Graph (Digraph)**: Edges have a direction (pairs are ordered).

### Representation of Graph
1. **Adjacency Matrix**: A 2D array $A$ of size $V \times V$ where $A[i][j] = 1$ if there is an edge from $i$ to $j$. Space: $O(V^2)$.
2. **Adjacency List**: An array of lists where array index represents the vertex and the list contains all adjacent vertices. Space: $O(V + E)$.

## 6. Graph Traversal

### Breadth-First Search (BFS)
Explores the neighbor nodes first, before moving to the next level neighbors.
- Data Structure used: Queue.
- Time Complexity: $O(V + E)$.

### Depth-First Search (DFS)
Explores as far as possible along each branch before backtracking.
- Data Structure used: Stack (or recursion).
- Time Complexity: $O(V + E)$.

## 7. Shortest-Path Algorithm

### Dijkstra's Algorithm (Greedy Algorithm)
Finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

**Algorithm Steps:**
1. Create a `dist` array holding distances from source to all vertices. Initialize to $\infty$. Set source distance to 0.
2. Create a priority queue (min-heap) to extract minimum distance vertices.
3. While the queue is not empty:
   - Extract vertex $u$ with minimum distance.
   - For every adjacent vertex $v$ of $u$, if `dist[u] + weight(u, v) < dist[v]`, update `dist[v]` and push to the queue.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Applying Dijkstra's algorithm to graphs with negative weight edges will yield incorrect results. Use Bellman-Ford for negative weights.

> [!TIP]
> Always memorize the space and time complexities of sorting algorithms. They are frequently tested as multiple-choice questions.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Binary search requires a sorted array.
> - Maximum edges in a simple undirected graph with $V$ vertices is $V(V-1)/2$.
> - BFS finds the shortest path in an unweighted graph.

## ✏️ Practice Problems
1. Sort the array `[5, 2, 9, 1, 5, 6]` using Insertion Sort and show intermediate steps.
   - *Sketch:* `[2, 5, 9, 1, 5, 6]` -> `[2, 5, 9, 1, 5, 6]` -> `[1, 2, 5, 9, 5, 6]` -> ...
2. Differentiate between Adjacency Matrix and Adjacency List representations.
3. Trace Dijkstra's algorithm on a 3-node triangular graph with edge weights $A-B=4$, $B-C=2$, $A-C=7$. Source node is $A$.
   - *Sketch:* Update distances. Output shortest distances from A: `A=0, B=4, C=6`.
</Section 7.2: Sorting, Searching, and Graphs (AEiE0702)>
