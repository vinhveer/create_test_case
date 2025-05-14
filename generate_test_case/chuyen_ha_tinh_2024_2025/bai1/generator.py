from ...generate_test import GenerateTest
import random

class PayTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--max_y_small", type=int, default=10**5, help="Max y for 70% score")
        parser.add_argument("--max_y_big", type=int, default=10**9, help="Max y for 30% score")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Biên nhỏ nhất: y=0
        test_cases.append("1000 2000 3000 4000\n0")

        # 2. y=1, x1 nhỏ nhất
        test_cases.append("1 2 3 4\n1")

        # 3. y=50 (hết bậc 1)
        test_cases.append("100 200 300 400\n50")

        # 4. y=51 (vừa sang bậc 2)
        test_cases.append("100 200 300 400\n51")

        # 5. y=100 (hết bậc 2)
        test_cases.append("100 200 300 400\n100")

        # 6. y=101 (vừa sang bậc 3)
        test_cases.append("100 200 300 400\n101")

        # 7. y=200 (hết bậc 3)
        test_cases.append("100 200 300 400\n200")

        # 8. y=201 (vừa sang bậc 4)
        test_cases.append("100 200 300 400\n201")

        # 9. y nhỏ, x1..x4 ngẫu nhiên
        test_cases.append("1800 1900 2100 2700\n300")  # Test mẫu đề

        # 10. y dưới 1e5, x random
        y = random.randint(0, params.max_y_small)
        xs = sorted(random.sample(range(1, 10000), 4))
        test_cases.append(f"{xs[0]} {xs[1]} {xs[2]} {xs[3]}\n{y}")

        # 11. y rất lớn, x random (test hiểm hóc)
        y = random.randint(10**8, params.max_y_big)
        xs = sorted(random.sample(range(1, 10000), 4))
        test_cases.append(f"{xs[0]} {xs[1]} {xs[2]} {xs[3]}\n{y}")

        # 12. x1, x2, x3, x4 sát nhau, y lớn
        test_cases.append(f"9950 9960 9970 9980\n{10**5}")

        # 13. x1, x2, x3, x4 cách xa nhau, y nhỏ
        test_cases.append("100 1000 5000 9000\n20")

        # 14. x1, x2, x3, x4 random, y=10^9
        xs = sorted(random.sample(range(1, 10000), 4))
        test_cases.append(f"{xs[0]} {xs[1]} {xs[2]} {xs[3]}\n{10**9}")

        # 15. x1=9999, x2=10000, x3=10001, x4=10002, y=99_999
        test_cases.append("9999 10000 10001 10002\n99999")

        # 16. y=50, x4 lớn nhất
        test_cases.append("10 20 30 9999\n50")

        # 17. y=100, x1 lớn nhất
        test_cases.append("9999 10000 10001 10002\n100")

        # 18. y=200, x2 lớn nhất
        test_cases.append("10 9999 10000 10001\n200")

        # 19. y=201, x3 lớn nhất
        test_cases.append("10 20 9999 10000\n201")

        # 20. Random nhỏ
        xs = sorted(random.sample(range(1, 10000), 4))
        y = random.randint(0, params.max_y_small)
        test_cases.append(f"{xs[0]} {xs[1]} {xs[2]} {xs[3]}\n{y}")

        return test_cases