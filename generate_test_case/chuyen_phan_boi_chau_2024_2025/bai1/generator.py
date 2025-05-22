from ...generate_test import GenerateTest
import random

class SODBTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_t", type=int, default=1, help="Min T")
        parser.add_argument("--max_t", type=int, default=10**6, help="Max T")
        parser.add_argument("--max_r", type=int, default=10**6, help="Max R, also max L, R")
        return parser

    def generate_inputs(self, params):
        tests = []

        # 1. Test nhỏ nhất (biên nhỏ)
        tests.append("1\n6 9")

        # 2. L = 1, R nhỏ (biên nhỏ)
        tests.append("1\n1 10")

        # 3. L = R (1 số duy nhất, biên, kiểm tra 1 số bất kỳ)
        tests.append("1\n8 8")

        # 4. L = 1, R = 1 (biên nhỏ nhất, 1 không là số đặc biệt)
        tests.append("1\n1 1")

        # 5. L = R = số lớn (số duy nhất, biên lớn)
        tests.append(f"1\n{params.max_r} {params.max_r}")

        # 6. Dãy liên tiếp nhỏ (trường hợp thường)
        tests.append("1\n10 20")

        # 7. Dãy liên tiếp lớn (R lớn)
        tests.append(f"1\n{params.max_r-20} {params.max_r}")

        # 8. L, R là số nguyên tố liên tiếp (không có số đặc biệt nào)
        tests.append("1\n2 3")

        # 9. L, R là hai số đặc biệt liên tiếp (vẫn kiểm tra đúng)
        tests.append("1\n6 8")

        # 10. L, R nằm trong vùng không có số đặc biệt (tricky)
        tests.append("1\n13 13")

        # 11. Nhiều test nhỏ (T > 1, bao phủ nhiều trường hợp)
        _lines = []
        _lines.append("5")
        _lines.append("1 2")     # 1,2
        _lines.append("7 10")    # 7,8,9,10
        _lines.append("100 120") # 100..120
        _lines.append("999990 1000000")
        _lines.append("25 30")
        tests.append('\n'.join(_lines))

        # 12. T = max, các đoạn nhỏ nhất có thể
        T = min(getattr(params, "max_t", 10**6), 1000)
        arr = ["{}".format(T)]
        for _ in range(T):
            L = random.randint(1, params.max_r-1)
            R = L + 1
            arr.append(f"{L} {R}")
        tests.append('\n'.join(arr))

        # 13. T = max, mỗi đoạn là 1 số (L=R)
        T = min(getattr(params, "max_t", 10**6), 1000)
        arr = ["{}".format(T)]
        for _ in range(T):
            L = random.randint(1, params.max_r)
            arr.append(f"{L} {L}")
        tests.append('\n'.join(arr))

        # 14. Một test cực đại (T=1, R-L=to, biên lớn)
        L = params.max_r - 5000
        R = params.max_r
        tests.append(f"1\n{L} {R}")

        # 15. Test ngẫu nhiên T lớn, đoạn nhỏ
        T = min(getattr(params, "max_t", 10**6), 10000)
        arr = ["{}".format(T)]
        for _ in range(T):
            L = random.randint(1, params.max_r-10)
            R = random.randint(L, min(params.max_r, L+10))
            arr.append(f"{L} {R}")
        tests.append('\n'.join(arr))

        return tests