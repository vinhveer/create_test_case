from ...generate_test import GenerateTest
import random

class INTERSECTIONTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=2500, help="Max n for <1MB, brute force")
        parser.add_argument("--min_val", type=int, default=-100000, help="Min value for elements")
        parser.add_argument("--max_val", type=int, default=100000, help="Max value for elements")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, có giao
        test_cases.append("1 1\n1 1")

        # 2. Hai tập giống hệt nhau
        test_cases.append("3 1 2 3\n3 1 2 3")

        # 3. Hai tập không giao nhau
        test_cases.append("3 1 2 3\n3 4 5 6")

        # 4. Một tập rỗng (n=0)
        test_cases.append("0\n3 1 2 3")
        test_cases.append("3 1 2 3\n0")

        # 5. Tập có phần tử âm, 0, dương, có giao
        test_cases.append("4 -5 0 2 7\n5 -5 -2 0 3 7")

        # 6. Tập có phần tử trùng nhau trong cùng 1 tập
        test_cases.append("5 1 2 2 3 3\n4 2 3 4 4")

        # 7. Tập có phần tử lớn nhất và nhỏ nhất
        test_cases.append(f"2 {params.min_val} {params.max_val}\n2 {params.min_val} {params.max_val}")

        # 8. Dãy ngẫu nhiên nhỏ (brute force)
        n = 10
        m = 10
        a = [random.randint(params.min_val, params.max_val) for _ in range(n)]
        b = [random.randint(params.min_val, params.max_val) for _ in range(m)]
        test_cases.append(f"{n} {' '.join(map(str, a))}\n{m} {' '.join(map(str, b))}")

        # 9. Dãy ngẫu nhiên lớn nhất dưới 1MB
        n = min(getattr(params, "max_n", 2500), 2500)
        m = n
        a = [random.randint(params.min_val, params.max_val) for _ in range(n)]
        b = [random.randint(params.min_val, params.max_val) for _ in range(m)]
        test_cases.append(f"{n} {' '.join(map(str, a))}\n{m} {' '.join(map(str, b))}")

        # 10. Một tập con của tập còn lại
        test_cases.append("5 1 2 3 4 5\n3 2 3 4")

        # 11. Tập có giá trị lặp lại nhiều lần
        test_cases.append("6 7 7 7 7 7 7\n4 7 7 7 7")

        # 12. Test mẫu đề (có giao)
        test_cases.append("2 1 2\n2 2 3")
        # 13. Test mẫu đề (không giao)
        test_cases.append("3 1 2 5\n4 0 6 7 8")

        # 14. Giao là 0
        test_cases.append("3 0 1 2\n2 0 3")

        # 15. Giao là số âm
        test_cases.append("4 -10 -5 0 5\n3 -10 2 3")

        # 16. Giao là số lớn nhất, nhỏ nhất
        test_cases.append(f"3 {params.min_val} 0 {params.max_val}\n2 {params.min_val} {params.max_val}")

        return test_cases