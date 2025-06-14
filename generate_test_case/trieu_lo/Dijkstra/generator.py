from ...generate_test import GenerateTest
import random

class DIJKSTRATestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=100, help="Max n (for brute force)")
        parser.add_argument("--min_w", type=int, default=0, help="Min weight")
        parser.add_argument("--max_w", type=int, default=100, help="Max weight")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, không có cạnh
        test_cases.append("2\n0 0\n0 0\n0")

        # 2. Nhỏ nhất, có cạnh
        test_cases.append("2\n0 1\n1 0\n0")

        # 3. Đồ thị có cạnh trọng số lớn, nhỏ, 0
        test_cases.append("3\n0 0 5\n0 0 1\n5 1 0\n0")

        # 4. Đồ thị đầy đủ, trọng số đều
        n = 4
        mat = [[0 if i == j else 2 for j in range(n)] for i in range(n)]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines) + "\n0")

        # 5. Đồ thị có hướng, không liên thông
        test_cases.append("3\n0 0 0\n0 0 1\n0 0 0\n1")

        # 6. Đồ thị có chu trình
        test_cases.append("3\n0 2 0\n0 0 3\n4 0 0\n0")

        # 7. Đồ thị có cạnh trọng số lớn nhất
        n = 3
        mat = [[0, 100, 0], [0, 0, 100], [100, 0, 0]]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines) + "\n0")

        # 8. Đồ thị có cạnh trọng số nhỏ nhất (không âm)
        n = 3
        mat = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines) + "\n1")

        # 9. Dãy ngẫu nhiên nhỏ (n=6)
        n = 6
        mat = [[0 if i == j else random.randint(params.min_w, params.max_w) if random.random() < 0.5 else 0 for j in range(n)] for i in range(n)]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines) + f"\n{random.randint(0, n-1)}")

        # 10. Dãy ngẫu nhiên lớn nhất dưới 1MB (n=max_n)
        n = min(getattr(params, "max_n", 100), 100)
        mat = [[0 if i == j else random.randint(params.min_w, params.max_w) if random.random() < 0.2 else 0 for j in range(n)] for i in range(n)]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines) + f"\n{random.randint(0, n-1)}")

        return test_cases