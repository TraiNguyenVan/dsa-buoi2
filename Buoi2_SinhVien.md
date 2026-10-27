INT1306_CLC · Lab CTDL & GT · Buổi 2 · Tài liệu sinh viên

**HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG — CƠ SỞ TP.HCM**

Khoa Công nghệ Thông tin 2

**Bài thực hành — Buổi 2**

Chương 3 & 4 · Cấu trúc dữ liệu và Giải thuật (INT1306_CLC)

**Tài liệu dành cho sinh viên** · Học kỳ 1, năm học 2026–2027

Lab trên lớp 3A, 4A · Lab về nhà 3B, 4B

Mã nguồn: **C++17** và **Python 3.8+** — mỗi bài đều có file khung (starter) chạy được ngay

Giảng viên: Lê Ngọc Hiếu — lnhieu@ptit.edu.vn

# Mục lục

**Phần 0. Hướng dẫn chung**

0.1 Tổng quan các bài thực hành

0.2 Chuẩn bị môi trường

0.3 Cách làm một bài lab

0.4 Nộp bài và đánh giá

**Phần 1. Lab trên lớp — Buổi 2 (Chương 3 và Chương 4)**

Lab 3A — Kỹ thuật thiết kế giải thuật

Lab 4A — Cấu trúc dữ liệu trừu tượng

**Phần 2. Lab về nhà — Chương 3 và 4**

Lab 3B — Kỹ thuật thiết kế giải thuật (nâng cao)

Lab 4B — Cấu trúc dữ liệu trừu tượng (nâng cao)

**Phụ lục A. Mẫu phiếu báo cáo**

**Phụ lục B. Lỗi thường gặp**

# Phần 0. Hướng dẫn chung

## 0.1 Tổng quan các bài thực hành

Theo đề cương học phần, phần thực hành bám theo bốn chương lý thuyết. Mỗi chương có **một bài lab trên lớp** (làm có giảng viên hướng dẫn, nộp cuối buổi) và **một bài lab về nhà** chia ba mức Cơ bản → Trung bình → Nâng cao (nộp sau một tuần).

| **Buổi** | **Chương** | **Lab trên lớp** | **Phút** | **Lab về nhà** |
| --- | --- | --- | --- | --- |
| Buổi 1 | 1. Giới thiệu CTDL & GT | 1A — Đặc tả, đếm phép toán, thực nghiệm nhân đôi n | 45 | 1B — Tìm kiếm tuyến tính, lũy thừa nhanh, Fibonacci, 3-SUM |
| Buổi 1 | 2. Sắp xếp & tìm kiếm | 2A — 5 thuật toán sắp xếp, tìm kiếm nhị phân, bảng băm | 65 | 2B — Radix, nội suy, median-of-3, bảng băm tự cài, nghịch thế, quickselect |
| Buổi 2 | 3. Kỹ thuật thiết kế GT | 3A — Sinh kế tiếp, quay lui, quy hoạch động (LCS) | 55 | 3B — Đệ quy, quay lui, tham lam, LIS, nhánh cận TSP, chia để trị |
| Buổi 2 | 4. CTDL trừu tượng | 4A — DSLK đơn, ngăn xếp, BST, BFS/DFS | 60 | 4B — DSLK kép/vòng, hàng đợi vòng, heap, shunting-yard, Dijkstra, Kruskal, AVL |

**Phân bổ thời gian mỗi buổi (120 phút).** Buổi 1: 10 phút giảng viên kiểm tra môi trường + 45 phút Lab 1A + 65 phút Lab 2A. Buổi 2: 55 phút Lab 3A + 60 phút Lab 4A + 5 phút nộp bài.

## 0.2 Chuẩn bị môi trường

- **C++:** trình biên dịch hỗ trợ **C++17** — g++ ≥ 7 (MinGW-w64 trên Windows, có sẵn trong Code::Blocks / Dev-C++ 6.x / VS Code), hoặc Visual Studio 2019 trở lên. Trong Dev-C++ cần bật -std=c++17 ở Tools → Compiler Options.
- **Python:** Python **3.8 trở lên** (bài 3A dùng math.comb). Không cần cài thêm thư viện ngoài.
- Kiểm tra trước buổi học: biên dịch và chạy thử file starter/cpp/lab3A_thiet_ke_giai_thuat.cpp. Nếu chạy được và in ra các dòng \[SAI] là môi trường đã sẵn sàng.

