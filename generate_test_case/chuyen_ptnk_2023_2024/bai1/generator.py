import random
from ...generate_test import GenerateTest

class LUCKTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n")
        parser.add_argument("--max_n", type=int, default=10**9, help="Max n for the problem LUCK (2 ≤ n ≤ 10^9)")
        return parser

    def generate_inputs(self, params):
        """
        Sinh bộ ít nhất 30 test, mỗi test một dòng chứa duy nhất 1 số n.
        Đảm bảo tính đa dạng, bao gồm:
        - Trường hợp nhỏ (biên dưới).
        - Trường hợp cỡ vừa.
        - Trường hợp rất lớn (tiệm cận 10^9).
        - Một số giá trị ngẫu nhiên.
        - Một số giá trị đặc biệt/hiểm hóc.
        """

        test_cases = []

        # 1) Nhỏ nhất theo ràng buộc
        test_cases.append("2")

        # 2) Thêm các giá trị nhỏ / trung bình
        test_cases.append("3")
        test_cases.append("4")
        test_cases.append("5")
        test_cases.append("6")
        test_cases.append("7")
        test_cases.append("10")
        test_cases.append("15")     # ví dụ đã có
        test_cases.append("16")
        test_cases.append("29")
        test_cases.append("30")
        test_cases.append("31")
        test_cases.append("32")
        test_cases.append("33")
        test_cases.append("34")
        test_cases.append("35")
        test_cases.append("99")
        test_cases.append("100")
        test_cases.append("999")
        test_cases.append("1000")

        # 3) Thêm một số giá trị ngẫu nhiên cỡ vừa
        for _ in range(5):
            val = random.randint(2000, 100000)
            test_cases.append(str(val))

        # 4) Thêm một vài giá trị rất lớn gần 10^9
        test_cases.append("999999999")
        test_cases.append("1000000000") # 10^9 (cận trên)
        test_cases.append("500000000")
        test_cases.append("300000001")
        test_cases.append("777777777")

        # 5) Một số giá trị ngẫu nhiên lớn khác
        for _ in range(3):
            val = random.randint(10**8, 10**9)
            test_cases.append(str(val))

        # Đảm bảo có ít nhất 30 test
        # Đếm lại, bổ sung nếu thiếu
        while len(test_cases) < 30:
            val = random.randint(getattr(params, "min_n", 2), getattr(params, "max_n", 10**9))
            test_cases.append(str(val))

        return test_cases