from ...generate_test import GenerateTest
import random

class COUNTTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min N")
        parser.add_argument("--max_n", type=int, default=20, help="Max N for brute force")
        parser.add_argument("--min_m", type=int, default=1, help="Min M")
        parser.add_argument("--max_m", type=int, default=10**6, help="Max M")
        parser.add_argument("--min_val", type=int, default=1, help="Min value of a_i")
        parser.add_argument("--max_val", type=int, default=100, help="Max value of a_i for small")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 1)
        max_n = getattr(params, "max_n", 20)
        min_m = getattr(params, "min_m", 1)
        max_m = getattr(params, "max_m", 100)
        min_val = getattr(params, "min_val", 1)
        max_val = getattr(params, "max_val", 100)
        
        # 1. Biên nhỏ nhất
        test_cases.append("1 1\n1")
        test_cases.append("1 2\n1")
        test_cases.append("1 1\n2")

        # 2. Toàn bộ phần quà < M
        n = 5
        m = 10
        test_cases.append(f"{n} {m}\n{' '.join(['1']*n)}")

        # 3. Toàn bộ phần quà >= M
        n = 5
        m = 2
        test_cases.append(f"{n} {m}\n{' '.join(['2']*n)}")

        # 4. Xen kẽ < M và >= M
        n = 6
        m = 5
        a = [1, 5, 2, 6, 3, 7]
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 5. Có đúng 1 phần tử >= M
        n = 4
        m = 5
        a = [1, 2, 5, 3]
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 6. Tất cả các phần quà bằng M
        n = 5
        m = 7
        a = [7] * n
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 7. Xen kẽ max/min, kiểm thử biên
        n = 8
        m = 50
        a = [1, 100, 1, 100, 1, 100, 1, 100]
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 8. Dãy tăng dần
        n = 7
        m = 4
        a = list(range(1, n+1))
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 9. Dãy giảm dần
        n = 7
        m = 4
        a = list(range(7, 0, -1))
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 10. Dãy ngẫu nhiên nhỏ (brute force)
        n = max_n
        m = random.randint(min_m, max_m)
        a = [random.randint(min_val, max_val) for _ in range(n)]
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 11. Dãy có phần tử đúng bằng M ở đầu/cuối
        n = 6
        m = 5
        a = [5, 1, 1, 1, 1, 5]
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 12. Test mẫu đề
        test_cases.append("3 4\n2 3 5")
        test_cases.append("4 6\n2 10 8 8")

        # 13. Dãy toàn max_val
        n = 6
        m = max_val
        a = [max_val] * n
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 14. Dãy toàn min_val
        n = 6
        m = min_val
        a = [min_val] * n
        test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        # 15-20: 6 random cases
        for _ in range(6):
            n = random.randint(min_n, max_n)
            m = random.randint(min_m, max_m)
            a = [random.randint(min_val, max_val) for _ in range(n)]
            test_cases.append(f"{n} {m}\n{' '.join(map(str, a))}")

        return test_cases