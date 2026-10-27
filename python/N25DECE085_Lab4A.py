# =====================================================================
#  LAB 4A (TREN LOP) - CHUONG 4: CAU TRUC DU LIEU TRUU TUONG
#  4.1 Danh sach lien ket don | 4.2 Ngan xep | 4.3 Cay BST | 4.4 Do thi BFS/DFS
#  Chay:  python lab4A_ctdl_truu_tuong.py
#  Luu y: KHONG dung list.append/pop cho Stack o 4.2 - phai tu quan ly chi so top.
# =====================================================================
from collections import deque

passed = total = 0


def check(name, got, expect):
    global passed, total
    total += 1
    ok = got == expect
    passed += ok
    print(f"  {name:<34} -> {got}" + ("   [OK]" if ok else f"   [SAI] can: {expect}"))


# =====================================================================
# BAI 4.1 - Danh sach lien ket don
# =====================================================================
class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def size(self):
        return self.count

    def __str__(self):                       # dang "[1 -> 2 -> 3]" (da cho san)
        out, p = [], self.head
        while p:
            out.append(str(p.data))
            p = p.next
        return "[" + " -> ".join(out) + "]"

    def push_front(self, x):
        self.head = Node(x, self.head)
        self.count += 1

    def push_back(self, x):
        node = Node(x)
        if self.head is None:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node
        self.count += 1

    def insert_at(self, pos, x):
        """Chen de x nam o vi tri pos (0..count). Sai vi tri -> False."""
        if pos < 0 or pos > self.count:
            return False
        if pos == 0:
            self.head = Node(x, self.head)
            self.count += 1
            return True
        p = self.head
        for _ in range(pos - 1):
            p = p.next
        p.next = Node(x, p.next)
        self.count += 1
        return True

    def find(self, x):
        i, p = 0, self.head
        while p:
            if p.data == x:
                return i
            p = p.next
            i += 1
        return -1

    def remove_value(self, x):
        """Xoa nut DAU TIEN co data == x."""
        prev, p = None, self.head
        while p and p.data != x:
            prev, p = p, p.next
        if p is None:
            return False
        if prev is None:
            self.head = p.next
        else:
            prev.next = p.next
        self.count -= 1
        return True

    def reverse(self):
        prev, p = None, self.head
        while p:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        self.head = prev


# =====================================================================
# BAI 4.2 - Ngan xep bang MANG co dinh dung luong + ung dung
# =====================================================================
class ArrayStack:
    def __init__(self, capacity):
        self.a = [None] * capacity
        self.top_idx = -1

    def empty(self):
        return self.top_idx == -1

    def full(self):
        return self.top_idx == len(self.a) - 1

    def push(self, x):
        """False neu day (overflow)."""
        if self.full():
            return False
        self.top_idx += 1
        self.a[self.top_idx] = x
        return True

    def pop(self):
        v = self.a[self.top_idx]
        self.top_idx -= 1
        return v

    def top(self):
        return self.a[self.top_idx]


def is_balanced(s):
    st = ArrayStack(len(s) + 1)
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.empty() or st.pop() != pairs[ch]:
                return False
    return st.empty()


def eval_postfix(expr):
    """Token cach nhau dau cach; + - * / (chia nguyen, lam tron ve 0 nhu C++)."""
    st = ArrayStack(len(expr) + 1)
    for tok in expr.split():
        if tok in ("+", "-", "*", "/"):
            b = st.pop()
            a = st.pop()
            if tok == "+":
                st.push(a + b)
            elif tok == "-":
                st.push(a - b)
            elif tok == "*":
                st.push(a * b)
            else:
                st.push(int(a / b))
        else:
            st.push(int(tok))
    return st.pop()


# =====================================================================
# BAI 4.3 - BST. Khoa trung: bo qua. height: so NUT (rong = 0).
#   remove nut 2 con: thay bang successor (nho nhat cay con phai).
# =====================================================================
class TNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, t, k):
        if t is None:
            return TNode(k)
        if k < t.key:
            t.left = self._insert(t.left, k)
        elif k > t.key:
            t.right = self._insert(t.right, k)
        return t

    def insert(self, k):
        self.root = self._insert(self.root, k)

    def contains(self, k):
        p = self.root
        while p:
            if k == p.key:
                return True
            p = p.left if k < p.key else p.right
        return False

    def min_key(self):
        p = self.root
        while p.left:
            p = p.left
        return p.key

    def max_key(self):
        p = self.root
        while p.right:
            p = p.right
        return p.key

    def _height(self, t):
        if t is None:
            return 0
        return 1 + max(self._height(t.left), self._height(t.right))

    def height(self):
        return self._height(self.root)

    def _inorder(self, t, out):
        if t is None:
            return
        self._inorder(t.left, out)
        out.append(t.key)
        self._inorder(t.right, out)

    def _preorder(self, t, out):
        if t is None:
            return
        out.append(t.key)
        self._preorder(t.left, out)
        self._preorder(t.right, out)

    def inorder(self):
        out = []
        self._inorder(self.root, out)
        return " ".join(map(str, out))

    def preorder(self):
        out = []
        self._preorder(self.root, out)
        return " ".join(map(str, out))

    def _remove(self, t, k):
        if t is None:
            return None
        if k < t.key:
            t.left = self._remove(t.left, k)
        elif k > t.key:
            t.right = self._remove(t.right, k)
        else:
            if t.left is None:
                return t.right
            if t.right is None:
                return t.left
            s = t.right
            while s.left:
                s = s.left
            t.key = s.key
            t.right = self._remove(t.right, s.key)
        return t

    def remove(self, k):
        self.root = self._remove(self.root, k)


