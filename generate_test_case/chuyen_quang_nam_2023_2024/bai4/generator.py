from ...generate_test import GenerateTest
import random

class VISITTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=8, help="Max n for brute force")
        parser.add_argument("--min_m", type=int, default=1, help="Min m")
        parser.add_argument("--max_m", type=int, default=8, help="Max m for brute force")
        parser.add_argument("--min_d", type=int, default=1, help="Min d_i")
        parser.add_argument("--max_d", type=int, default=100, help="Max d_i")
        parser.add_argument("--min_v", type=int, default=1, help="Min v_j")
        parser.add_argument("--max_v", type=int, default=100, help="Max v_j")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 1)
        max_n = getattr(params, "max_n", 8)
        min_m = getattr(params, "min_m", 1)
        max_m = getattr(params, "max_m", 8)
        min_d = getattr(params, "min_d", 1)
        max_d = getattr(params, "max_d", 100)
        min_v = getattr(params, "min_v", 1)
        max_v = getattr(params, "max_v", 100)

        # 1. Biên nhỏ nhất, 1 đoàn 1 xe
        test_cases.append("1 1\n1\n1")
        # 2. n = 1, m = 8, random d, random v
        d = random.randint(min_d, max_d)
        v = [random.randint(min_v, max_v) for _ in range(8)]
        test_cases.append(f"1 8\n{d}\n{' '.join(map(str, v))}")
        # 3. n = m = 2, d_i, v_j = min
        test_cases.append("2 2\n1 1\n1 1")
        # 4. n = m = 2, d_i, v_j = max
        test_cases.append(f"2 2\n{max_d} {max_d}\n{max_v} {max_v}")
        # 5. n = 2, m = 5, d tăng, v giảm
        test_cases.append("2 5\n1 10\n10 5 3 2 1")
        # 6. n = 4, m = 8, d xen kẽ min/max, v xen kẽ min/max
        d = [min_d, max_d, min_d, max_d]
        v = [min_v, max_v, min_v, max_v, min_v+1, max_v-1, min_v+2, max_v-2]
        test_cases.append(f"4 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 7. n = m = 8, d tăng dần, v giảm dần
        d = list(range(1, 9))
        v = list(range(8, 0, -1))
        test_cases.append(f"8 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 8. n = 3, m = 8, d ngẫu nhiên, v toàn bằng nhau
        d = [random.randint(min_d, max_d) for _ in range(3)]
        v = [7]*8
        test_cases.append(f"3 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 9. n = m = 8, d toàn max, v toàn min
        d = [max_d]*8
        v = [min_v]*8
        test_cases.append(f"8 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 10. n = 8, m = 8, d toàn min, v toàn max
        d = [min_d]*8
        v = [max_v]*8
        test_cases.append(f"8 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 11. n = m = 8, d, v random
        d = [random.randint(min_d, max_d) for _ in range(8)]
        v = [random.randint(min_v, max_v) for _ in range(8)]
        test_cases.append(f"8 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 12. n = 5, m = 8, d random, v random
        d = [random.randint(min_d, max_d) for _ in range(5)]
        v = [random.randint(min_v, max_v) for _ in range(8)]
        test_cases.append(f"5 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 13. n = 4, m = 4, d,v random
        d = [random.randint(min_d, max_d) for _ in range(4)]
        v = [random.randint(min_v, max_v) for _ in range(4)]
        test_cases.append(f"4 4\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 14. n = 3, m = 8, d tăng, v random
        d = list(range(1, 4))
        v = [random.randint(min_v, max_v) for _ in range(8)]
        test_cases.append(f"3 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 15. n = 8, m = 8, random shuffle d, v
        d = list(range(1, 9))
        v = list(range(1, 9))
        random.shuffle(d)
        random.shuffle(v)
        test_cases.append(f"8 8\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        # 16-25: các bộ random n, m, d, v
        for _ in range(10):
            n = random.randint(min_n, max_n)
            m = random.randint(n, max_m)
            d = [random.randint(min_d, max_d) for _ in range(n)]
            v = [random.randint(min_v, max_v) for _ in range(m)]
            test_cases.append(f"{n} {m}\n{' '.join(map(str, d))}\n{' '.join(map(str, v))}")
        return test_cases