# Sinh test cho bài toán nghiệm nguyên dương, nguyên tố của phương trình ax+b=0

from ...generate_test import GenerateTest
import random
from sympy import isprime

class LinearPrimeRootTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min N")
        parser.add_argument("--max_n", type=int, default=20, help="Max N")
        parser.add_argument("--max_coef", type=int, default=10**12, help="Max |a|,|b|")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Biên nhỏ nhất
        test_cases.append("1\n1 -2")  # x=2, là nguyên tố, nghiệm dương, đáp án 1

        # 2. a > 0, b < 0, nghiệm nguyên dương, là số nguyên tố
        test_cases.append("1\n3 -15") # x=5, 5 là nguyên tố

        # 3. a < 0, b < 0, nghiệm nguyên dương, không nguyên tố
        test_cases.append("1\n-2 -6") # x=-6/-2=3, 3 là nguyên tố

        # 4. Không có nghiệm nguyên dương
        test_cases.append("1\n2 3")   # x = -3/2 = -1.5

        # 5. Nghiệm nguyên dương nhưng không phải số nguyên tố
        test_cases.append("1\n2 -8")  # x=4

        # 6. Trường hợp nhiều phương trình, 1 nghiệm hợp lệ
        test_cases.append("3\n1 -3\n12 -6\n-50 -100") # x=3 (prime), x=0.5, x=2 (prime)

        # 7. Nghiệm âm
        test_cases.append("1\n5 10")  # x=-2

        # 8. a rất lớn, b rất lớn, nghiệm nhỏ
        big = 10**12
        test_cases.append(f"1\n{big} {-2*big}") # x=2 (prime)

        # 9. a nhỏ, b lớn
        test_cases.append("1\n1 -7") # x=7 (prime)

        # 10. a âm, b âm, nghiệm lớn (prime)
        test_cases.append("1\n-1 -101") # x=101 (prime)

        # 11. Nhiều phương trình, phối hợp các dạng
        test_cases.append("5\n1 -2\n2 -8\n3 -9\n4 -8\n5 -10")  # x=2,4,3,2,2 (primes:2,3)

        # 12. Random hợp lệ: tạo nghiệm là prime
        from sympy import nextprime
        N = random.randint(getattr(params,"min_n",1), getattr(params,"max_n",20))
        lines = []
        for _ in range(N):
            # Random x là prime
            x = nextprime(random.randint(1,1000000))
            a = random.choice([1,-1,random.randint(-100,100)])
            if a == 0: a = 1
            b = -a*x
            lines.append(f"{a} {b}")
        test_cases.append(f"{N}\n" + "\n".join(lines))

        # 13. Random "hiểm hóc": nghiệm lớn, không phải prime
        N = random.randint(getattr(params,"min_n",1), getattr(params,"max_n",20))
        lines = []
        for _ in range(N):
            x = random.randint(10**6,10**12)
            while isprime(x):
                x += 1
            a = random.choice([1,-1,random.randint(-100,100)])
            if a == 0: a = 1
            b = -a*x
            lines.append(f"{a} {b}")
        test_cases.append(f"{N}\n" + "\n".join(lines))

        # 14. Edge: a = 1, b = -(prime), nghiệm là prime
        test_cases.append("1\n1 -11")

        # 15. Edge: a = -1, b = prime, nghiệm là prime
        test_cases.append("1\n-1 13")

        return test_cases