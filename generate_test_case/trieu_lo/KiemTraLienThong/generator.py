from ...generate_test import GenerateTest
import random

class KIEMTRALIENTHONGTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=20, help="Max n (small for brute force)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, liên thông
        test_cases.append("2\n0 1 1 0")

        # 2. Nhỏ nhất, không liên thông
        test_cases.append("2\n0 0 0 0")

        # 3. 3 đỉnh, liên thông (tam giác)
        test_cases.append("3\n0 1 1 1 0 1 1 1 0")

        # 4. 3 đỉnh, không liên thông (1 đỉnh tách biệt)
        test_cases.append("3\n0 1 0 1 0 0 0 0 0")

        # 5. 4 đỉnh, liên thông (đường thẳng)
        test_cases.append("4\n0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0")

        # 6. 4 đỉnh, không liên thông (2 thành phần)
        test_cases.append("4\n0 1 0 0 1 0 0 0 0 0 0 1 0 0 1 0")

        # 7. 5 đỉnh, liên thông (đồ thị đầy đủ)
        n = 5
        mat = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 8. 5 đỉnh, không liên thông (chia đôi)
        mat = [[0]*n for _ in range(n)]
        for i in range(2):
            for j in range(2):
                if i != j:
                    mat[i][j] = 1
        for i in range(2, n):
            for j in range(2, n):
                if i != j:
                    mat[i][j] = 1
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 9. Dãy ngẫu nhiên nhỏ (n=6)
        n = 6
        # Tạo ma trận đối xứng ngẫu nhiên
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        # 10. Dãy ngẫu nhiên lớn nhất dưới 1MB (n=max_n)
        n = min(getattr(params, "max_n", 20), 20)
        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                val = random.randint(0, 1)
                mat[i][j] = mat[j][i] = val
        flat = [str(mat[i][j]) for i in range(n) for j in range(n)]
        test_cases.append(f"{n}\n{' '.join(flat)}")

        return test_cases