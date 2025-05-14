import random
from ...generate_test import GenerateTest

"""
  -----------------------------
  Class sinh test cho Bài 5
  -----------------------------
  - Tuân thủ ràng buộc:
      1 ≤ N ≤ 5000
      |a[i]| ≤ 10^6
  - Mục tiêu: Tạo ra các test case đa dạng, gồm:
      + N nhỏ nhất
      + N trung bình
      + N lớn
      + a[i] gồm số âm, dương
      + Trường hợp ranh giới, tricky
      + Tổng kích thước <= 1MB
"""

class TICHTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min size N")
        parser.add_argument("--max_n", type=int, default=50, help="Max size for test (example usage)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1) N=1, duy nhất 1 phần tử
        N = 1
        arr = [0]  # c(1) = 0
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 2) N=3, giá trị bé, có thể có sum 0
        N = 3
        arr = [1, -1, 0]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 3) N=5, có số âm, dương, như ví dụ trong đề
        N = 5
        arr = [-5, 7, 6, -5, 8]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 4) N=8, ví dụ trong đề
        N = 8
        arr = [-4, 2, -2, 3, 0, -2, 1, 1]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 5) N=6, toàn dương
        N = 6
        arr = [1, 2, 3, 4, 5, 6]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 6) N=6, toàn âm
        N = 6
        arr = [-1, -2, -3, -4, -5, -6]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 7) N=6, trộn lẫn, values ~ ±100
        N = 6
        arr = [random.randint(-100,100) for _ in range(N)]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 8) N=10, random values
        N = 10
        arr = [random.randint(-100,100) for _ in range(N)]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 9) N=12, random values
        N = 12
        arr = [random.randint(-10**6,10**6) for _ in range(N)]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 10) N=15, random values
        N = 15
        arr = [random.randint(-10**6,10**6) for _ in range(N)]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 11) Trường hợp có nhiều 0
        N = 7
        arr = [0, 0, 1, -1, 0, 2, -2]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 12) N=5, all same
        N = 5
        arr = [1, 1, 1, 1, 1]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 13) N=5, all same negative
        N = 5
        arr = [-2, -2, -2, -2, -2]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 14) N=20, random values
        N = 20
        arr = [random.randint(-1000,1000) for _ in range(N)]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        # 15) N=30, random values
        N = 30
        arr = [random.randint(-1000,1000) for _ in range(N)]
        test_cases.append(
            f"{N}\n{' '.join(map(str, arr))}"
        )

        return test_cases