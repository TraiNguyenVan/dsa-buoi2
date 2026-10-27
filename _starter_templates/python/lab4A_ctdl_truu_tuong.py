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
        # TODO: viet code cua ban o day
        pass

    def push_back(self, x):
        # TODO: viet code cua ban o day
        pass

    def insert_at(self, pos, x):
        """Chen de x nam o vi tri pos (0..count). Sai vi tri -> False."""
        # TODO: viet code cua ban o day
        return False

    def find(self, x):
        # TODO: viet code cua ban o day
        return -1

    def remove_value(self, x):
        """Xoa nut DAU TIEN co data == x."""
        # TODO: viet code cua ban o day
        return False

    def reverse(self):
        # TODO: viet code cua ban o day
        pass


# =====================================================================
# BAI 4.2 - Ngan xep bang MANG co dinh dung luong + ung dung
# =====================================================================
class ArrayStack:
    def __init__(self, capacity):
        self.a = [None] * capacity
        self.top_idx = -1

    def empty(self):
        # TODO: viet code cua ban o day
        return True

    def full(self):
        # TODO: viet code cua ban o day
        return False

    def push(self, x):
        """False neu day (overflow)."""
        # TODO: viet code cua ban o day
        return False

    def pop(self):
        # TODO: viet code cua ban o day
        return 0

    def top(self):
        # TODO: viet code cua ban o day
        return 0


def is_balanced(s):
    # TODO: viet code cua ban o day
    return False


def eval_postfix(expr):
    """Token cach nhau dau cach; + - * / (chia nguyen, lam tron ve 0 nhu C++)."""
    # TODO: viet code cua ban o day
    return 0


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
        # TODO: viet code cua ban o day
        return t

    def insert(self, k):
        self.root = self._insert(self.root, k)

    def contains(self, k):
        # TODO: viet code cua ban o day
        return False

    def min_key(self):
        # TODO: viet code cua ban o day
        return 0

    def max_key(self):
        # TODO: viet code cua ban o day
        return 0

    def _height(self, t):
        # TODO: viet code cua ban o day
        return 0

    def height(self):
        return self._height(self.root)

    def _inorder(self, t, out):
        # TODO: viet code cua ban o day
        pass

    def _preorder(self, t, out):
        # TODO: viet code cua ban o day
        pass

    def inorder(self):
        out = []
        self._inorder(self.root, out)
        return " ".join(map(str, out))

    def preorder(self):
        out = []
        self._preorder(self.root, out)
        return " ".join(map(str, out))

    def _remove(self, t, k):
        # TODO: viet code cua ban o day
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
        # TODO: viet code cua ban o day
        pass

    def bfs(self, s):
        """Tra ve (order, dist, parent)."""
        order, dist, parent = [], [-1] * self.n, [-1] * self.n
        # TODO: viet code cua ban o day
        pass
        return order, dist, parent

    def _dfs(self, u, vis, order):
        # TODO: viet code cua ban o day
        pass

    def dfs(self, s):
        vis, order = [False] * self.n, []
        self._dfs(s, vis, order)
        return order

    def components(self):
        # TODO: viet code cua ban o day
        return 0


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
