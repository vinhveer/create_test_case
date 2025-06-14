from ...generate_test import GenerateTest
import random

class HOANVIKETIEPTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=8, help="Max n (factorial grows fast)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất n=1
        test_cases.append("1")

        # 2. n=2
        test_cases.append("2")

        # 3. n=3 (test mẫu đề)
        test_cases.append("3")

        # 4. n=4
        test_cases.append("4")

        # 5. n=5
        test_cases.append("5")

        # 6. n=6 (gần giới hạn thực tế cho brute force)
        test_cases.append("6")

        # 7. n=max_n (giới hạn lớn nhất cho phép)
        n = min(getattr(params, "max_n", 8), 8)
        test_cases.append(str(n))

        # 8. n ngẫu nhiên trong [min_n, max_n]
        n = random.randint(getattr(params, "min_n", 1), getattr(params, "max_n", 8))
        test_cases.append(str(n))

        return test_cases