# =====================================================================
#  LAB 3B (VE NHA) - CHUONG 3: KY THUAT THIET KE GIAI THUAT
#  Muc do: 3B.1 De quy, 3B.2 Quay lui (Co ban) | 3B.3 Tham lam, 3B.4 QHD (Trung binh)
#          3B.5 Nhanh can, 3B.6 Chia de tri (Nang cao)
#  Chay:  python lab3B_ve_nha.py
# =====================================================================
import heapq
import sys
import time
from bisect import bisect_left
from itertools import permutations

sys.setrecursionlimit(10000)


class LCG:
    def __init__(self, seed):
        self.x = seed

    def next(self):
        self.x = (self.x * 1103515245 + 12345) & 0x7FFFFFFF
        return self.x

    def range(self, lo, hi):
        return lo + self.next() % (hi - lo + 1)


def time_ms(f):
    t0 = time.perf_counter()
    r = f()
    return r, (time.perf_counter() - t0) * 1000


# =====================================================================
# 3B.1 (CO BAN) - C(n,k) de quy thuan va co nho. Moi lan goi tang calls.
# =====================================================================
calls = 0


def binom_rec(n, k):
    global calls
    # TODO: viet code cua ban o day
    return 0


def binom_memo_helper(n, k, memo):
    global calls
    # TODO: viet code cua ban o day
    return 0


def binom_memo(n, k):
    return binom_memo_helper(n, k, [[-1] * (k + 1) for _ in range(n + 1)])


# =====================================================================
# 3B.2 (CO BAN) - Xau nhi phan do dai n khong co hai bit 1 lien ke (thu '0' truoc '1')
# =====================================================================
def gen_no_adj(n, cur, out):
    # TODO: viet code cua ban o day
    pass


# =====================================================================
# 3B.3 (TRUNG BINH) - So phong hop toi thieu. ms = list (ten, start, end).
#   Sap theo (start, end); min-heap (end, phong). Tra ve (so_phong, ms_da_sap, room).
# =====================================================================
def min_rooms(ms):
    # TODO: viet code cua ban o day
    return (0, ms, [0] * len(ms))


# =====================================================================
# 3B.4 (TRUNG BINH) - LIS: O(n^2) co truy vet (quy tac nhu ban C++) va O(n log n) do dai
# =====================================================================
def lis_n2(a):
    # TODO: viet code cua ban o day
    return []


def lis_nlogn(a):
    # TODO: viet code cua ban o day
    return 0


# =====================================================================
# 3B.5 (NANG CAO) - TSP: vet can va nhanh-can (can duoi cost + so_canh_con_lai * cmin)
# =====================================================================
bnb_nodes = 0


def tsp_brute(c):
    # TODO: viet code cua ban o day
    return 0


def tsp_bnb(c):
    """Tra ve (chi_phi_toi_uu, hanh_trinh bat dau bang 0)."""
    global bnb_nodes
    n = len(c)
    cmin = min(c[i][j] for i in range(n) for j in range(n) if i != j)
    used = [False] * n
    used[0] = True
    path = [0]
    best = [float("inf"), []]

    def bnb(last, k, cost):
        global bnb_nodes
        # TODO: viet code cua ban o day
        pass

    bnb(0, 1, 0)
    return best[0], best[1]


# =====================================================================
# 3B.6 (NANG CAO) - Cap diem gan nhat, tra ve BINH PHUONG khoang cach
# =====================================================================
def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def closest_brute(p):
    # TODO: viet code cua ban o day
    return 0


def closest_rec(p, lo, hi):
    """p[lo:hi] da sap theo x."""
    # TODO: viet code cua ban o day
    return 0


def closest_dc(p):
    p = sorted(p)
    return closest_rec(p, 0, len(p))


def random_points(n, seed):
    g = LCG(seed)
    out = []
    for _ in range(n):
        x = g.range(0, 1000000)
        y = g.range(0, 1000000)
        out.append((x, y))
    return out


