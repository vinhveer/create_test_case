from ...generate_test import GenerateTest
import random

class HANHTRINHTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=8, help="Max n (small for brute force, exponential paths)")
        parser.add_argument("--max_k", type=int, default=6, help="Max k (path length)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, có 1 hành trình
        test_cases.append("2\n1 1 1 0\n1 0 1")

        # 2. Nhỏ nhất, không có hành trình
        test_cases.append("2\n0 0 0 0\n1 0 1")

        # 3. Đồ thị đầy đủ, k=2, từ 0 đến 1
        test_cases.append("3\n1 1 1 1 1 1 1 1 1\n2 0 1")

        # 4. Đường thẳng, chỉ 1 hành trình duy nhất
        test_cases.append("3\n0 1 0 0 0 1 0 0 0\n2 0 2")

        # 5. Có chu trình, k=3, từ 0 đến 0
        test_cases.append("3\n0 1 1 1 0 1 1 1 0\n3 0 0")

        # 6. Đồ thị có hướng, nhiều đường đi, k=2
        test_cases.append("4\n0 1 1 0 0 0 1 1 0 0 0 1 0 0 0 0\n2 0 3")

        # 7. Đồ thị không liên thông, không có hành trình
        test_cases.append("4\n0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0\n2 2 3")

        # 8. Đồ thị có khuyên, k=1, từ 2 đến 2
        test_cases.append("3\n0 1 0 0 1 0 0 0 1\n1 2 2")

        # 9. Dãy ngẫu nhiên nhỏ (n=5, k=3)
        n = 5
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        k = 3
        v_i = random.randint(0, n-1)
        v_j = random.randint(0, n-1)
        test_cases.append(f"{n}\n{' '.join(flat)}\n{k} {v_i} {v_j}")

        # 10. Dãy ngẫu nhiên lớn nhất dưới 1MB (n=max_n, k=max_k)
        n = min(getattr(params, "max_n", 8), 8)
        k = min(getattr(params, "max_k", 6), 6)
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        v_i = random.randint(0, n-1)
        v_j = random.randint(0, n-1)
        test_cases.append(f"{n}\n{' '.join(flat)}\n{k} {v_i} {v_j}")

        return test_cases