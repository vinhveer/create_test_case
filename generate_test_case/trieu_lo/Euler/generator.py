from ...generate_test import GenerateTest
import random

class EULERTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=20, help="Max n (small for brute force)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, Euler (chu trình)
        test_cases.append("2\n0 1\n1 0")

        # 2. Nhỏ nhất, không Euler (không liên thông)
        test_cases.append("2\n0 0\n0 0")

        # 3. Tam giác đầy đủ (Euler)
        test_cases.append("3\n0 1 1\n1 0 1\n1 1 0")

        # 4. Đường thẳng 3 đỉnh (không Euler)
        test_cases.append("3\n0 1 0\n1 0 1\n0 1 0")

        # 5. Đồ thị đầy đủ chẵn đỉnh (Euler)
        n = 4
        mat = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines))

        # 6. Đồ thị đầy đủ lẻ đỉnh (Euler)
        n = 5
        mat = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines))

        # 7. Đồ thị có đỉnh bậc lẻ (không Euler)
        n = 4
        mat = [
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 0]
        ]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines))

        # 8. Đồ thị có khuyên (Euler)
        n = 3
        mat = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ]
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines))

        # 9. Dãy ngẫu nhiên nhỏ (n=6)
        n = 6
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines))

        # 10. Dãy ngẫu nhiên lớn nhất dưới 1MB (n=max_n)
        n = min(getattr(params, "max_n", 20), 20)
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        lines = [' '.join(map(str, row)) for row in mat]
        test_cases.append(f"{n}\n" + '\n'.join(lines))

        return test_cases