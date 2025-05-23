from ...generate_test import GenerateTest
import random

class PrimeDivisorCountTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_a", type=int, default=1, help="Min a value")
        parser.add_argument("--max_a", type=int, default=1000000, help="Max a value")
        parser.add_argument("--min_b", type=int, default=1, help="Min b value")
        parser.add_argument("--max_b", type=int, default=1000000, help="Max b value")
        parser.add_argument("--min_t", type=int, default=1, help="Min number of test cases")
        parser.add_argument("--max_t", type=int, default=1000, help="Max number of test cases")
        return parser

    def generate_test_cases(self, params):
        # Tạo danh sách các test case (chuỗi input), mỗi phần tử là một test input hoàn chỉnh.
        inputs = self.generate_inputs(params)
        test_cases = []
        for i, input_str in enumerate(inputs):
            test_cases.append({
                'id': i + 1,
                'input': input_str
            })
        return test_cases

    def generate_inputs(self, params):
        test_cases = []

        # 1) Test nhỏ nhất, T=1, a=b
        test_cases.append("1\n1 1")

        # 2) Test đoạn rất nhỏ: T=1, [1..2]
        test_cases.append("1\n1 2")

        # 3) Test ví dụ trong đề (T=2)
        test_cases.append("2\n2 7\n1 100")

        # 4) Test khung nhỏ subtask 1: T=5, mỗi dòng [a..b] <= 200
        test_cases.append("5\n1 1\n2 2\n199 200\n10 10\n50 60")

        # 5) Test đoạn [1..200] (subtask 1)
        test_cases.append("1\n1 200")

        # 6) Test với T=3, vài đoạn nhỏ <= 200
        test_cases.append("3\n1 5\n2 4\n50 100")

        # 7) Test đoạn [100..120], [180..200], [1..1], [6..6], [12..13]
        test_cases.append("5\n100 120\n180 200\n1 1\n6 6\n12 13")

        # 8) Trường hợp cận biên subtask 2: T=1, [1..2000]
        test_cases.append("1\n1 2000")

        # 9) T=3, [100..101], [500..510], [1990..2000]
        test_cases.append("3\n100 101\n500 510\n1990 2000")

        # 10) Test [1000..1000], [999..1000], [2..2]
        test_cases.append("3\n1000 1000\n999 1000\n2 2")

        # 11) Đoạn lớn nhất subtask 2: [1..2000], T=2
        test_cases.append("2\n1 2000\n1999 2000")

        # 12) Test cận biên subtask 3: T=1, [1..1000000]
        test_cases.append("1\n1 1000000")

        # 13) Test T=3, [999990..1000000], [500000..500010], [999994..999999]
        test_cases.append("3\n999990 1000000\n500000 500010\n999994 999999")

        # 14) Đoạn [720..720], [360..360], [5040..5040], [2520..2520], [10080..10080] (nhiều ước)
        test_cases.append("5\n720 720\n360 360\n5040 5040\n2520 2520\n10080 10080")

        # 15) Một số đoạn cỡ vừa, T=5, [990..1010], [999000..999100], [950..960], [1000..1010], [1990..2000]
        test_cases.append("5\n990 1010\n999000 999100\n950 960\n1000 1010\n1990 2000")

        # 16) T=5, [10..20], [100..120], [1000..1010], [2001..2010], [300..310]
        test_cases.append("5\n10 20\n100 120\n1000 1010\n2001 2010\n300 310")

        # 17) Random nhỏ subtask 1
        t_small = 5
        lines = []
        for _ in range(t_small):
            a = random.randint(1, 150)
            b = random.randint(a, 200)
            lines.append(f"{a} {b}")
        test_cases.append(f"{t_small}\n" + "\n".join(lines))

        # 18) Random thêm subtask 1
        t_small2 = 5
        lines2 = []
        for _ in range(t_small2):
            a = random.randint(1, 200)
            b = random.randint(a, 200)
            lines2.append(f"{a} {b}")
        test_cases.append(f"{t_small2}\n" + "\n".join(lines2))

        # 19) Random vừa subtask 2
        t_med = 5
        lines3 = []
        for _ in range(t_med):
            a = random.randint(1, 1500)
            b = random.randint(a, 2000)
            lines3.append(f"{a} {b}")
        test_cases.append(f"{t_med}\n" + "\n".join(lines3))

        # 20) Random vừa subtask 2
        t_med2 = 5
        lines4 = []
        for _ in range(t_med2):
            a = random.randint(500, 1500)
            b = random.randint(a, 2000)
            lines4.append(f"{a} {b}")
        test_cases.append(f"{t_med2}\n" + "\n".join(lines4))

        # 21) Random lớn subtask 3
        t_lg1 = 5
        lines5 = []
        for _ in range(t_lg1):
            a = random.randint(1, 999900)
            b = random.randint(a, a+1000) 
            if b > 1000000:
                b = 1000000
            lines5.append(f"{a} {b}")
        test_cases.append(f"{t_lg1}\n" + "\n".join(lines5))

        # 22) Random lớn subtask 3
        t_lg2 = 5
        lines6 = []
        for _ in range(t_lg2):
            a = random.randint(500000, 999000)
            b = random.randint(a, a+5000)
            if b > 1000000:
                b = 1000000
            lines6.append(f"{a} {b}")
        test_cases.append(f"{t_lg2}\n" + "\n".join(lines6))

        # 23) Test [2..9] (có 6 số thỏa mãn: 2,3,4,5,7,9)
        test_cases.append("1\n2 9")

        # 24) T=3, [15..16], [63..64], [255..256]
        test_cases.append("3\n15 16\n63 64\n255 256")

        # 25) T=5, [2..2], [3..3], [5..5], [7..7], [11..11] (toàn prime => divisor count=2)
        test_cases.append("5\n2 2\n3 3\n5 5\n7 7\n11 11")

        # 26) Trường hợp [4..4], [9..9], [16..16], [25..25], [36..36] (là perfect squares)
        test_cases.append("5\n4 4\n9 9\n16 16\n25 25\n36 36")

        # 27) T=3, [60..60], [120..120], [180..180] (số có nhiều ước)
        test_cases.append("3\n60 60\n120 120\n180 180")

        # 28) T=3, [996..1000], [200..210], [300..305]
        test_cases.append("3\n996 1000\n200 210\n300 305")

        # 29) T=5, [1..10], [2..7], [30..40], [997000..997010], [500000..500010]
        lines7 = [
            "1 10",
            "2 7",
            "30 40",
            "997000 997010",
            "500000 500010"
        ]
        test_cases.append(f"5\n" + "\n".join(lines7))

        # 30) Có T=5, [999998..1000000], [999999..1000000], [1000000..1000000], [500..501], [700..701]
        test_cases.append("5\n999998 1000000\n999999 1000000\n1000000 1000000\n500 501\n700 701")

        # 31..35) Thêm 5 test random subtask 3, T=5 mỗi test
        for _ in range(5):
            temp_lines = []
            T_test = 5
            for __ in range(T_test):
                a = random.randint(1, 999900)
                b = random.randint(a, a + 300)
                if b > 1000000:
                    b = 1000000
                temp_lines.append(f"{a} {b}")
            test_cases.append(f"{T_test}\n" + "\n".join(temp_lines))

        # 36..40) Một số test cỡ nhỏ khác (# queries = 4) 
        #         để đảm bảo vượt trên 30 test và tăng coverage
        for _ in range(5):
            T_test = 4
            temp_lines = []
            for __ in range(T_test):
                a = random.randint(1, 100)
                b = random.randint(a, 200)
                temp_lines.append(f"{a} {b}")
            test_cases.append(f"{T_test}\n" + "\n".join(temp_lines))

        # Đảm bảo trên 30 test case.
        return test_cases