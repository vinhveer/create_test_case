from ...generate_test import GenerateTest
import random

class SODEPTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_T", type=int, default=1, help="Min T")
        parser.add_argument("--max_T", type=int, default=10**5, help="Max T")
        parser.add_argument("--max_b", type=int, default=10**16, help="Max b")
        parser.add_argument("--max_test_size", type=int, default=51200, help="Max size (bytes) for each test case")
        return parser

    def generate_inputs(self, params):
        tests = []
        max_test_size = params.max_test_size

        # Helper để sinh test lớn nhưng không quá max_test_size
        def add_large_test(arr):
            s = '\n'.join(arr)
            if len(s.encode('utf8')) <= max_test_size:
                tests.append(s)
                return True
            # Nếu quá lớn, thử giảm bớt số dòng
            T = int(arr[0])
            hi = T
            lo = 1
            ok = ""
            while lo <= hi:
                mid = (lo + hi) // 2
                s_try = '\n'.join([str(mid)] + arr[1:mid+1])
                if len(s_try.encode('utf8')) <= max_test_size:
                    ok = s_try
                    lo = mid + 1
                else:
                    hi = mid - 1
            if ok:
                tests.append(ok)
            return

        # Các test nhỏ và đa dạng trước
        tests.append("1\n1 2")
        tests.append("1\n2 4")
        tests.append("1\n1 6")
        tests.append("1\n1 10")
        tests.append("1\n5 6")
        tests.append("1\n1 12")
        tests.append("1\n4 15")
        tests.append("1\n10 20")
        tests.append("1\n2 4")
        tests.append("1\n2 8")
        tests.append("1\n1 18")

        # T = 10, mỗi test đoạn nhỏ <= 18
        arr = ["10"]
        for _ in range(10):
            a = random.randint(1, 10)
            b = random.randint(a+1, min(a+18, 18))
            arr.append(f"{a} {b}")
        tests.append('\n'.join(arr))

        tests.append("1\n1 100000")
        tests.append("1\n23456 45678")
        tests.append("1\n10 100")
        tests.append("1\n11 31")
        tests.append("1\n2 20")
        tests.append("1\n5 25")
        tests.append(f"1\n{10**16-100} {10**16}")
        tests.append(f"1\n{10**16-10} {10**16}")
        tests.append(f"1\n1 {10**16}")
        a = 10**16 - 500
        b = 10**16
        tests.append(f"1\n{a} {b}")

        # 5 đoạn ngẫu nhiên lớn
        arr = ["5"]
        for _ in range(5):
            a = random.randint(1, 10**10)
            b = random.randint(a+1, min(a+10**5, 10**16))
            arr.append(f"{a} {b}")
        tests.append('\n'.join(arr))

        # 100 đoạn nhỏ (biên cho T lớn, kích thước nhỏ)
        arr = ["100"]
        for _ in range(100):
            a = random.randint(1, 1000)
            b = random.randint(a+1, min(a+100, 10000))
            arr.append(f"{a} {b}")
        tests.append('\n'.join(arr))

        # Các test lớn nhưng kiểm soát kích thước
        # 1. T = max_T, đoạn nhỏ nhất hợp lệ (b = a+1)
        T = min(getattr(params,"max_T",10**5), 10**5)
        arr = [str(T)]
        for _ in range(T):
            a = random.randint(1, 10**16-1)
            arr.append(f"{a} {a+1}")
        add_large_test(arr)

        # 2. T = max_T, đoạn lớn vừa phải, mỗi đoạn cách nhau đều
        T2 = min(getattr(params,"max_T",10**5), 10000)
        arr = [str(T2)]
        step = (10**16-1000)//T2
        for i in range(T2):
            a = 1 + i*step
            b = a+100
            arr.append(f"{a} {b}")
        add_large_test(arr)

        # 3. T = max_T, tất cả đoạn là 1 số (a+1), chia đều trong miền [1, 1e16]
        T3 = min(getattr(params,"max_T",10**5), 10**5)
        arr = [str(T3)]
        for i in range(T3):
            a = 1 + i*(10**16//T3)
            arr.append(f"{a} {a+1}")
        add_large_test(arr)

        # Các test lẻ
        tests.append(f"1\n100 150")
        tests.append(f"1\n1000 1100")
        tests.append(f"1\n10000 10100")
        tests.append(f"1\n5 55")
        tests.append(f"1\n2 20")
        tests.append(f"1\n101 121")
        tests.append(f"1\n{10**16-100000} {10**16}")
        tests.append("1\n13 19")
        tests.append("1\n10 20")
        tests.append("1\n20 25")
        tests.append("1\n9999999999999999 10000000000000000")
        tests.append("1\n10000000000000001 10000000000000018")
        tests.append("1\n10000000000000 10000000000040")

        # Đảm bảo tổng file .in nhỏ hơn 1MB
        acc_size = 0
        filtered = []
        for tc in tests:
            size = len(tc.encode('utf8')) + 1
            if acc_size + size > 1048576:
                break
            filtered.append(tc)
            acc_size += size
        return filtered