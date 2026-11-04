# Lab 4B Report

**Student:** N25DECE085  
**Course:** INT1306_CLC — Data Structures and Algorithms  
**Topic:** Abstract data types and graph algorithms

## Results

The Python and C++ implementations pass all 31 supplied Lab 4B checks, including the AVL challenge. Verification covers linked-list directions, Josephus order, circular queue wraparound, sliding maxima, heap operations, expression conversion/evaluation, shortest paths, minimum spanning trees, and AVL rotations.

## 4B.1 — Sorted doubly linked list

Deletion must handle four pointer cases: deleting the only node (update both head and tail), deleting the head (update the new head's `prev`), deleting the tail (update the new tail's `next`), and deleting a middle node (link its predecessor to its successor in both directions). A sorted linked list still cannot support binary search efficiently because reaching the middle node requires traversing from an endpoint; indexed access is `O(n)`.

## 4B.2 — Josephus

The circular linked-list implementation removes each selected node in constant pointer time after counting around the ring. Its overall time is `O(nk)` and space is `O(n)` for the list and returned order. With zero-based survivor numbering, `J(1,k)=0` and `J(n,k)=(J(n-1,k)+k) mod n`; converting to one-based labels gives survivor 31 for `n=41,k=3`.

## 4B.3 — Circular queue and sliding maximum

A non-circular array queue can leave unused cells before its front after dequeues; without shifting elements, it may report full despite free cells. A circular queue reuses those positions by wrapping indices modulo capacity. In the sliding-maximum deque, each index is inserted once and removed at most once, either from the front when expired or from the back when dominated by a newer value. The total work is `O(n)`.

## 4B.4 — Heap, heapsort, and top-k

Bottom-up heap construction is `O(n)`: most nodes are near the leaves and require little or no sift-down work, so summing work by height is bounded by a geometric series. The top-k implementation takes `O(n log k)` time and `O(k)` extra space. Sorting all values takes `O(n log n)` time and is preferable when a fully sorted result is needed; the size-k heap is more efficient when `k` is small.

## 4B.5 — Infix to postfix

The shunting-yard implementation emits operands immediately and uses an operator stack to enforce precedence and associativity. Operators `+,-,*,/` associate left; exponentiation associates right. The evaluator pops the right operand before the left operand, preserving subtraction and division order. Supplied expressions, including `2^3^2`, evaluate correctly (`512`).

## 4B.6 — Dijkstra and Floyd–Warshall

Dijkstra uses a min-priority queue with lazy deletion and returns shortest distances and parent links for nonnegative edge weights. Floyd–Warshall initializes direct edges and repeatedly allows each vertex as an intermediate point. Its `O(V^3)` result agrees with Dijkstra on the supplied verification graph; unreachable pairs remain infinite.

## 4B.7 — Kruskal and Prim

Kruskal sorts edges by `(weight,u,v)` and uses a disjoint-set union structure with path compression and union by rank. Prim grows a tree using a min-heap of frontier edges. Both produce total MST weight 39 on the supplied 7-vertex graph, and their totals agree on the seeded 300-vertex graph.

## 4B.8 — AVL challenge

AVL insertion updates subtree heights and restores balance with single or double rotations. The supplied insertion sequence produces preorder `30 20 10 25 40 50`, height 3, and 4 single rotations. Inserting keys 1 through 1000 in increasing order produces height 10, rather than a linear-height BST.

## Verification

- Python: `python python/lab4B_ve_nha.py` — **31/31 checks pass**.
- C++: `g++ -O2 -std=c++17 cpp/lab4B_ve_nha.cpp -o lab4B && ./lab4B` — **31/31 checks pass**.
