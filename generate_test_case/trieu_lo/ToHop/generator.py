from ...generate_test import GenerateTest
import random

class TOHOPTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=0, help="Min n")
        parser.add_argument("--max_n", type=int, default=100, help="Max n (for big int test)")
        parser.add_argument("--min_k", type=int, default=0, help="Min k")
        parser.add_argument("--max_k", type=int, default=100, help="Max k")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất (n=0, k=0)
        test_cases.append("0 0")

        # 2. k = 0, n > 0
        test_cases.append("5 0")

        # 3. n = k
        test_cases.append("5 5")

        # 4. k = 1
        test_cases.append("100 1")

        # 5. k = n-1
        test_cases.append("8 7")

        # 6. k > n (không hợp lệ)
        test_cases.append("4 5")

        # 7. n lớn, k nhỏ
        test_cases.append("20 2")

        # 8. n lớn, k lớn
        test_cases.append("20 15")

        # 9. n, k ngẫu nhiên nhỏ
        for _ in range(3):
            n = random.randint(1, 10)
            k = random.randint(0, n)
            test_cases.append(f"{n} {k}")

        # 10. n, k ngẫu nhiên lớn
        for _ in range(3):
            n = random.randint(50, params.max_n)
            k = random.randint(0, n)
            test_cases.append(f"{n} {k}")

        # 11. n rất lớn, k = 0
        test_cases.append(f"{params.max_n} 0")

        # 12. n rất lớn, k = n
        test_cases.append(f"{params.max_n} {params.max_n}")

        # 13. n rất lớn, k = n//2
        test_cases.append(f"{params.max_n} {params.max_n // 2}")

        # 14. k < 0 (không hợp lệ)
        test_cases.append("10 -1")

        # 15. n < 0 (không hợp lệ)
        test_cases.append("-5 3")

        return test_cases