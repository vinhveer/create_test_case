from ...generate_test import GenerateTest
import random

class MultipleOf3Or5TestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min N")
        parser.add_argument("--max_n", type=int, default=10**6, help="Max N for brute force (90% cases)")
        parser.add_argument("--max_big_n", type=int, default=10**10, help="Max N for big test (10% cases)")
        parser.add_argument("--max_T", type=int, default=10, help="Max T (number of test lines per file)")
        return parser

    def generate_inputs(self, params):
        """
        Generate test cases covering:
          1) Small boundary conditions.
          2) Values that are multiples of 3 or 5.
          3) Mixed small inputs including edge cases.
          4) Key multiples like 15.
          5) Large inputs near 10^6 (for 90% of the points).
          6) Extremely large input near 10^10 (for remaining 10%).
          7) Sequences: increasing and decreasing N.
          8) Random picks in small range and large range.
        """
        test_cases = []

        # 1. Single T=1, smallest N
        test_cases.append("1\n1")

        # 2. T=2, includes 3 and 5
        test_cases.append("2\n3\n5")

        # 3. T=5, small values including 2, 3, 5, 6, 10
        test_cases.append("5\n2\n3\n5\n6\n10")

        # 4. Single T=1, includes 15 (LCM of 3 and 5)
        test_cases.append("1\n15")

        # 5. Single T=1, near max_n (for 90% data)
        test_cases.append(f"1\n{params.max_n}")

        # 6. Single T=1, near max_big_n (for 10% data)
        test_cases.append(f"1\n{params.max_big_n}")

        # 7. T=10, strictly increasing from 1..10
        test_cases.append("10\n" + "\n".join(str(i) for i in range(1, 11)))

        # 8. T=10, strictly decreasing from 10..1
        test_cases.append("10\n" + "\n".join(str(i) for i in range(10, 0, -1)))

        # 9. T (max_T), random range in [min_n..max_n]
        T = params.max_T
        arr_small = [str(random.randint(params.min_n, params.max_n)) for _ in range(T)]
        test_cases.append(f"{T}\n" + "\n".join(arr_small))

        # 10. T=5, random large values in [10^9..max_big_n]
        T10 = 5
        arr_large = [str(random.randint(10**9, params.max_big_n)) for _ in range(T10)]
        test_cases.append(f"{T10}\n" + "\n".join(arr_large))

        return test_cases