from ...generate_test import GenerateTest
import random

class SUMFIBOTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min N")
        parser.add_argument("--max_n", type=int, default=10 ** 9, help="Max N")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 1)
        max_n = getattr(params, "max_n", 10 ** 9)

        # 1. Nhỏ nhất (N = 1)
        test_cases.append("1")

        # 2. N = 2 (chính là số Fibonacci)
        test_cases.append("2")

        # 3. N là một số Fibonacci lớn (gần 10^9)
        fib = [1, 1]
        while fib[-1] + fib[-2] <= max_n:
            fib.append(fib[-1] + fib[-2])
        test_cases.append(str(fib[-1]))

        # 4. N là tổng của nhiều số Fibonacci nhỏ (vd: 1+2+3+5+8=19)
        test_cases.append("19")

        # 5. N là tổng của các số Fibonacci liên tiếp lớn nhất nhỏ hơn max_n
        n = sum(fib[-5:])
        test_cases.append(str(n))

        # 6. N = 10^4 (ràng buộc nhỏ)
        test_cases.append("10000")

        # 7. N = 10^9 (ràng buộc lớn nhất)
        test_cases.append("1000000000")

        # 8. N là số lẻ nhỏ (vd: 7)
        test_cases.append("7")

        # 9. N là số chẵn nhỏ (vd: 8)
        test_cases.append("8")

        # 10. N là tổng của hai số Fibonacci không liên tiếp (vd: 21+8)
        test_cases.append("29")

        # 11. N là tổng của tất cả các số Fibonacci <= 10^6
        fibsum = 0
        for f in fib:
            if f > 10**6: break
            fibsum += f
        test_cases.append(str(fibsum))

        # 12. N là số ngẫu nhiên nhỏ (1 <= N <= 1e4)
        n = random.randint(1, 10000)
        test_cases.append(str(n))

        # 13. N là số ngẫu nhiên lớn (1e8 < N <= 1e9)
        n = random.randint(10 ** 8, 10 ** 9)
        test_cases.append(str(n))

        # 14. N là số Fibonacci chẵn lớn nhất <= 1e9
        even_fib = [f for f in fib if f % 2 == 0 and f <= max_n]
        test_cases.append(str(even_fib[-1]))

        # 15. N là số Fibonacci lẻ lớn nhất <= 1e9
        odd_fib = [f for f in fib if f % 2 == 1 and f <= max_n]
        test_cases.append(str(odd_fib[-1]))

        # 16. N là tổng hai số lớn nhất <= 1e9
        n = fib[-1] + fib[-2]
        if n <= max_n:
            test_cases.append(str(n))
        else:
            test_cases.append(str(fib[-2] + fib[-3]))

        # 17. Test ngẫu nhiên nhiều (10 case)
        for _ in range(10):
            n = random.randint(min_n, max_n)
            test_cases.append(str(n))

        return test_cases