# =====================================================================
# BAI 4.4 - Do thi vo huong: danh sach ke (sap tang), BFS, DFS, thanh phan lien thong
# =====================================================================
class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        for lst in self.adj:
            lst.sort()

    def bfs(self, s):
        """Tra ve (order, dist, parent)."""
        order, dist, parent = [], [-1] * self.n, [-1] * self.n
        q = deque()
        dist[s] = 0
        q.append(s)
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
        return order, dist, parent

    def _dfs(self, u, vis, order):
        vis[u] = True
        order.append(u)
        for v in self.adj[u]:
            if not vis[v]:
                self._dfs(v, vis, order)

    def dfs(self, s):
        vis, order = [False] * self.n, []
        self._dfs(s, vis, order)
        return order

    def components(self):
        vis = [False] * self.n
        c = 0
        for i in range(self.n):
            if not vis[i]:
                c += 1
                self._dfs(i, vis, [])
        return c


def join(v):
    return " ".join(map(str, v))


def path_to(t, parent):
    p = []
    while t != -1:
        p.append(t)
        t = parent[t]
    return join(p[::-1])


def main():
    print("===== BAI 4.1: Danh sach lien ket don =====")
    L = SinglyLinkedList()
    L.push_back(10)
    L.push_back(20)
    L.push_front(5)
    L.push_back(30)
    check("pushBack 10,20; pushFront 5; pushBack 30", str(L), "[5 -> 10 -> 20 -> 30]")
    L.insert_at(2, 15)
    L.insert_at(0, 1)
    L.insert_at(L.size(), 99)
    check("insertAt(2,15), (0,1), (size,99)", str(L), "[1 -> 5 -> 10 -> 15 -> 20 -> 30 -> 99]")
    check("find(20), find(7)", f"{L.find(20)} {L.find(7)}", "4 -1")
    for x in (1, 15, 99):
        L.remove_value(x)
    r = L.remove_value(42)
    check("remove 1,15,99,42", f"{L} {'true' if r else 'false'}", "[5 -> 10 -> 20 -> 30] false")
    L.reverse()
    check("reverse", f"{L} size={L.size()}", "[30 -> 20 -> 10 -> 5] size=4")

    print("\n===== BAI 4.2: Ngan xep =====")
    st = ArrayStack(3)
    s = "E " if st.empty() else "N "
    for x in (1, 2, 3):
        st.push(x)
    over = st.push(4)
    s += ("F " if st.full() else "- ") + ("push4=ok " if over else "push4=overflow ")
    p1 = st.pop()
    p2 = st.pop()
    s += f"{p1}{p2} top={st.top()}"
    check("stack cap 3: push 1,2,3,4; pop x2", s, "E F push4=overflow 32 top=1")
    b = "".join("T" if is_balanced(e) else "F" for e in ("{[()()]}", "([)]", "((a+b)*c", "a[i] = f(x) + {y}", ")("))
    check("ngoac: {[()()]} ([)] ((a+b)*c ...", b, "TFFTF")
    check("hau to: 2 3 4 * + 5 -", str(eval_postfix("2 3 4 * + 5 -")), "9")
    check("hau to: 5 1 2 + 4 * + 3 -", str(eval_postfix("5 1 2 + 4 * + 3 -")), "14")
    check("hau to: 100 7 / 3 -", str(eval_postfix("100 7 / 3 -")), "11")

    print("\n===== BAI 4.3: Cay nhi phan tim kiem =====")
    T = BST()
    for k in (50, 30, 70, 20, 40, 60, 80, 35, 45, 65, 40):
        T.insert(k)
    check("inorder", T.inorder(), "20 30 35 40 45 50 60 65 70 80")
    check("preorder", T.preorder(), "50 30 20 40 35 45 70 60 65 80")
    check("height / min / max", f"{T.height()} {T.min_key()} {T.max_key()}", "4 20 80")
    check("contains 45, 55", ("T" if T.contains(45) else "F") + ("T" if T.contains(55) else "F"), "TF")
    T.remove(20)
    check("remove 20 (la)", T.preorder(), "50 30 40 35 45 70 60 65 80")
    T.remove(60)
    check("remove 60 (1 con)", T.preorder(), "50 30 40 35 45 70 65 80")
    T.remove(40)
    check("remove 40 (2 con)", T.preorder(), "50 30 45 35 70 65 80")
    T.remove(50)
    check("remove 50 (goc, 2 con)", f"{T.preorder()} | h={T.height()}", "65 30 45 35 70 80 | h=4")

    print("\n===== BAI 4.4: Do thi BFS / DFS =====")
    E = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (2, 6), (6, 5), (7, 8)]
    G = Graph(9, E)
    check("adj[3]", "".join(f"{v} " for v in G.adj[3]), "1 2 4 ")
    ob, dist, par = G.bfs(0)
    check("BFS(0) thu tu", join(ob), "0 1 2 3 6 4 5")
    check("dist tu 0 (0..8)", join(dist), "0 1 1 2 3 3 2 -1 -1")
    check("duong di ngan nhat 0 -> 5", path_to(5, par), "0 2 6 5")
    check("DFS(0) thu tu", join(G.dfs(0)), "0 1 3 2 6 5 4")
    check("so thanh phan lien thong", str(G.components()), "2")
    print(f"\nTONG: {passed}/{total} test dung")


if __name__ == "__main__":
    main()