\# C++ (dong lenh)\
g++ -O2 -std=c++17 -Wall -o lab3A lab3A_thiet_ke_giai_thuat.cpp\
./lab3A                 # Windows: lab3A.exe\

\# Python\
python lab3A_thiet_ke_giai_thuat.py          # hoac: python3 ...

## 0.3 Cách làm một bài lab

1. Chọn **một** ngôn ngữ (C++ hoặc Python) cho bài trên lớp. Bài về nhà làm bằng ngôn ngữ đã chọn; làm thêm ngôn ngữ thứ hai được cộng điểm thưởng.
2. Mở file khung trong thư mục starter/. Mỗi chỗ cần viết code được đánh dấu // TODO: viet code cua ban o day (Python: # TODO). Đọc kỹ chú thích phía trên mỗi hàm — đó là **đặc tả** (input, output, quy tắc đếm).
3. File khung **đã biên dịch được** và có sẵn hàm main() kiểm thử. Khi chưa làm, chương trình in \[SAI]; làm đúng sẽ in \[OK]. **Không sửa \`main()\`** và không sửa dữ liệu test.
4. Làm lần lượt từng hàm, chạy lại sau mỗi hàm. Đừng viết hết rồi mới chạy.
5. Trả lời các **câu hỏi** cuối mỗi bài vào phiếu báo cáo (Phụ lục A). Câu hỏi chiếm một phần điểm — code chạy đúng mà không giải thích được vẫn chưa đủ.

**Quy tắc chung.**  Không dùng hàm thư viện làm sẵn cho chính thứ mà bài yêu cầu cài đặt: không gọi sort() trong bài sắp xếp, không dùng heapq / priority_queue trong bài tự cài heap (4B.4), không dùng dict / unordered_map trong bài tự cài bảng băm (2B.4), không dùng list.append/pop thay cho chỉ số top trong bài ngăn xếp bằng mảng (4A.2). Các chỗ được phép dùng thư viện đã ghi rõ trong đặc tả.

**Dữ liệu ngẫu nhiên.**  Mọi dữ liệu ngẫu nhiên đều sinh từ cùng một bộ sinh LCG có trong file, nên bản C++ và bản Python cho **cùng một kết quả đếm**. Chỉ các cột thời gian (ms) là khác nhau giữa các máy.

## 0.4 Nộp bài và đánh giá

| **Loại** | **Nộp gì** | **Hạn** | **Đặt tên** |
| --- | --- | --- | --- |
| Lab trên lớp (1A, 2A, 3A, 4A) | File mã nguồn đã hoàn thành + file kết quả chạy (output.txt) + phiếu trả lời | Cuối buổi | MSSV_Lab1A.cpp / .py<br>MSSV_Lab1A_output.txt |
| Lab về nhà (1B, 2B, 3B, 4B) | Như trên, nén thành một file .zip | 7 ngày sau buổi học | MSSV_HoTen_Lab1B.zip |

Lưu kết quả chạy ra file: ./lab1A > MSSV_Lab1A_output.txt (Python: python lab1A_do_phuc_tap.py > MSSV_Lab1A_output.txt).

**Thang điểm.** Mỗi lab trên lớp: 10 điểm (code chạy đúng  *70%, câu hỏi*  30%). Mỗi lab về nhà: Cơ bản 5 điểm, Trung bình 3 điểm, Nâng cao 2 điểm; bài Thử thách (nếu có) cộng tối đa 1 điểm. Điểm thực hành thuộc thành phần **Bài tập 20%** của học phần.

**Liêm chính học thuật.**  Được thảo luận ý tưởng với bạn, nhưng code phải tự viết. Hai bài nộp giống nhau bất thường sẽ được giảng viên hỏi vấn đáp trực tiếp; không giải thích được code của mình thì bài nhận 0 điểm.

# Phần 1. Lab trên lớp — Buổi 2 (Chương 3 và Chương 4)

## Lab 3A — Kỹ thuật thiết kế giải thuật

| **Mục** | **Nội dung** |
| --- | --- |
| File khung | starter/cpp/lab3A_thiet_ke_giai_thuat.cpp   ·   starter/python/lab3A_thiet_ke_giai_thuat.py |
| Thời lượng | 55 phút (3.1: 15’ · 3.2: 20’ · 3.3: 20’) |
| Mục tiêu | Phương pháp sinh kế tiếp (mục 3.1)<br>Quay lui và cắt nhánh (mục 3.3)<br>Quy hoạch động có truy vết (mục 3.7) |

### Bài 3.1. Sinh kế tiếp: tổ hợp chập k của n  (15 phút)

**Kiến thức cần nhớ**

- Phương pháp sinh cần: (1) cấu hình đầu, (2) cách nhận biết cấu hình cuối, (3) thuật toán sinh cấu hình kế tiếp.
- Tổ hợp chập k của {1..n} theo thứ tự từ điển: đầu 1 2 … k, cuối n−k+1 … n. Phần tử c\[i] (chỉ số từ 0) đạt giá trị lớn nhất có thể là n − k + i + 1.

**Đề bài**

Cài nextCombination(c, n): biến c thành cấu hình kế tiếp, trả về false nếu c đã là cấu hình cuối.

**Hướng dẫn từng bước**

1. Từ phải sang trái, tìm i lớn nhất có c\[i] < n − k + i + 1.
2. Nếu không có i → cấu hình cuối, trả về false.
3. Tăng c\[i] lên 1; đặt c\[j] = c\[j−1] + 1 với mọi j > i.
4. Chạy: phải in đủ 10 tổ hợp của C(5,3), từ 1 2 3 đến 3 4 5.

**Kết quả cần đạt**

- C(10,4) = 210, C(12,6) = 924, C(20,3) = 1140 — số sinh được khớp công thức.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Sau 1 4 5 là cấu hình nào? Chạy tay thuật toán để giải thích.
2. Độ phức tạp sinh toàn bộ C(n,k) tổ hợp là bao nhiêu?
3. Thay đổi những gì để thuật toán sinh các xâu nhị phân độ dài n?

### Bài 3.2. Quay lui: tập con có tổng bằng S  (20 phút)

**Đề bài**

Cho mảng a đã sắp tăng (a = 1..10) và S = 15. Cài trySubset(start, sum): với j = start..n−1, chọn a\[j]; nếu tổng mới = S thì ghi nhận tập con; luôn gọi đệ quy trySubset(j+1, sum + a\[j]). Biến nodes tăng 1 mỗi lần **gọi** hàm.

Tham số prune: nếu true thì khi sum + a\[j] > S dừng vòng lặp (break) vì các phần tử sau còn lớn hơn; nếu false thì không cắt.

**Hướng dẫn từng bước**

1. Vẽ cây quay lui cho a = {1, 2, 3}, S = 3 trên giấy.
2. Cài phần chọn / gọi đệ quy / bỏ chọn (push_back – gọi – pop_back).
3. Thêm điều kiện cắt nhánh khi prune = true.
4. Chạy và so sánh hai con số nodes.

**Kết quả cần đạt**

- Có đúng **20** tập con; số nút: không cắt 1024, có cắt 119.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao khi không cắt nhánh số nút đúng bằng 2¹⁰?
2. Điều kiện break chỉ đúng khi mảng đã sắp tăng. Nếu mảng chưa sắp thì phải sửa thế nào?
3. Độ phức tạp trường hợp xấu nhất của thuật toán quay lui này?

### Bài 3.3. Quy hoạch động: xâu con chung dài nhất (LCS)  (20 phút)

**Kiến thức cần nhớ**

- L\[i]\[j] = L\[i−1]\[j−1] + 1 nếu X\[i−1] = Y\[j−1]; ngược lại L\[i]\[j] = max(L\[i−1]\[j], L\[i]\[j−1]).
- Truy vết từ (m, n): ký tự bằng nhau → lấy ký tự, đi chéo; ngược lại nếu L\[i−1]\[j] >= L\[i]\[j−1] đi **lên**, còn lại đi **trái**. Quy tắc này làm kết quả duy nhất.

**Đề bài**

Cài lcsTable (điền bảng) và lcsTrace (truy vết). Chương trình in bảng L cho ví dụ kinh điển ABCBDAB / BDCABA.

**Hướng dẫn từng bước**

1. Điền tay 3 hàng đầu của bảng L cho ví dụ kinh điển.
2. Cài hai vòng for điền bảng.
3. Cài truy vết, nhớ đảo ngược xâu kết quả.
4. Chạy: ba test đều \[OK].

**Kết quả cần đạt**

- ABCBDAB / BDCABA → độ dài 4, LCS = BCBA.
- AGGTAB / GXTXAYB → GTAB.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Độ phức tạp thời gian và bộ nhớ? So với cách vét cạn mọi dãy con của X.
2. Nếu chỉ cần độ dài, có thể giảm bộ nhớ xuống bao nhiêu? Mô tả cách làm.
3. Đổi quy tắc truy vết thành > thay cho >= thì LCS của ví dụ kinh điển là gì? Nhận xét về tính duy nhất của LCS.

## Lab 4A — Cấu trúc dữ liệu trừu tượng

| **Mục** | **Nội dung** |
| --- | --- |
| File khung | starter/cpp/lab4A_ctdl_truu_tuong.cpp   ·   starter/python/lab4A_ctdl_truu_tuong.py |
| Thời lượng | 60 phút (mỗi bài 15’) |
| Mục tiêu | Cài đặt danh sách liên kết đơn, ngăn xếp bằng mảng (LO3)<br>Cây nhị phân tìm kiếm: chèn, tìm, duyệt, xóa 3 trường hợp<br>Đồ thị: danh sách kề, BFS, DFS, thành phần liên thông |

Mỗi phép kiểm thử in một dòng \[OK] / \[SAI] can: … (giá trị mong đợi). Cuối chương trình in TONG: x/24 test dung.

### Bài 4.1. Danh sách liên kết đơn  (15 phút)

**Đề bài**

Hoàn thành lớp SinglyLinkedList: pushFront, pushBack, insertAt(pos, x) (chèn để x nằm ở vị trí pos, 0 ≤ pos ≤ size), find(x) (vị trí đầu tiên hoặc −1), removeValue(x) (xóa nút đầu tiên), reverse() (đảo tại chỗ, bộ nhớ O(1)).

**Hướng dẫn từng bước**

1. Vẽ hình con trỏ trước khi viết mỗi hàm.
2. removeValue: duy trì hai con trỏ prev và cur; chú ý trường hợp xóa nút đầu.
3. reverse: ba con trỏ prev, cur, next.
4. C++: nhớ delete nút bị xóa.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Độ phức tạp của từng thao tác? Làm sao để pushBack thành O(1)?
2. So sánh danh sách liên kết với mảng khi chèn ở đầu và khi truy cập phần tử thứ i.

### Bài 4.2. Ngăn xếp bằng mảng và ứng dụng  (15 phút)

**Đề bài**

Cài lớp ArrayStack dung lượng cố định (dùng chỉ số topIdx, rỗng khi topIdx = −1). Dùng nó để viết: (a) isBalanced(s) kiểm tra ngoặc () \[] {} cân bằng; (b) evalPostfix(expr) tính biểu thức hậu tố, các token cách nhau dấu cách, phép chia là chia nguyên.

**Hướng dẫn từng bước**

1. push trả về false khi đầy (tràn ngăn xếp).
2. isBalanced: gặp ngoặc mở → push; gặp ngoặc đóng → ngăn xếp phải không rỗng và đỉnh phải là ngoặc mở tương ứng; cuối cùng ngăn xếp phải rỗng.
3. evalPostfix: gặp số → push; gặp toán tử → pop **b** trước rồi pop **a**, push a op b.

**Kết quả cần đạt**

- 2 3 4 * + 5 - = 9; 5 1 2 + 4 * + 3 - = 14.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao phải lấy b trước a? Điều gì xảy ra với phép trừ nếu đảo thứ tự?
2. Viết dạng hậu tố của (2 + 3) × (7 − 4) và tính giá trị.

### Bài 4.3. Cây nhị phân tìm kiếm (BST)  (15 phút)

**Kiến thức cần nhớ**

- Chiều cao = số **nút** trên đường đi dài nhất từ gốc (cây rỗng = 0, một nút = 1).
- Xóa nút có 2 con: thay khóa bằng nút **nhỏ nhất của cây con phải** (successor) rồi xóa nút đó.

**Đề bài**

Cài insertRec, contains (dạng lặp), minKey, maxKey, heightRec, inorderRec, preorderRec, removeRec. Dữ liệu: chèn 50 30 70 20 40 60 80 35 45 65 40 (khóa 40 trùng phải bị bỏ qua), rồi xóa lần lượt 20 (lá), 60 (1 con), 40 (2 con), 50 (gốc).

**Hướng dẫn từng bước**

1. Vẽ cây sau khi chèn và sau mỗi lần xóa.
2. Cài chèn và duyệt trước, kiểm tra inorder ra dãy tăng.
3. Cài xóa theo 3 trường hợp.

**Kết quả cần đạt**

- Preorder ban đầu 50 30 20 40 35 45 70 60 65 80; sau khi xóa 50: 65 30 45 35 70 80.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Duyệt inorder của BST luôn cho dãy gì? Vì sao?
2. Chèn các khóa 1, 2, …, n theo thứ tự tăng thì cây có hình dạng gì, chiều cao bao nhiêu? Cấu trúc nào khắc phục (xem bài 4B.8)?

### Bài 4.4. Đồ thị: BFS, DFS, thành phần liên thông  (15 phút)

**Đề bài**

Đồ thị vô hướng 9 đỉnh, cạnh (0,1) (0,2) (1,3) (2,3) (3,4) (4,5) (2,6) (6,5) (7,8). Cài: hàm dựng danh sách kề (**sắp tăng** danh sách kề của mỗi đỉnh để thứ tự duyệt là duy nhất), bfs(s) trả về thứ tự thăm, dist (số cạnh ít nhất) và parent; dfsRec đệ quy; components() đếm số thành phần liên thông.

**Hướng dẫn từng bước**

1. Vẽ đồ thị trên giấy, chạy tay BFS từ 0.
2. BFS dùng hàng đợi; đánh dấu dist\[v] ngay khi **đưa vào** hàng đợi.
3. DFS đệ quy theo thứ tự danh sách kề.
4. components: gọi DFS từ mỗi đỉnh chưa thăm.

**Kết quả cần đạt**

- BFS(0): 0 1 2 3 6 4 5; DFS(0): 0 1 3 2 6 5 4; đường đi ngắn nhất 0 → 5: 0 2 6 5.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao BFS cho đường đi ít cạnh nhất còn DFS thì không?
2. Độ phức tạp BFS/DFS với danh sách kề và với ma trận kề?
3. Liệt kê các thành phần liên thông của đồ thị.

# Phần 2. Lab về nhà — Chương 3 và 4

Mỗi bài về nhà có các mức **Cơ bản** (bắt buộc, 5 điểm), **Trung bình** (3 điểm), **Nâng cao** (2 điểm). Làm theo thứ tự — bài sau thường dùng kết quả của bài trước. Hạn nộp: 7 ngày sau buổi học tương ứng.

## Lab 3B — Kỹ thuật thiết kế giải thuật (nâng cao)

| **Mục** | **Nội dung** |
| --- | --- |
| File khung | starter/cpp/lab3B_ve_nha.cpp   ·   starter/python/lab3B_ve_nha.py |
| Thời lượng | Về nhà · khoảng 4 giờ |
| Mục tiêu | Đệ quy có nhớ, quay lui có ràng buộc<br>Tham lam có chứng minh, QHĐ có truy vết<br>Nhánh và cận, chia để trị hình học |

### Bài 3B.1. Đệ quy: tổ hợp C(n, k)  \[Cơ bản]

**Đề bài**

Cài binomRec (đệ quy theo công thức Pascal) và binomMemoHelper (có bảng nhớ −1 = chưa tính), cả hai tăng calls mỗi lần gọi.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Chứng minh số lời gọi của binomRec(n,k) là 2·C(n,k) − 1.
2. Số lời gọi của bản có nhớ xấp xỉ bao nhiêu? Độ phức tạp?

### Bài 3B.2. Quay lui: xâu nhị phân không có hai bit 1 liền kề  \[Cơ bản]

**Đề bài**

Cài genNoAdj(n) liệt kê các xâu độ dài n không có hai bit 1 kề nhau, thử bit 0 trước bit 1 (bit 1 chỉ được chọn khi bit trước không phải 1).

**Kết quả cần đạt**

- n = 4 → 8 xâu: 0000 0001 0010 0100 0101 1000 1001 1010.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Dãy số lượng 2, 3, 5, 8, 13, … là dãy gì? Chứng minh bằng hệ thức truy hồi.
2. So sánh số nút của cây quay lui này với cây sinh mọi xâu nhị phân.

### Bài 3B.3. Tham lam: số phòng họp tối thiểu  \[Trung bình]

**Đề bài**

Cài minRooms: sắp các cuộc họp theo (start, end); duy trì min-heap các cặp (giờ kết thúc, số phòng). Nếu phòng kết thúc sớm nhất có end ≤ start thì dùng lại, ngược lại mở phòng mới (đánh số từ 1). Ở bài này **được dùng** priority_queue / heapq.

**Kết quả cần đạt**

- 10 cuộc họp cần 4 phòng.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Chứng minh thuật toán tối ưu (gợi ý: số phòng ≥ số cuộc họp chồng lấn tại một thời điểm).
2. Độ phức tạp?
3. Chiến lược tham lam “sắp theo giờ kết thúc” có cho đáp án đúng cho bài này không? Thử với dữ liệu đã cho.

### Bài 3B.4. QHĐ: dãy con tăng dài nhất (LIS)  \[Trung bình]

**Đề bài**

Cài lisN2 (QHĐ O(n²) có truy vết; quy tắc chọn predecessor và điểm kết thúc ghi rõ trong chú thích để kết quả duy nhất) và lisNlogN (mảng tails + tìm kiếm nhị phân, chỉ trả về độ dài).

**Kết quả cần đạt**

- 10 9 2 5 3 7 101 18 → độ dài 4, LIS = 2 5 7 101.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Viết công thức truy hồi và giải thích ý nghĩa dp\[i].
2. Mảng tails có phải là một dãy LIS thật không? Giải thích bất biến của tails.

### Bài 3B.5. Nhánh và cận: bài toán người du lịch (TSP)  \[Nâng cao]

**Đề bài**

Cài tspBrute (duyệt mọi hoán vị của 1..n−1) và bnb (quay lui, chọn thành phố theo chỉ số tăng, bnbNodes tăng mỗi lần gọi). Cận dưới tại nút con: cost + (số cạnh còn lại) × cmin, với cmin là cạnh nhỏ nhất của ma trận; cắt nhánh nếu cận ≥ best.

**Kết quả cần đạt**

- Ma trận 5 thành phố: chi phí tối ưu 22.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Với n = 10, nhánh cận duyệt bao nhiêu nút so với 9! = 362 880 hành trình của vét cạn?
2. Đề xuất một cận dưới chặt hơn (ví dụ dùng cạnh nhỏ nhất đi ra từ mỗi thành phố chưa thăm). Cài thử và so sánh số nút (không bắt buộc).

### Bài 3B.6. Chia để trị: cặp điểm gần nhất  \[Nâng cao]

**Đề bài**

Cài closestBrute O(n²) và closestRec: chia đôi theo x, d = min(hai nửa), xét dải |x − x_mid| < d sắp theo y, mỗi điểm chỉ so với các điểm sau có (Δy)² < d. Kết quả là **bình phương khoảng cách** (số nguyên) để tránh sai số.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao mỗi điểm trong dải chỉ cần so với hằng số điểm kế tiếp?
2. Phiên bản này là O(n log² n). Sửa thế nào để đạt O(n log n)?

## Lab 4B — Cấu trúc dữ liệu trừu tượng (nâng cao)

| **Mục** | **Nội dung** |
| --- | --- |
| File khung | starter/cpp/lab4B_ve_nha.cpp   ·   starter/python/lab4B_ve_nha.py |
| Thời lượng | Về nhà · khoảng 5 giờ |
| Mục tiêu | Các biến thể danh sách liên kết và hàng đợi (4.1, 4.3)<br>Heap và ứng dụng ngăn xếp (4.2, 4.4.5)<br>Đường đi ngắn nhất, cây khung nhỏ nhất, cây AVL (4.4.4, 4.5.6, 4.5.7) |

### Bài 4B.1. Danh sách liên kết kép có thứ tự  \[Cơ bản]

**Đề bài**

Lớp SortedDList luôn giữ dãy tăng: insert(x) chèn sau các phần tử ≤ x; remove(x) xóa nút đầu tiên bằng x. Cập nhật đúng cả prev, next, head, tail — chương trình kiểm tra cả chiều xuôi và chiều ngược.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Liệt kê 4 trường hợp con trỏ khi xóa một nút trong DSLK kép.
2. Vì sao DSLK có thứ tự không giúp tìm kiếm nhị phân được?

### Bài 4B.2. Danh sách liên kết vòng: bài toán Josephus  \[Cơ bản]

**Đề bài**

n người 1..n đứng thành vòng, người thứ k bị loại, đếm tiếp từ người kế. Dùng DSLK vòng tự cài để trả về thứ tự bị loại (phần tử cuối = người sống sót).

**Kết quả cần đạt**

- n = 7, k = 3: 3 6 2 7 5 1 4.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Độ phức tạp theo n và k?
2. Tìm hiểu công thức truy hồi J(n,k) = (J(n−1,k) + k) mod n và kiểm chứng với n = 41, k = 3.

### Bài 4B.3. Hàng đợi vòng và cửa sổ trượt  \[Cơ bản]

**Đề bài**

Cài CircularQueue bằng mảng (chỉ số front và count, vị trí cuối = (front + count) mod cap). Sau đó cài slidingMax(a, k) dùng deque chứa chỉ số với giá trị giảm dần — O(n).

**Kết quả cần đạt**

- \[1 3 -1 -3 5 3 6 7], k = 3 → 3 3 5 5 6 7.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao hàng đợi bằng mảng thường (không vòng) bị lãng phí bộ nhớ?
2. Chứng minh slidingMax là O(n) dù có vòng while lồng trong for.

### Bài 4B.4. Heap, heap sort và top-k  \[Trung bình]

**Đề bài**

Tự cài MinHeap (push + siftUp, pop + siftDown), heapSort tại chỗ (xây max-heap O(n) rồi đưa max về cuối), và topK(a, k) dùng min-heap kích thước k. Không dùng heapq / priority_queue.

**Kết quả cần đạt**

- Mảng heap sau khi push 5 3 8 1 9 2: 1 3 2 5 9 8.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao xây heap từ dưới lên là O(n) chứ không phải O(n log n)?
2. topK có độ phức tạp bao nhiêu? So với việc sắp xếp toàn bộ rồi lấy k phần tử.

### Bài 4B.5. Trung tố → hậu tố (shunting-yard)  \[Trung bình]

**Đề bài**

Cài infixToPostfix với toán hạng nhiều chữ số hoặc một chữ cái, toán tử + - (ưu tiên 1), * / (2), ^ (3, **kết hợp phải**) và ngoặc; rồi evalPostfix cho số nguyên.

**Kết quả cần đạt**

- 3+4*2/(1-5)^2^3 → 3 4 2 * 1 5 - 2 3 ^ ^ / +; 2^3^2 = 512.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Điều kiện pop toán tử khỏi ngăn xếp khác nhau thế nào giữa toán tử kết hợp trái và kết hợp phải?
2. Chuyển tay biểu thức a*(b+c)-d/e và đối chiếu với chương trình.

### Bài 4B.6. Dijkstra và Floyd-Warshall  \[Nâng cao]

**Đề bài**

Cài dijkstra với hàng đợi ưu tiên (bỏ qua bản ghi cũ — lazy deletion), trả về khoảng cách và parent; cài floydWarshall để **kiểm chứng**: hàng s của ma trận Floyd phải trùng với kết quả Dijkstra từ s, trên đồ thị mẫu và đồ thị ngẫu nhiên 200 đỉnh.

**Kết quả cần đạt**

- Đồ thị mẫu: dist từ 0 = 0 3 1 4 7 8, đường đi 0 → 5 = 0 2 1 3 4 5.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao Dijkstra sai khi có cạnh âm? Cho ví dụ 3 đỉnh. Thuật toán nào xử lý được (mục 4.5.6.2)?
2. So sánh độ phức tạp: Dijkstra chạy n lần vs Floyd-Warshall một lần, trên đồ thị thưa và đồ thị dày.

### Bài 4B.7. Cây khung nhỏ nhất: Kruskal và Prim  \[Nâng cao]

**Đề bài**

Cài DSU (hợp theo hạng + nén đường), kruskal (sắp cạnh theo (w, u, v), trả về tổng trọng số và các cạnh theo thứ tự chọn) và prim (từ đỉnh 0, dùng min-heap) để đối chiếu.

**Kết quả cần đạt**

- Đồ thị mẫu 7 đỉnh: tổng trọng số 39.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. Vì sao Kruskal cần DSU? Độ phức tạp tổng thể?
2. Khi nào nên chọn Prim thay cho Kruskal?
3. Tìm hiểu thuật toán Boruvka (mục 4.5.7.3) và mô tả ý tưởng trong 3–4 câu.

### Bài 4B.8. Cây AVL  \[Thử thách]

**Đề bài**

Cài rotRight, rotLeft, avlInsert (4 trường hợp LL, RR, LR, RL), đếm tổng số phép xoay đơn (LR/RL tính 2).

**Kết quả cần đạt**

- Chèn 10 20 30 40 50 25 → preorder 30 20 10 25 40 50, cao 3, 4 phép xoay; chèn 1..1000 tăng dần → cao 10.

**Câu hỏi (trả lời trong phiếu báo cáo)**

1. So sánh chiều cao với BST thường khi chèn 1..1000 tăng dần.
2. Chứng minh chiều cao cây AVL n nút là O(log n) (gợi ý: số nút tối thiểu N(h) = N(h−1) + N(h−2) + 1).

# Phụ lục A. Mẫu phiếu báo cáo

| **Thông tin** |  |
| --- | --- |
| Họ tên — MSSV — Lớp |  |
| Bài lab | Lab ___   (trên lớp / về nhà) |
| Ngôn ngữ | C++  /  Python  /  cả hai |
| Số test \[OK] / tổng |  |
| Các bài đã hoàn thành |  |
| Khó khăn gặp phải |  |

| **Câu hỏi** | **Trả lời** |
| --- | --- |
| 1.1-1 |  |
| 1.1-2 |  |
| … |  |

Phần trả lời: ghi số bài – số câu (ví dụ 2.1-3), trả lời ngắn gọn, có số liệu đo được trên máy của mình khi câu hỏi yêu cầu.

# Phụ lục B. Lỗi thường gặp

| **Hiện tượng** | **Nguyên nhân thường gặp** | **Cách xử lý** |
| --- | --- | --- |
| error: structured bindings only available with -std=c++17 | Trình biên dịch mặc định C++11/14 | Thêm -std=c++17 (Dev-C++: Tools → Compiler Options) |
| Chữ tiếng Việt in ra bị lỗi | Console Windows không dùng UTF-8 | Chương trình chỉ in tiếng Việt không dấu; nếu tự thêm, chạy chcp 65001 |
| RecursionError (Python) | Đệ quy sâu (quick sort trên mảng đã sắp, DFS) | Giữ dòng sys.setrecursionlimit(10000) có sẵn |
| Segmentation fault / chương trình dừng đột ngột | Truy cập con trỏ NULL, chỉ số ngoài mảng, pop ngăn xếp rỗng | Kiểm tra điều kiện biên; C++ dùng -fsanitize=address -g để tìm dòng lỗi |
| Bộ đếm lệch so với đáp án | Đếm sai chỗ (đếm cả so sánh j >= 0, đếm swap khi minPos == i…) | Đọc lại quy tắc đếm trong chú thích ngay trên hàm |
| Python chạy rất lâu | Vòng lặp lồng nhau trong Python chậm hơn C++ ~50 lần | Bình thường; các kích thước n trong bản Python đã được giảm sẵn |

Trang  /
