# Lab 3B Report

**Student:** N25DECE085  
**Course:** INT1306_CLC — Data Structures and Algorithms  
**Topic:** Algorithm design techniques

## Results

The Python and C++ implementations pass the supplied Lab 3B checks. The tested meeting schedule requires 4 rooms; the sample TSP optimum is 22; and both closest-pair implementations return the same squared distance on the verification data.

## 3B.1 — Recursive binomial coefficient

For an interior state, Pascal recursion branches into `(n-1,k-1)` and `(n-1,k)`. The recursion tree has one leaf for each term in the expansion, and the full binary tree therefore has `2*C(n,k)-1` calls. The memoized version computes each valid `(i,j)` state once, so it takes `O(nk)` time and `O(nk)` table space (plus `O(n)` recursion depth). Its call count is also `O(nk)`.

## 3B.2 — Binary strings without adjacent ones

Let `A(n)` count valid strings of length `n`. Strings ending in 0 correspond to any valid length `n-1` string. Strings ending in 1 must have 0 immediately before that bit, leaving any valid prefix of length `n-2`. Thus `A(n)=A(n-1)+A(n-2)`, with `A(1)=2`, `A(2)=3`. The counts are Fibonacci numbers shifted by two positions. Backtracking visits only prefixes that can still lead to valid strings; generating every binary string instead explores a full binary tree with `2^(n+1)-1` prefix nodes.

## 3B.3 — Minimum meeting rooms

Meetings are processed by increasing `(start,end)`. The min-heap exposes the room that becomes free first. Reusing it whenever its end time is at most the next start avoids opening a room while one is available. If no room is free, all existing rooms overlap the new meeting, so another room is necessary. The number of rooms is therefore the maximum overlap depth, which is a lower bound for every schedule; the greedy schedule meets that bound and is optimal. Sorting and heap operations take `O(m log m)` time and `O(m)` space.

Choosing meetings by earliest finishing time solves interval scheduling (maximizing the number of non-overlapping meetings), not interval partitioning. For example, three meetings `[0,4)`, `[1,2)`, `[2,3)` need two rooms, while selecting only by finish time would retain just two compatible meetings and does not construct a room assignment.

## 3B.4 — Longest increasing subsequence

For each index `i`, `dp[i]` is the length of the longest strictly increasing subsequence ending at `i`. The recurrence is `dp[i]=1+max(dp[j])` over `j<i` with `a[j]<a[i]`, or 1 if no such `j` exists. The implementation stores predecessor indices for reconstruction. The quadratic method takes `O(n^2)` time and `O(n)` space; the tails method finds the length in `O(n log n)` time. `tails` is not necessarily an actual subsequence: `tails[k]` is the smallest possible ending value of an increasing subsequence of length `k+1` seen so far.

## 3B.5 — TSP branch and bound

The branch-and-bound search visits cities in increasing index order and prunes when the current cost plus a valid lower bound cannot beat the best completed tour. On the supplied 5-city matrix, the optimum is 22. On the seeded 10-city matrix, the C++ run examined 13,230 recursive nodes versus 362,880 complete tours for brute force. A tighter valid bound can sum, for each not-yet-completed city, its cheapest feasible outgoing edge, while accounting for the current endpoint and the return to city 0.

## 3B.6 — Closest pair

The divide-and-conquer method computes the best result in each half, then checks points in the vertical strip around the dividing line, ordered by y-coordinate. In a strip with minimum separation `d`, geometric packing limits the number of relevant points in a `d × 2d` neighborhood to a constant; therefore only a constant number of following points need checking. Sorting each recursive strip costs `O(n log^2 n)` overall. To reach `O(n log n)`, keep each recursive range sorted by y and merge the two y-sorted halves at each level instead of sorting each strip again.

## Verification

- Python: `python python/lab3B_ve_nha.py` — all displayed checks pass.
- C++: `g++ -O2 -std=c++17 cpp/lab3B_ve_nha.cpp -o lab3B && ./lab3B` — all displayed checks pass.
