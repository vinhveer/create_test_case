import argparse
import random
from ...generate_test import GenerateTest

class TICHTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=2500, help="Max n for <1MB, brute force")
        parser.add_argument("--min_val", type=int, default=1, help="Min value for a, b")
        parser.add_argument("--max_val", type=int, default=100000, help="Max value for a, b")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. N=1, K=1, chỉ một phần tử
        N = 1
        K = 1
        a = [1]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 2. N nhỏ, K nhỏ, dãy toàn 1
        N = 5
        K = 3
        a = [1]*N
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 3. Ví dụ chuẩn đề (N=5, K=10)
        N = 5
        K = 10
        a = [1, 2, 3, 4, 5]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 4. Dãy tăng dần, N=10, K vừa phải
        N = 10
        K = 50
        a = list(range(1, N + 1))
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 5. Dãy giảm dần, K bé
        N = 10
        K = 15
        a = list(range(N, 0, -1))
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 6. Dãy toàn max (a[i] = 10^5), K lớn
        N = 5
        K = 300000
        a = [100000]*N
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 7. Dãy xoắn (zigzag), K ngẫu nhiên
        N = 8
        K = 50
        a = [1, 100, 2, 99, 3, 98, 4, 97]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 8. Dãy ngẫu nhiên trung bình
        N = 12
        K = 500
        a = [random.randint(1, 100) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 9. Dãy xen kẽ 1 và 2, K rất bé
        N = 6
        K = 2
        a = [1, 2, 1, 2, 1, 2]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 10. N hơi lớn một chút, a random, K = 10^9
        N = 30
        K = 10**9
        a = [random.randint(1, 100000) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 11. Trường hợp N=2, K=1 (để test viền, dãy random <= 2)
        N = 2
        K = 1
        a = [1, 1]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 12. Dãy có 1 giá trị lớn, các giá trị còn lại nhỏ
        N = 7
        K = 20
        a = [1, 2, 3, 100, 2, 2, 1]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 13. Dãy toàn 99999, N=6, K = 600000
        N = 6
        K = 600000
        a = [99999]*N
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 14. Dãy lớn cỡ ~50, random, K nhỏ cố ý
        N = 50
        K = 100
        a = [random.randint(1, 500) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # 15. Dãy ngẫu nhiên cỡ vừa, K khoảng 10000
        N = 20
        K = 10000
        a = [random.randint(500, 1000) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        # Thêm những test khác để tăng độ hóc búa nếu cần
        # 16. N cỡ tối đa (giả lập) ~1000, a random, K random
        # Mặc dù đề tối đa N=10^5, vẫn minh họa cỡ 1000 để tránh file quá lớn.
        N = 1000
        K = random.randint(1, 10**9)
        a = [random.randint(1, 100000) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str, a))}")

        return test_cases