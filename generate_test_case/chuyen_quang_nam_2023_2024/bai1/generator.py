from ...generate_test import GenerateTest
import random

class SOTKTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min N")
        parser.add_argument("--max_n_small", type=int, default=10**6, help="Max N for 50% tests")
        parser.add_argument("--max_n_medium", type=int, default=10**9, help="Max N for 40% tests")
        parser.add_argument("--max_n_large", type=int, default=5*10**17, help="Max N for 10% tests")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 1)
        max_n_small = getattr(params, "max_n_small", 10**6)
        max_n_medium = getattr(params, "max_n_medium", 10**9)
        max_n_large = getattr(params, "max_n_large", 5*10**17)

        # 1. Biên nhỏ nhất
        test_cases.append("1\n1")
        # 2. Biên N = 10^6, K = 1
        test_cases.append(f"{10**6}\n1")
        # 3. Biên N = 10^9, K = 9
        test_cases.append(f"{10**9}\n9")
        # 4. Biên N = 5*10^17, K = 1
        test_cases.append(f"{5*10**17}\n1")
        # 5. N có nhiều chữ số giống nhau, K=1..9
        for k in range(1, 10):
            test_cases.append(f"{'7'*k}\n{k}")
        # 6. N toàn các chữ số tăng dần, K = 5
        test_cases.append("123456789\n5")
        # 7. N toàn các chữ số giảm dần, K = 5
        test_cases.append("987654321\n5")
        # 8. N có chữ số lặp xen kẽ, K = 3
        test_cases.append("9090909090\n3")
        # 9. N có nhiều chữ số 0 ở đầu/giữa/cuối, K=2
        test_cases.append("1002003004\n2")
        # 10. N có đủ 10 chữ số, xáo trộn, K=6
        test_cases.append("9081726354\n6")
        # 11. N có 1 chữ số khác nổi bật, K=1,2,3
        test_cases.append("1111911111\n1")
        test_cases.append("1111911111\n2")
        test_cases.append("1111911111\n3")
        # 12. N = số ngẫu nhiên nhỏ, K ngẫu nhiên
        for _ in range(4):
            n = random.randint(min_n, max_n_small)
            digits = str(n)
            k = random.randint(1, min(len(digits), 9))
            test_cases.append(f"{digits}\n{k}")
        # 13. N = số ngẫu nhiên vừa, K ngẫu nhiên
        for _ in range(4):
            n = random.randint(max_n_small+1, max_n_medium)
            digits = str(n)
            k = random.randint(1, min(len(digits), 9))
            test_cases.append(f"{digits}\n{k}")
        # 14. N = số ngẫu nhiên lớn, K ngẫu nhiên
        for _ in range(4):
            length = random.randint(10, 18)
            digits = ''.join(random.choices('0123456789', k=length))
            if digits[0] == '0':
                digits = '1' + digits[1:] # tránh số 0 ở đầu
            k = random.randint(1, min(len(digits), 9))
            test_cases.append(f"{digits}\n{k}")
        # 15. N toàn số chẵn, K ngẫu nhiên
        test_cases.append("24682468\n3")
        # 16. N toàn số lẻ, K ngẫu nhiên
        test_cases.append("135797531\n4")
        # 17. N có nhiều chữ số 0, K=1
        test_cases.append("100000000000\n1")
        # 18. N có chữ số max ở cuối, K=1
        test_cases.append("111117\n1")
        # 19. N có chữ số min ở đầu, K=1
        test_cases.append("0123456789\n1")
        # 20. N có 2 chữ số duy nhất lặp lại, K=2
        test_cases.append("8989898989\n2")
        # 21-40: Random length, random content, random K
        for _ in range(20):
            length = random.randint(1, 18)
            digits = ''.join(random.choices('0123456789', k=length))
            if digits[0] == '0': digits = '1' + digits[1:]
            k = random.randint(1, min(len(digits), 9))
            test_cases.append(f"{digits}\n{k}")

        return test_cases