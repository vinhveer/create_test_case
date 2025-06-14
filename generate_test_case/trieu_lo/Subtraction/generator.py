from ...generate_test import GenerateTest
import random
import string

class SUBTRACTIONTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=2500, help="Max n for <1MB, brute force")
        parser.add_argument("--min_val", type=int, default=-100000, help="Min value for numbers")
        parser.add_argument("--max_val", type=int, default=100000, help="Max value for numbers")
        parser.add_argument("--min_char", type=str, default='a', help="Min char")
        parser.add_argument("--max_char", type=str, default='z', help="Max char")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Nhỏ nhất, chỉ số
        test_cases.append("2 1 2\n2 2 3")

        # 2. Nhỏ nhất, chỉ chữ
        test_cases.append("2 a b\n2 b c")

        # 3. Số và chữ, giao là số
        test_cases.append("3 1 2 a\n2 2 b")

        # 4. Số và chữ, giao là chữ
        test_cases.append("3 a b 1\n2 b 2")

        # 5. Số và chữ, không giao
        test_cases.append("3 1 2 a\n2 b c")

        # 6. Tất cả phần tử A đều trong B
        test_cases.append("3 1 a b\n5 1 a b 2 c")

        # 7. Một tập rỗng (n=0)
        test_cases.append("0\n3 1 2 a")
        test_cases.append("3 1 2 a\n0")

        # 8. Số âm, số 0, số dương, chữ
        test_cases.append("5 -5 0 2 7 a\n4 -5 0 a b")

        # 9. Số trùng nhau trong A, chữ trùng nhau trong A
        test_cases.append("6 1 1 a a b b\n3 1 a b")

        # 10. Số trùng nhau trong B, chữ trùng nhau trong B
        test_cases.append("4 1 a b c\n6 1 1 a a b b")

        # 11. Số lớn nhất, nhỏ nhất, chữ đầu bảng, cuối bảng
        test_cases.append(f"4 {params.min_val} {params.max_val} {params.min_char} {params.max_char}\n2 {params.max_val} {params.max_char}")

        # 12. Dãy ngẫu nhiên nhỏ (brute force)
        n = 10
        m = 10
        nums = [random.randint(params.min_val, params.max_val) for _ in range(n//2)]
        chars = random.choices(string.ascii_lowercase, k=n - n//2)
        a = nums + chars
        random.shuffle(a)
        nums_b = [random.randint(params.min_val, params.max_val) for _ in range(m//2)]
        chars_b = random.choices(string.ascii_lowercase, k=m - m//2)
        b = nums_b + chars_b
        random.shuffle(b)
        test_cases.append(f"{n} {' '.join(map(str, a))}\n{m} {' '.join(map(str, b))}")

        # 13. Dãy ngẫu nhiên lớn nhất dưới 1MB
        n = min(getattr(params, "max_n", 2500), 2500)
        m = n
        nums = [random.randint(params.min_val, params.max_val) for _ in range(n//2)]
        chars = random.choices(string.ascii_lowercase, k=n - n//2)
        a = nums + chars
        random.shuffle(a)
        nums_b = [random.randint(params.min_val, params.max_val) for _ in range(m//2)]
        chars_b = random.choices(string.ascii_lowercase, k=m - m//2)
        b = nums_b + chars_b
        random.shuffle(b)
        test_cases.append(f"{n} {' '.join(map(str, a))}\n{m} {' '.join(map(str, b))}")

        # 14. Toàn số, toàn chữ
        test_cases.append("5 1 2 3 4 5\n5 a b c d e")
        test_cases.append("5 a b c d e\n5 1 2 3 4 5")

        # 15. Toàn số giống nhau
        test_cases.append("5 7 7 7 7 7\n3 7 7 7")

        # 16. Toàn chữ giống nhau
        test_cases.append("5 x x x x x\n3 x x x")

        # 17. Số âm, số dương, chữ trộn lẫn
        test_cases.append("6 -10 0 5 a z m\n4 0 m 100 b")

        return test_cases