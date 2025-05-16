from ...generate_test import GenerateTest
import random

class SUMSOCPTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=10**3, help="Max n for brute force")
        parser.add_argument("--min_val", type=int, default=0, help="Min value for a_i")
        parser.add_argument("--max_val", type=int, default=10**4, help="Max value for a_i for small test")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 1)
        max_n = getattr(params, "max_n", 10**3)
        min_val = getattr(params, "min_val", 0)
        max_val = getattr(params, "max_val", 10**4)
        # số chính phương trong đoạn [0, max_val]
        sqr_list = [i*i for i in range(int(max_val**0.5)+1)]

        # 1. Biên nhỏ nhất: n=1, a_1=0
        test_cases.append("1\n0")
        # 2. n=1, a_1=max_val
        test_cases.append(f"1\n{max_val}")
        # 3. Tất cả là số chính phương nhỏ nhất
        test_cases.append(f"{min(10, max_n)}\n" + " ".join(str(i*i) for i in range(min(10, max_n))))
        # 4. Dãy chứa mọi số chính phương <= 100
        sq = [str(i*i) for i in range(11)]
        test_cases.append(f"{len(sq)}\n{' '.join(sq)}")
        # 5. Không có số chính phương nào trong dãy, chỉ toàn số lẻ lớn
        d = [x for x in range(1, min(max_n, 1000)*2, 2) if int(x**0.5)**2 != x]
        test_cases.append(f"{len(d)}\n{' '.join(map(str, d))}")
        # 6. Dãy toàn số giống nhau (không chính phương)
        test_cases.append(f"{max_n}\n{' '.join(['3']*max_n)}")
        # 7. Dãy toàn số giống nhau (chính phương)
        test_cases.append(f"{max_n}\n{' '.join(['4']*max_n)}")
        # 8. Dãy tăng dần từ 0, bước 1
        n = min(50, max_n)
        test_cases.append(f"{n}\n{' '.join(str(x) for x in range(n))}")
        # 9. Dãy giảm dần từ max_val
        n = min(50, max_n)
        test_cases.append(f"{n}\n{' '.join(str(x) for x in range(max_val, max_val-n, -1))}")
        # 10. Dãy xen kẽ 2 số chính phương và không chính phương
        n = min(20, max_n)
        arr = []
        for i in range(n):
            arr.append(str(i*i if i%2==0 else i+3))
        test_cases.append(f"{n}\n{' '.join(arr)}")
        # 11. Dãy random nhỏ, không trùng
        n = min(30, max_n)
        arr = random.sample(range(min_val, max_val+1), n)
        test_cases.append(f"{n}\n{' '.join(map(str, arr))}")
        # 12. Dãy random nhỏ, có trùng
        n = min(30, max_n)
        arr = [random.randint(min_val, max_val) for _ in range(n)]
        test_cases.append(f"{n}\n{' '.join(map(str, arr))}")
        # 13. Dãy toàn số 1
        test_cases.append(f"{max_n}\n{' '.join(['1']*max_n)}")
        # 14. Dãy toàn số lớn nhất
        test_cases.append(f"{max_n}\n{' '.join([str(max_val)]*max_n)}")
        # 15. Dãy random, có 0, max_val, số chính phương xen kẽ
        arr = []
        for i in range(min(30, max_n)):
            if i%3==0:
                arr.append('0')
            elif i%3==1:
                arr.append(str(max_val))
            else:
                arr.append(str((i%100)**2))
        test_cases.append(f"{len(arr)}\n{' '.join(arr)}")
        # 16. Dãy random lớn, không có số chính phương nào
        arr = [random.randint(2, max_val) for _ in range(max_n)]
        arr = [x for x in arr if int(x**0.5)**2 != x]
        arr = arr[:max_n]
        test_cases.append(f"{len(arr)}\n{' '.join(map(str, arr))}")
        # 17. Dãy random, mỗi số là số chính phương nhỏ
        n = min(40, max_n)
        arr = random.choices(sqr_list, k=n)
        test_cases.append(f"{n}\n{' '.join(map(str, arr))}")
        # 18. Dãy random, trộn số chính phương và không chính phương
        n = min(40, max_n)
        arr = []
        for _ in range(n):
            if random.random() < 0.5:
                arr.append(str(random.choice(sqr_list)))
            else:
                v = random.randint(min_val, max_val)
                while int(v**0.5)**2 == v:
                    v = random.randint(min_val, max_val)
                arr.append(str(v))
        test_cases.append(f"{n}\n{' '.join(arr)}")
        # 19-40: Random các kiểu
        for _ in range(22):
            n = random.randint(1, max_n)
            arr = [random.randint(min_val, max_val) for _ in range(n)]
            test_cases.append(f"{n}\n{' '.join(map(str, arr))}")
        return test_cases