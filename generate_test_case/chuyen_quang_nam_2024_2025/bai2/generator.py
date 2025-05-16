from ...generate_test import GenerateTest
import random
import string

class NUMMAXTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_len", type=int, default=1, help="Min length of S")
        parser.add_argument("--max_len", type=int, default=300, help="Max length of S")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_len = getattr(params, "min_len", 1)
        max_len = getattr(params, "max_len", 300)

        # 1. Biên: xâu rỗng
        test_cases.append("")

        # 2. Biên: xâu chỉ có 1 số
        test_cases.append("5")

        # 3. Biên: xâu chỉ có 6 số liên tiếp
        test_cases.append("123456")

        # 4. Biên: xâu chỉ có 5 số lẫn ký tự
        test_cases.append("a1b2c3d4e5")

        # 5. Đủ 6 số, xen kẽ ký tự thường, hoa, số
        test_cases.append("aB1cD2eF3gH4iJ5kL6")

        # 6. Có nhiều hơn 6 số, số lớn nằm cuối
        test_cases.append("aaa1234bbb5678")

        # 7. Có nhiều hơn 6 số, số lớn nằm đầu
        test_cases.append("987654321abc")

        # 8. Xâu toàn số, độ dài max 100 (ràng buộc nhỏ)
        test_cases.append("".join(str(random.randint(0, 9)) for _ in range(100)))

        # 9. Xâu toàn số, độ dài max 300 (ràng buộc lớn)
        test_cases.append("".join(str(random.randint(0, 9)) for _ in range(300)))

        # 10. Xâu toàn ký tự không có số
        test_cases.append("".join(random.choice(string.ascii_letters) for _ in range(30)))

        # 11. Xâu dạng mẫu đề
        test_cases.append("23459225")
        test_cases.append("1g9ahgj78hd6r4g28a")
        test_cases.append("Abc43")

        # 12. Xâu đủ 6 số nhưng cách nhau bởi nhiều ký tự đặc biệt
        test_cases.append("a1!@#b2$%^c3&*d4()e5_+f6")

        # 13. Xâu có dấu cách, số ở cuối
        test_cases.append("ab cd 12 34 56")

        # 14. 6 số 0 ở đầu, các số sau nhỏ hơn nhưng nhiều hơn 6 số
        test_cases.append("00000012345")

        # 15. Số lẻ xen số chẵn, số lớn nằm xen kẽ ký tự
        test_cases.append("a9b8c7d6e5f4g3h2i1")

        # 16. Số ngẫu nhiên, chữ xen kẽ, tổng độ dài gần max
        n = max_len - 1
        S = []
        for _ in range(n):
            S.append(random.choice(string.digits + string.ascii_letters + " "))
        test_cases.append("".join(S))

        # 17. Xâu chỉ có 6 số 9
        test_cases.append("9"*6)

        # 18. Xâu có nhiều số 0, chọn số 0 là tối ưu
        test_cases.append("a0b0c0d0e0f0")

        # 19. Số phân tán, chọn không liên tiếp
        test_cases.append("1a9b8c7d6e5f4g3h2i1")

        # 20. Xâu có cả chữ hoa, thường, số, dấu cách, ký tự đặc biệt, đủ 6 số
        complex_chars = "aA1! 2@bB#3$C4%5^D6&"
        test_cases.append(complex_chars)

        # 21-30: 10 random cases, độ dài ngẫu nhiên từ 1 đến max_len
        for _ in range(10):
            n = random.randint(min_len, max_len)
            S = []
            for _ in range(n):
                S.append(random.choice(string.ascii_letters + string.digits + " "))
            test_cases.append("".join(S))

        return test_cases