import random
from ...generate_test import GenerateTest

"""
  -----------------------------
  Test Generator for "Bài 4. Đặt trạm phát sóng"
  -----------------------------

  Ràng buộc:
    - 1 ≤ n ≤ 10^6
    - 1 ≤ k ≤ 10^9
    - 1 ≤ x, y ≤ 10^9

  Yêu cầu test:
    - Phải tuân thủ ràng buộc.
    - Bao quát các trường hợp:
      + n nhỏ nhất và lớn.
      + k nhỏ, k lớn.
      + min x, max x, x trùng lặp.
      + y nhỏ, y lớn, etc.
    - Bảo đảm tổng kích thước <1MB (đây là ví dụ mô phỏng).

  Ta chọn n nhỏ hoặc trung bình để minh họa.
"""

class EMISTATestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--max_n", type=int, default=20, help="Limit n to keep test under 1MB for example")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1) n=1, k=1, x=1 => trivial
        test_cases.append("1 1\n1 1")

        # 2) n=2, k=1, x cỡ nhỏ
        test_cases.append("2 1\n1 10\n2 5")

        # 3) n=3, k=3, x trung bình
        test_cases.append("3 3\n1 4\n2 8\n7 2")

        # 4) n=4, k=3, theo ví dụ đề
        #     2 8
        #     7 2
        #     10 6
        #     1 4
        test_cases.append("4 3\n2 8\n7 2\n10 6\n1 4")

        # 5) n=5, k nhỏ, random x,y <= 50
        n=5
        k=2
        arr = []
        for _ in range(n):
            xx = random.randint(1, 50)
            yy = random.randint(1, 50)
            arr.append(f"{xx} {yy}")
        test_cases.append(f"{n} {k}\n" + "\n".join(arr))

        # 6) n=5, k lớn, random x,y <= 100
        n=5
        k=999999999  # k cực lớn
        arr = []
        for _ in range(n):
            xx = random.randint(1, 100)
            yy = random.randint(1, 100)
            arr.append(f"{xx} {yy}")
        test_cases.append(f"{n} {k}\n" + "\n".join(arr))

        # 7) n=10, x xen kẽ, random y up to 100
        n=10
        k=5
        arr = []
        # Tạo x lẻ, x chẵn xen kẽ, y random
        for i in range(n):
            if i % 2 == 0:
                xx = 2*i
            else:
                xx = 2*i + 1
            yy = random.randint(1, 100)
            arr.append(f"{xx} {yy}")
        test_cases.append(f"{n} {k}\n" + "\n".join(arr))

        # 8) n=10, random x up to 1000, y up to 1000
        n=10
        k=100
        arr = []
        for _ in range(n):
            xx = random.randint(1, 1000)
            yy = random.randint(1, 1000)
            arr.append(f"{xx} {yy}")
        test_cases.append(f"{n} {k}\n" + "\n".join(arr))

        # 9) n=15, random x up to 10^5, y up to 10^3, k cỡ trung
        n=15
        k=5000
        arr = []
        for _ in range(n):
            xx = random.randint(1, 10**5)
            yy = random.randint(1, 10**3)
            arr.append(f"{xx} {yy}")
        test_cases.append(f"{n} {k}\n" + "\n".join(arr))

        # 10) n=15, random x up to 10^5, y up to 10^6, k rất lớn
        n=15
        k=10**9
        arr = []
        for _ in range(n):
            xx = random.randint(1, 10**5)
            yy = random.randint(1, 10**6)
            arr.append(f"{xx} {yy}")
        test_cases.append(f"{n} {k}\n" + "\n".join(arr))

        return test_cases