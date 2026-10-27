# =====================================================================
#  LAB 4B (VE NHA) - CHUONG 4: CAU TRUC DU LIEU TRUU TUONG
#  Co ban    : 4B.1 DS lien ket kep co thu tu | 4B.2 DS vong - Josephus | 4B.3 Hang doi vong + Deque
#  Trung binh: 4B.4 Heap + Heap sort          | 4B.5 Trung to -> Hau to
#  Nang cao  : 4B.6 Dijkstra + Floyd-Warshall | 4B.7 Kruskal + Prim    | 4B.8 (thu thach) AVL
#  Chay:  python lab4B_ve_nha.py
#  Luu y: o 4B.4 KHONG dung module heapq - phai tu cai dat heap.
# =====================================================================
import heapq          # chi dung o 4B.6 / 4B.7 (Dijkstra, Prim)
import sys
from collections import deque

sys.setrecursionlimit(10000)
INF = float("inf")


class LCG:
    def __init__(self, seed):
        self.x = seed

    def next(self):
        self.x = (self.x * 1103515245 + 12345) & 0x7FFFFFFF
        return self.x

    def range(self, lo, hi):
        return lo + self.next() % (hi - lo + 1)


passed = total = 0


def check(name, got, expect):
    global passed, total
    total += 1
    ok = got == expect
    passed += ok
    print(f"  {name:<36} -> {got}" + ("   [OK]" if ok else f"   [SAI] can: {expect}"))


def join(v):
    return " ".join(map(str, v))


# =====================================================================
# 4B.1 (CO BAN) - DS lien ket kep luon tang dan. insert on dinh, remove nut dau tien == x.
# =====================================================================
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class SortedDList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, x):
        # TODO: viet code cua ban o day
        pass

    def remove(self, x):
        # TODO: viet code cua ban o day
        return False

    def forward(self):
        v, p = [], self.head
        while p:
            v.append(p.data)
            p = p.next
        return join(v)

    def backward(self):
        v, p = [], self.tail
        while p:
            v.append(p.data)
            p = p.prev
        return join(v)


# =====================================================================
# 4B.2 (CO BAN) - Josephus bang DS lien ket vong tu cai dat
# =====================================================================
class CNode:
    def __init__(self, ident):
        self.id = ident
        self.next = None


def josephus(n, k):
    order = []
    # TODO: viet code cua ban o day
    pass
    return order


# =====================================================================
# 4B.3 (CO BAN) - Hang doi vong bang mang + cua so truot (deque)
# =====================================================================
class CircularQueue:
    def __init__(self, cap):
        self.a = [None] * cap
        self.front_ = 0
        self.count = 0

    def empty(self):
        return self.count == 0

    def full(self):
        return self.count == len(self.a)

    def size(self):
        return self.count

    def enqueue(self, x):
        # TODO: viet code cua ban o day
        return False

    def dequeue(self):
        # TODO: viet code cua ban o day
        return 0

    def front(self):
        # TODO: viet code cua ban o day
        return 0


def sliding_max(a, k):
    res = []
    # TODO: viet code cua ban o day
    pass
    return res


def sliding_max_brute(a, k):
    return [max(a[i:i + k]) for i in range(len(a) - k + 1)]


# =====================================================================
# 4B.4 (TRUNG BINH) - Min-heap tren mang (con cua i: 2i+1, 2i+2), heap sort, top-k
# =====================================================================
class MinHeap:
    def __init__(self):
        self.h = []

    def push(self, x):
        # TODO: viet code cua ban o day
        pass

    def pop(self):
        # TODO: viet code cua ban o day
        return 0

    def peek(self):
        return self.h[0]

    def size(self):
        return len(self.h)


def sift_down_max(a, i, n):
    # TODO: viet code cua ban o day
    pass


def heap_sort(a):
    # TODO: viet code cua ban o day
    pass


def top_k(a, k):
    """k phan tu lon nhat, thu tu GIAM dan, dung MinHeap kich thuoc k."""
    res = []
    # TODO: viet code cua ban o day
    pass
    return res


# =====================================================================
# 4B.5 (TRUNG BINH) - Trung to -> hau to (shunting-yard). ^ ket hop phai.
# =====================================================================
def prec(op):
    return {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}.get(op, 0)


def infix_to_postfix(s):
    out = []
    # TODO: viet code cua ban o day
    pass
    return " ".join(out)


def eval_postfix(expr):
    # TODO: viet code cua ban o day
    return 0


