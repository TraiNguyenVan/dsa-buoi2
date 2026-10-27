# =====================================================================
#  LAB 3A (TREN LOP) - CHUONG 3: KY THUAT THIET KE GIAI THUAT
#  3.1 Sinh ke tiep | 3.2 Quay lui | 3.3 Quy hoach dong
#  Chay:  python lab3A_thiet_ke_giai_thuat.py
# =====================================================================
from math import comb


# =====================================================================
# BAI 3.1 - Sinh ke tiep: to hop chap k cua {1..n} theo thu tu tu dien
#   next_combination(c, n): sua c thanh cau hinh ke tiep; tra ve False neu c la cau hinh cuoi.
#   Y tuong: tim i lon nhat co c[i] < n - k + i + 1, tang c[i], dat c[j] = c[j-1] + 1 voi j > i.
# =====================================================================
def next_combination(c, n):
    k = len(c)
    i = k - 1
    while i >= 0 and c[i] == n - k + i + 1:
        i -= 1
    if i < 0:
        return False
    c[i] += 1
    for j in range(i + 1, k):
        c[j] = c[j - 1] + 1
    return True


# =====================================================================
# BAI 3.2 - Quay lui: tap con cua a (DA SAP TANG) co tong = S
#   nodes tang 1 moi lan GOI try_subset. prune=True -> gap sum + a[j] > S thi break.
# =====================================================================
nodes = 0
found = []


def try_subset(a, S, start, total, cur, prune):
    global nodes
    nodes += 1
    for j in range(start, len(a)):
        nt = total + a[j]
        if prune and nt > S:
            break
        if nt == S:
            cur.append(a[j])
            found.append(cur.copy())
            cur.pop()
        cur.append(a[j])
        try_subset(a, S, j + 1, nt, cur, prune)
        cur.pop()


# =====================================================================
# BAI 3.3 - QHD: xau con chung dai nhat (LCS). Quy tac truy vet: xem ban C++ / tai lieu.
# =====================================================================
def lcs_table(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L


def lcs_trace(X, Y, L):
    res = []
    i, j = len(X), len(Y)
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            res.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))


def is_subseq(Z, X):
    it = iter(X)
    return all(c in it for c in Z)


def main():
    global nodes
    print("===== BAI 3.1: Sinh to hop chap k cua n =====")
    n, k = 5, 3
    c = list(range(1, k + 1))
    cnt = 0
    while True:
        cnt += 1
        print(f"{cnt:>3}:" + "".join(f" {x}" for x in c))
        if not next_combination(c, n):
            break
    print(f"So to hop C(5,3) = {cnt}" + ("  [OK]" if cnt == comb(5, 3) else "  [SAI]"))
    ok = True
    for nn, kk in ((10, 4), (12, 6), (20, 3)):
        d, t = list(range(1, kk + 1)), 1
        while next_combination(d, nn):
            t += 1
        print(f"C({nn},{kk}): sinh duoc {t}, cong thuc {comb(nn, kk)}")
        ok &= t == comb(nn, kk)
    print("[OK]" if ok else "[SAI]")

    print("\n===== BAI 3.2: Quay lui - tap con co tong S =====")
    a, S = list(range(1, 11)), 15
    found.clear()
    nodes = 0
    try_subset(a, S, 0, 0, [], False)
    nodes_no, cnt_no = nodes, len(found)
    found.clear()
    nodes = 0
    try_subset(a, S, 0, 0, [], True)
    print(f"a = 1..10, S = 15: so tap con = {len(found)}")
    line = ""
    for i, f in enumerate(found):
        line += "  {" + ",".join(map(str, f)) + "}"
        if i % 5 == 4:
            print(line)
            line = ""
    if line:
        print(line)
    print(f"So nut KHONG cat nhanh = {nodes_no} | CO cat nhanh = {nodes}"
          + ("  [OK]" if cnt_no == len(found) == 20 else "  [SAI]"))

    print("\n===== BAI 3.3: QHD - Xau con chung dai nhat =====")
    for X, Y in (("ABCBDAB", "BDCABA"), ("QUYHOACHDONG", "QUAYLUINHANHCAN"), ("AGGTAB", "GXTXAYB")):
        L = lcs_table(X, Y)
        z = lcs_trace(X, Y, L)
        ok = len(z) == L[len(X)][len(Y)] and is_subseq(z, X) and is_subseq(z, Y) and z != ""
        print(f"{X} / {Y} -> do dai {L[len(X)][len(Y)]}, LCS = {z}" + ("  [OK]" if ok else "  [SAI]"))
        if X == "ABCBDAB":
            print("     " + "".join(f"{ch:>3}" for ch in Y))
            for i in range(1, len(X) + 1):
                print(f"  {X[i - 1]}  " + "".join(f"{L[i][j]:>3}" for j in range(1, len(Y) + 1)))


if __name__ == "__main__":
    main()