def main():
    global calls, bnb_nodes
    print("===== 3B.1: To hop C(n,k) de quy =====")
    for n, k in ((5, 2), (10, 5), (20, 10), (26, 13)):
        calls = 0
        r1 = binom_rec(n, k)
        c1 = calls
        calls = 0
        r2 = binom_memo(n, k)
        c2 = calls
        print(f"C({n},{k}) = {r1}   calls rec = {c1}, calls memo = {c2}" + ("  [OK]" if r1 == r2 > 0 else "  [SAI]"))

    print("\n===== 3B.2: Xau nhi phan khong co hai bit 1 lien ke =====")
    out = []
    gen_no_adj(4, [], out)
    print("n = 4: " + " ".join(out) + f"  ({len(out)} xau)")
    f1, f2, ok, line = 1, 2, len(out) == 8, "So xau theo n:"
    for n in range(1, 21):
        o = []
        gen_no_adj(n, [], o)
        if n <= 10 or n == 20:
            line += f" {len(o)}"
        ok &= len(o) == f2
        f1, f2 = f2, f1 + f2
    print(line + ("  [OK]" if ok else "  [SAI]"))

    print("\n===== 3B.3: So phong hop toi thieu =====")
    ms = [("M1", 9, 11), ("M2", 9, 10), ("M3", 10, 12), ("M4", 11, 13), ("M5", 9, 12),
          ("M6", 13, 14), ("M7", 12, 15), ("M8", 14, 16), ("M9", 10, 11), ("M10", 15, 17)]
    r, ms2, room = min_rooms(ms)
    for (name, s, e), rm in zip(ms2, room):
        print(f"  {name:>4} [{s:>2},{e:>2}) -> phong {rm}")
    depth = max(sum(1 for _, s, e in ms if s <= t < e) for t in range(24))
    print(f"So phong = {r}, do chong lan lon nhat = {depth}" + ("  [OK]" if r == depth > 0 else "  [SAI]"))

    print("\n===== 3B.4: Day con tang dai nhat =====")
    for a in ([10, 9, 2, 5, 3, 7, 101, 18], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]):
        s = lis_n2(a)
        inc = bool(s) and all(s[i - 1] < s[i] for i in range(1, len(s)))
        print(f"  do dai {len(s)}, LIS = " + " ".join(map(str, s))
              + ("  [OK]" if inc and len(s) == lis_nlogn(a) else "  [SAI]"))
    g = LCG(4)
    a = [g.range(0, 100000) for _ in range(3000)]
    s1, t1 = time_ms(lambda: lis_n2(a))
    l2, t2 = time_ms(lambda: lis_nlogn(a))
    print(f"  n = 3000: O(n^2) -> {len(s1)} ({t1:.3f} ms), O(n log n) -> {l2} ({t2:.3f} ms)"
          + ("  [OK]" if len(s1) == l2 > 0 else "  [SAI]"))

    print("\n===== 3B.5: TSP - Nhanh va can =====")
    c5 = [[0, 3, 14, 18, 15], [3, 0, 4, 22, 20], [17, 9, 0, 16, 4], [6, 3, 7, 0, 12], [9, 15, 11, 5, 0]]
    bnb_nodes = 0
    b, path = tsp_bnb(c5)
    br5 = tsp_brute(c5)
    print(f"n = 5: brute = {br5}, B&B = {b}, hanh trinh: " + " ".join(map(str, path))
          + f" 0, so nut = {bnb_nodes}" + ("  [OK]" if b == br5 else "  [SAI]"))
    n, g = 10, LCG(10)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                c[i][j] = g.range(10, 99)
    br, tb = time_ms(lambda: tsp_brute(c))
    bnb_nodes = 0
    (bb, path), tn = time_ms(lambda: tsp_bnb(c))
    print(f"n = 10: brute = {br} (9! = 362880 hanh trinh, {tb:.3f} ms), B&B = {bb} ({bnb_nodes} nut, {tn:.3f} ms)"
          + ("  [OK]" if br == bb else "  [SAI]"))
    print("        hanh trinh: " + " ".join(map(str, path)) + " 0")

    print("\n===== 3B.6: Cap diem gan nhat =====")
    p = random_points(2000, 3)
    d1, d2 = closest_brute(p), closest_dc(p)
    print(f"n = 2000: brute d^2 = {d1}, chia de tri d^2 = {d2}" + ("  [OK]" if d1 == d2 else "  [SAI]"))
    q = random_points(50000, 9)                 # Python: 50 000 thay cho 200 000
    d, t = time_ms(lambda: closest_dc(q))
    print(f"n = 50000: d^2 = {d}, {t:.3f} ms")


if __name__ == "__main__":
    main()