# =====================================================================
# 4B.6 (NANG CAO) - Dijkstra (heapq, lazy deletion) + Floyd-Warshall kiem chung
#   adj[u] = list cac (v, w)
# =====================================================================
def dijkstra(adj, s):
    """Tra ve (dist, parent)."""
    n = len(adj)
    d, parent = [INF] * n, [-1] * n
    # TODO: viet code cua ban o day
    pass
    return d, parent


def floyd_warshall(adj):
    n = len(adj)
    D = [[INF] * n for _ in range(n)]
    # TODO: viet code cua ban o day
    pass
    return D


# =====================================================================
# 4B.7 (NANG CAO) - Kruskal (DSU) + Prim. Canh = (u, v, w).
# =====================================================================
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        # TODO: viet code cua ban o day
        return x

    def unite(self, a, b):
        # TODO: viet code cua ban o day
        return False


def kruskal(n, edges):
    """Tra ve (tong trong so, danh sach canh duoc chon theo thu tu chon)."""
    total, chosen = 0, []
    # TODO: viet code cua ban o day
    pass
    return total, chosen


def prim(n, edges):
    total = 0
    # TODO: viet code cua ban o day
    pass
    return total


# =====================================================================
# 4B.8 (THU THACH) - AVL: chen co can bang, dem so phep xoay don
# =====================================================================
class ANode:
    def __init__(self, key):
        self.key, self.h, self.l, self.r = key, 1, None, None


rotations = 0


def H(t):
    return t.h if t else 0


def upd(t):
    t.h = 1 + max(H(t.l), H(t.r))


def rot_right(y):
    global rotations
    # TODO: viet code cua ban o day
    return y


def rot_left(x):
    global rotations
    # TODO: viet code cua ban o day
    return x


def avl_insert(t, k):
    # TODO: viet code cua ban o day
    return t if t else ANode(k)


def pre(t, v):
    if t:
        v.append(t.key)
        pre(t.l, v)
        pre(t.r, v)


def height_any(t):
    return 1 + max(height_any(t.l), height_any(t.r)) if t else 0


