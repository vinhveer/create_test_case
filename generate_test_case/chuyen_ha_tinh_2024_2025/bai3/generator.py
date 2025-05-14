import random
from ...generate_test import GenerateTest

"""
  -----------------------------
  Test Generator for "Bài 3. Tổng chẵn"
  -----------------------------

  Ràng buộc:
    - 2 ≤ n ≤ 10^6
    - 0 ≤ a[i] ≤ 10^6

  Yêu cầu test:
    - Đa dạng tình huống:
      + Biên: n = 2, n lớn (vẫn giới hạn <1MB).
      + Mảng nhỏ, mảng 1 phần tử không hợp lệ (n ≥ 2 mới hợp lệ).
      + Nhiều phần tử 0.
      + Lẫn chẵn/lẻ.
      + Các giá trị max 10^6.
      + Mảng ngẫu nhiên.
    - Bảo đảm tổng file test <1MB.

  Lưu ý: Đây chỉ là một ví dụ minh họa, test thực tế có thể linh hoạt hơn nhiều.
"""

class ESUMTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=50, help="Max n to keep test size under 1MB for demonstration")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1) n = 2, smallest valid
        test_cases.append("2\n0 0")

        # 2) n = 2, different parity
        test_cases.append("2\n1 2")

        # 3) n = 5, all zeros
        test_cases.append("5\n0 0 0 0 0")

        # 4) n = 5, mix chẵn lẻ
        test_cases.append("5\n1 6 3 8 4")

        # 5) n = 5, all large values ~10^6
        test_cases.append("5\n1000000 999999 1000000 999999 500000")

        # 6) n=10, random in [0..100]
        arr = [random.randint(0, 100) for _ in range(10)]
        test_cases.append(f"10\n{' '.join(map(str, arr))}")

        # 7) n=15, random in [0..10^6]
        arr = [random.randint(0, 10**6) for _ in range(15)]
        test_cases.append(f"15\n{' '.join(map(str, arr))}")

        # 8) n=20, random in [0..10^6]
        arr = [random.randint(0, 10**6) for _ in range(20)]
        test_cases.append(f"20\n{' '.join(map(str, arr))}")

        # 9) n=10, alternating even/odd
        arr = []
        for i in range(10):
            if i % 2 == 0:
                arr.append(2 * i)       # even
            else:
                arr.append(2 * i + 1)   # odd
        test_cases.append("10\n" + " ".join(map(str, arr)))

        # 10) n=10, half are max, half are 0
        arr = [1000000]*(5) + [0]*5
        test_cases.append("10\n" + " ".join(map(str, arr)))

        return test_cases