from ...generate_test import GenerateTest
import random

class DUYETDOTHITestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=20, help="Max n (small for brute force)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, 2 đỉnh, có cạnh
        test_cases.append("2\n0 1 1 0\n0")
        test_cases.append("2\n0 1 1 0\n1")

        # 2. 3 đỉnh, đường thẳng
        test_cases.append("3\n0 1 0 1 0 1 0 1 0\n0")
        test_cases.append("3\n0 1 0 1 0 1 0 1 0\n2")

        # 3. 4 đỉnh, đồ thị đầy đủ
        test_cases.append("4\n0 1 1 1 1 0 1 1 1 1 0 1 1 1 1 0\n0")

        # 4. 4 đỉnh, có cạnh đơn lẻ
        test_cases.append("4\n0 1 0 0 1 0 0 0 0 0 0 1 0 0 1 0\n0")

        # 5. 5 đỉnh, không liên thông
        test_cases.append("5\n0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0\n0")
        test_cases.append("5\n0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0\n3")

        # 6. Có khuyên (self-loop)
        test_cases.append("3\n1 1 0 1 1 1 0 1 1\n0")

        # 7. Đồ thị có hướng, DFS khác nhau theo đỉnh bắt đầu
        test_cases.append("3\n0 1 0 0 0 1 0 0 0\n0")
        test_cases.append("3\n0 1 0 0 0 1 0 0 0\n1")

        # 8. Dãy ngẫu nhiên nhỏ (n=6)
        n = 6
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        for v in range(2):
            test_cases.append(f"{n}\n{' '.join(flat)}\n{v}")

        # 9. Dãy ngẫu nhiên lớn nhất dưới 1MB (n=max_n)
        n = min(getattr(params, "max_n", 20), 20)
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}\n{random.randint(0, n-1)}")

        return test_cases