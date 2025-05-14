# Sinh test case theo yêu cầu đề bài cắt dây, bao quát biên, đặc biệt, hiểm hóc

from ...generate_test import GenerateTest
import random

class CATDAYTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_N", type=int, default=1, help="Min N")
        parser.add_argument("--max_N", type=int, default=20, help="Max N cho test trâu")
        parser.add_argument("--min_val", type=int, default=1, help="Min chiều dài dây")
        parser.add_argument("--max_val", type=int, default=1000, help="Max chiều dài dây")
        parser.add_argument("--max_K", type=int, default=10000, help="Max K")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Biên nhỏ nhất: 1 dây, 1 đoạn
        test_cases.append("1 1\n1")

        # 2. Biên: dây dài nhất, K=1
        test_cases.append("1 1\n1000000000")

        # 3. Biên: nhiều dây nhỏ, K lớn không cắt được
        test_cases.append("3 100\n1 2 3")

        # 4. Biên: tất cả dây cùng chiều dài, chia hết
        test_cases.append("5 5\n10 10 10 10 10")

        # 5. Biên: tất cả dây cùng chiều dài, chia dư
        test_cases.append("5 7\n10 10 10 10 10")

        # 6. Dây có chiều dài tăng dần
        test_cases.append("5 7\n1 2 3 4 5")

        # 7. Dây có chiều dài giảm dần
        test_cases.append("5 7\n5 4 3 2 1")

        # 8. Dây xen kẽ max/min
        test_cases.append("6 100\n1 1000 1 1000 1 1000")

        # 9. Dây ngẫu nhiên nhỏ
        N = 10
        K = 12
        a = [random.randint(1, 30) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str,a))}")

        # 10. Dây ngẫu nhiên lớn (test trâu)
        N = min(getattr(params,"max_N",20), 20)
        K = random.randint(1, getattr(params,"max_K",10000))
        a = [random.randint(getattr(params,"min_val",1), getattr(params,"max_val",1000)) for _ in range(N)]
        test_cases.append(f"{N} {K}\n{' '.join(map(str,a))}")

        # 11. K quá lớn không thể cắt
        test_cases.append("4 1000\n802 743 547 539")

        # 12. Mẫu đề
        test_cases.append("4 11\n802 743 547 539")

        # 13. Tất cả dây là 1, K rất lớn
        test_cases.append("10 1000\n" + " ".join(["1"]*10))

        # 14. Dây có số siêu lớn, K nhỏ
        test_cases.append("2 2\n1000000000 999999999")

        # 15. Dây có số siêu lớn, K lớn
        test_cases.append("2 1000000000\n1000000000 999999999")

        # 16. Tất cả dây là max, K vừa phải
        N = 20
        K = 100
        test_cases.append(f"{N} {K}\n" + " ".join([str(1000)]*N))

        # 17. Một dây dài cực đại, các dây còn lại nhỏ
        test_cases.append("5 1000\n1000000000 1 1 1 1")

        # 18. Dây là số nguyên tố, K lẻ
        test_cases.append("3 7\n13 17 19")

        # 19. Dây là bội số của nhau
        test_cases.append("4 10\n2 4 8 16")

        # 20. Chỉ có 1 dây, K rất lớn
        test_cases.append("1 500\n1234")

        return test_cases