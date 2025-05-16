from ...generate_test import GenerateTest
import random

class MANOCANHTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_m", type=int, default=1, help="Min m")
        parser.add_argument("--max_m", type=int, default=8, help="Max m for brute-force")
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=8, help="Max n for brute-force")
        parser.add_argument("--min_v", type=int, default=1, help="Min V_ij")
        parser.add_argument("--max_v", type=int, default=100, help="Max V_ij")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_m = getattr(params, "min_m", 1)
        max_m = getattr(params, "max_m", 8)
        min_n = getattr(params, "min_n", 1)
        max_n = getattr(params, "max_n", 8)
        min_v = getattr(params, "min_v", 1)
        max_v = getattr(params, "max_v", 100)

        # 1. Biên nhỏ nhất, 1 áo 1 ma-nơ-canh
        test_cases.append("1 1\n42")

        # 2. 1 áo, nhiều ma-nơ-canh
        test_cases.append("1 8\n" + " ".join(str(random.randint(min_v, max_v)) for _ in range(8)))

        # 3. m = n = 2, giá trị nhỏ nhất
        test_cases.append("2 2\n1 1\n1 1")

        # 4. m = n = 2, giá trị lớn nhất
        test_cases.append(f"2 2\n{max_v} {max_v}\n{max_v} {max_v}")

        # 5. m = n = 3, toàn giá trị giống nhau
        test_cases.append("3 3\n5 5 5\n5 5 5\n5 5 5")

        # 6. m = n = 3, tăng dần theo dòng/cột
        test_cases.append("3 3\n1 2 3\n4 5 6\n7 8 9")

        # 7. m = 4, n = 6, giá trị xen kẽ min/max
        vals = [min_v, max_v]
        mat = [[vals[(i+j)%2] for j in range(6)] for i in range(4)]
        test_cases.append("4 6\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 8. m = 8, n = 8, random nhỏ nhất/lớn nhất (khó)
        mat = [[random.randint(min_v, max_v) for _ in range(8)] for _ in range(8)]
        test_cases.append("8 8\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 9. m = 5, n = 8, tất cả V_ij = min_v
        mat = [[min_v for _ in range(8)] for _ in range(5)]
        test_cases.append("5 8\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 10. m = 8, n = 8, tất cả V_ij = max_v
        mat = [[max_v for _ in range(8)] for _ in range(8)]
        test_cases.append("8 8\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 11. m < n, random
        mat = [[random.randint(min_v, max_v) for _ in range(7)] for _ in range(4)]
        test_cases.append("4 7\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 12. m = n = 6, random, giá trị sát max_v
        mat = [[random.randint(max_v-10, max_v) for _ in range(6)] for _ in range(6)]
        test_cases.append("6 6\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 13. m = n = 5, random, giá trị sát min_v
        mat = [[random.randint(min_v, min_v+10) for _ in range(5)] for _ in range(5)]
        test_cases.append("5 5\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        # 14-20: 7 random cases, m,n random trong [min_m,max_m], [min_n,max_n]
        for _ in range(7):
            m = random.randint(min_m, max_m)
            n = random.randint(m, max_n)  # n >= m
            mat = [[random.randint(min_v, max_v) for _ in range(n)] for _ in range(m)]
            test_cases.append(f"{m} {n}\n" + "\n".join(" ".join(map(str, row)) for row in mat))

        return test_cases