from ...generate_test import GenerateTest
import random

class DEMSOCANHTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=100, help="Max n")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, vô hướng (n=2, đối xứng)
        test_cases.append("2\n0 1 1 0")

        # 2. Nhỏ nhất, có hướng (n=2, không đối xứng)
        test_cases.append("2\n0 1 0 0")

        # 3. Đối xứng toàn 0 (vô hướng)
        test_cases.append("3\n0 0 0 0 0 0 0 0 0")

        # 4. Đối xứng toàn 1 (vô hướng)
        test_cases.append("3\n1 1 1 1 1 1 1 1 1")

        # 5. Đối xứng ngẫu nhiên (vô hướng)
        n = 4
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 6. Không đối xứng ngẫu nhiên (có hướng)
        n = 4
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        # đảm bảo không đối xứng
        mat[0][1] = 1
        mat[1][0] = 0
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 7. Đối xứng với đường chéo khác 0 (vô hướng, có khuyên)
        n = 5
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        for i in range(n):
            mat[i][i] = 1
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 8. Không đối xứng, chỉ 1 phần tử lệch (có hướng)
        n = 3
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        mat[0][2] = 1
        mat[2][0] = 0
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 9. Dãy ngẫu nhiên nhỏ (n=6)
        n = 6
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 10. Dãy ngẫu nhiên lớn nhất dưới 1MB (n=max_n)
        n = min(getattr(params, "max_n", 100), 100)
        mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        return test_cases