def main():
    global rotations
    print("===== 4B.1: DS lien ket kep co thu tu =====")
    L = SortedDList()
    for x in (30, 10, 50, 20, 40, 10):
        L.insert(x)
    check("insert 30 10 50 20 40 10", f"{L.forward()} | {L.backward()}", "10 10 20 30 40 50 | 50 40 30 20 10 10")
    a, b, c = L.remove(10), L.remove(50), L.remove(99)
    L.insert(5)
    L.insert(60)
    tf = "".join("T" if v else "F" for v in (a, b, c))
    check("remove 10,50,99; insert 5,60", f"{L.forward()} | {L.backward()} | {tf}",
          "5 10 20 30 40 60 | 60 40 30 20 10 5 | TTF")

    print("\n===== 4B.2: Josephus =====")
    check("n=7, k=3 (thu tu bi loai)", join(josephus(7, 3)), "3 6 2 7 5 1 4")
    check("n=10, k=2 song sot", str((josephus(10, 2) or [0])[-1]), "5")
    check("n=41, k=3 song sot", str((josephus(41, 3) or [0])[-1]), "31")
    check("n=1, k=5", join(josephus(1, 5)), "1")

    print("\n===== 4B.3: Hang doi vong + cua so truot =====")
    q = CircularQueue(5)
    for i in range(1, 6):
        q.enqueue(i)
    s = "ok " if q.enqueue(6) else "full "
    d1 = q.dequeue()
    d2 = q.dequeue()
    s += f"{d1}{d2} "
    q.enqueue(6)
    q.enqueue(7)
    s += f"front={q.front()} size={q.size()} :"
    while not q.empty():
        s += f" {q.dequeue()}"
    check("cap 5: 1..5, +6, -2, +6 +7, xa het", s, "full 12 front=3 size=5 : 3 4 5 6 7")
    check("slidingMax [1 3 -1 -3 5 3 6 7], k=3", join(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3)), "3 3 5 5 6 7")
    g = LCG(12)
    arr = [g.range(-1000, 1000) for _ in range(5000)]
    check("n=5000, k=50: khop vet can?", "khop" if sliding_max(arr, 50) == sliding_max_brute(arr, 50) else "lech", "khop")

    print("\n===== 4B.4: Heap =====")
    hp = MinHeap()
    for x in (5, 3, 8, 1, 9, 2):
        hp.push(x)
    check("mang heap sau push 5 3 8 1 9 2", join(hp.h), "1 3 2 5 9 8")
    out = []
    while hp.size():
        out.append(hp.pop())
    check("pop het", join(out), "1 2 3 5 8 9")
    bb = [4, 10, 3, 5, 1, 7, 7, 2]
    heap_sort(bb)
    check("heapSort 4 10 3 5 1 7 7 2", join(bb), "1 2 3 4 5 7 7 10")
    g = LCG(21)
    arr = [g.range(0, 1000000) for _ in range(100000)]
    cc = arr[:]
    heap_sort(cc)
    dd = sorted(arr)
    check("heapSort 100000 so ngau nhien", "dung" if cc == dd else "sai", "dung")
    check("top-5 lon nhat", join(top_k(arr, 5)), join(dd[::-1][:5]))

    print("\n===== 4B.5: Trung to -> Hau to =====")
    check("a+b*c", infix_to_postfix("a+b*c"), "a b c * +")
    check("(a+b)*(c-d)/e", infix_to_postfix("(a+b)*(c-d)/e"), "a b + c d - * e /")
    check("a-b-c (ket hop trai)", infix_to_postfix("a-b-c"), "a b - c -")
    check("a^b^c (ket hop phai)", infix_to_postfix("a^b^c"), "a b c ^ ^")
    check("3+4*2/(1-5)^2^3", infix_to_postfix("3+4*2/(1-5)^2^3"), "3 4 2 * 1 5 - 2 3 ^ ^ / +")
    check("gia tri (12+3)*4-100/(2+3)", str(eval_postfix(infix_to_postfix("(12+3)*4-100/(2+3)"))), "40")
    check("gia tri 2^3^2", str(eval_postfix(infix_to_postfix("2^3^2"))), "512")

    print("\n===== 4B.6: Dijkstra + Floyd-Warshall =====")
    n = 6
    adj = [[] for _ in range(n)]
    for u, v, w in [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5), (3, 4, 3), (4, 5, 1), (3, 5, 6), (2, 4, 8)]:
        adj[u].append((v, w))
    d, par = dijkstra(adj, 0)
    check("dist tu 0", join(d), "0 3 1 4 7 8")
    p, v = [], 5
    while v != -1:
        p.append(v)
        v = par[v]
    check("duong di 0 -> 5", join(p[::-1]), "0 2 1 3 4 5")
    D = floyd_warshall(adj)
    check("Floyd dong 0 khop Dijkstra?", "khop" if D[0] == d else "lech", "khop")
    check("Floyd D[3][0] (khong toi duoc)", "INF" if D[3][0] == INF else str(D[3][0]), "INF")
    g, N = LCG(33), 200
    A = [[] for _ in range(N)]
    for _ in range(2000):
        u = g.range(0, N - 1)
        v = g.range(0, N - 1)
        w = g.range(1, 100)
        A[u].append((v, w))
    D2 = floyd_warshall(A)
    ok, tot = True, 0
    for s0 in range(N):
        ds, _ = dijkstra(A, s0)
        ok &= ds == D2[s0]
        tot += sum(x for x in ds if x != INF)
    check("200 dinh: Dijkstra x200 == Floyd?", "khop" if ok else "lech", "khop")
    print(f"  (tong moi khoang cach toi duoc = {tot})")

    print("\n===== 4B.7: Kruskal + Prim =====")
    E = [(0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15),
         (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)]
    w, ch = kruskal(7, E)
    check("Kruskal: canh chon", "".join(f"({u},{v},{x})" for u, v, x in ch), "(0,3,5)(2,4,5)(3,5,6)(0,1,7)(1,4,7)(4,6,9)")
    check("Kruskal / Prim tong trong so", f"{w} / {prim(7, E)}", "39 / 39")
    g, N, R = LCG(44), 300, []
    for i in range(1, N):
        u = g.range(0, i - 1)
        R.append((u, i, g.range(1, 1000)))
    for _ in range(3000):
        u = g.range(0, N - 1)
        v = g.range(0, N - 1)
        if u != v:
            R.append((min(u, v), max(u, v), g.range(1, 1000)))
    k1, ch = kruskal(N, R)
    p1 = prim(N, R)
    check("300 dinh: Kruskal == Prim?", "khop" if k1 == p1 and len(ch) == N - 1 else "lech", "khop")
    print(f"  (trong so MST = {k1})")

    print("\n===== 4B.8: AVL (thu thach) =====")
    t, rotations = None, 0
    for k in (10, 20, 30, 40, 50, 25):
        t = avl_insert(t, k)
    v = []
    pre(t, v)
    check("chen 10 20 30 40 50 25: preorder", f"{join(v)} | h={height_any(t)} rot={rotations}", "30 20 10 25 40 50 | h=3 rot=4")
    t, rotations = None, 0
    for k in range(1, 1001):
        t = avl_insert(t, k)
    check("chen 1..1000 tang dan: chieu cao", str(height_any(t)), "10")
    print(f"\nTONG: {passed}/{total} test dung")


if __name__ == "__main__":
    main()
