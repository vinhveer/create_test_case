# Sinh test cho bài toán chèn dấu để ra tổng M, bao quát các trường hợp

from ...generate_test import GenerateTest
import random

class InsertSignTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_len", type=int, default=1, help="Min length of S")
        parser.add_argument("--max_len", type=int, default=9, help="Max length of S (<10)")
        parser.add_argument("--min_M", type=int, default=0, help="Min value of M")
        parser.add_argument("--max_M", type=int, default=199, help="Max value of M (<200)")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Edge: S có 1 chữ số
        test_cases.append("5\n5")
        test_cases.append("7\n3")

        # 2. S có 2 chữ số, các trường hợp cộng, trừ, nối
        test_cases.append("12\n3")   # 1+2=3
        test_cases.append("12\n9")   # 12
        test_cases.append("12\n-1")  # 1-2=-1
        test_cases.append("99\n18")  # 9+9=18

        # 3. S có 3 chữ số, tổng là số nhỏ/âm/lớn
        test_cases.append("123\n6")  # 1+2+3=6
        test_cases.append("123\n123")# 123
        test_cases.append("123\n24") # 12+3=15, 1+23=24
        test_cases.append("321\n-4") # 3-2-1=0, 3-21=-18, ...

        # 4. S toàn số 1
        test_cases.append("1111\n4") # 1+1+1+1=4
        test_cases.append("1111\n1111")
        test_cases.append("1111\n2") # Không có cách

        # 5. S tăng dần
        test_cases.append("123456789\n185") # Test mẫu đề

        # 6. S giảm dần
        test_cases.append("987654321\n100") # Có thể có nghiệm

        # 7. S có số 0 ở đầu/sau
        test_cases.append("101\n2")  # 1+0+1=2
        test_cases.append("101\n11") # 10+1=11
        test_cases.append("101\n101")# nối hết

        # 8. S ngẫu nhiên, M ngẫu nhiên
        for _ in range(5):
            L = random.randint(getattr(params, "min_len", 1), getattr(params, "max_len", 9))
            S = ''.join(str(random.randint(0, 9)) for _ in range(L))
            M = random.randint(getattr(params, "min_M", 0), getattr(params, "max_M", 199))
            test_cases.append(f"{S}\n{M}")

        # 9. S có tất cả các chữ số giống nhau
        S = '5'*9
        test_cases.append(f"{S}\n{int(S)}") # nối hết
        test_cases.append(f"{S}\n{9*5}")    # cộng hết

        # 10. Số M = 0, S bất kỳ
        test_cases.append("123456\n0")

        # 11. Tricky: nghiệm âm, nghiệm lớn, S có số trùng
        test_cases.append("7755\n24")
        test_cases.append("98765\n-1")

        # 12. S có 9 chữ số, M lớn
        S = ''.join(str(random.randint(1, 9)) for _ in range(9))
        test_cases.append(f"{S}\n{random.randint(100, 199)}")

        return test_cases