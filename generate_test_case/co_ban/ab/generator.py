from ...generate_test import GenerateTest
import random

class SUMTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_T", type=int, default=1, help="Min T")
        parser.add_argument("--max_T", type=int, default=100, help="Max T")
        parser.add_argument("--min_val", type=int, default=0, help="Min value for A, B")
        parser.add_argument("--max_val", type=int, default=1000, help="Max value for A, B")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_T = getattr(params, "min_T", 1)
        max_T = getattr(params, "max_T", 100)
        min_val = getattr(params, "min_val", 0)
        max_val = getattr(params, "max_val", 1000)

        # 1. Test nhỏ nhất
        test_cases.append("1\n0 0")

        # 2. Test nhỏ, giá trị nhỏ nhất và lớn nhất phân tách
        test_cases.append("2\n0 1000\n1000 0")

        # 3. Test cả hai số lớn nhất
        test_cases.append("1\n1000 1000")

        # 4. Test cả hai số nhỏ nhất
        test_cases.append("1\n0 0")

        # 5. Test hai số giống nhau, ở giá trị giữa
        test_cases.append("1\n500 500")

        # 6. Test hai số là lẻ với tổng nhỏ nhất
        test_cases.append("1\n1 1")

        # 7. Test hai số là lẻ với tổng lớn nhất
        test_cases.append("1\n999 999")

        # 8. Test một số lẻ, một số chẵn
        test_cases.append("1\n1000 1")

        # 9. Test số đầu bằng 0, số sau random
        test_cases.append(f"5\n" + "\n".join(f"0 {random.randint(min_val,max_val)}" for _ in range(5)))

        # 10. Test số sau bằng 0, số đầu random
        test_cases.append(f"5\n" + "\n".join(f"{random.randint(min_val,max_val)} 0" for _ in range(5)))

        # 11. Test số đầu max, số sau random
        test_cases.append(f"5\n" + "\n".join(f"1000 {random.randint(min_val,max_val)}" for _ in range(5)))

        # 12. Test số sau max, số đầu random
        test_cases.append(f"5\n" + "\n".join(f"{random.randint(min_val,max_val)} 1000" for _ in range(5)))

        # 13. Test các số đều là số chẵn
        test_cases.append(f"5\n" + "\n".join(f"{2*i} {2*i+2}" for i in range(5)))

        # 14. Test các số đều là số lẻ
        test_cases.append(f"5\n" + "\n".join(f"{2*i+1} {2*i+3}" for i in range(5)))

        # 15. Các cặp số liên tiếp (0 1, 1 2, ..., 99 100)
        test_cases.append(f"5\n" + "\n".join(f"{i} {i+1}" for i in range(5)))

        # 16. Tất cả các tổng là 1000
        test_cases.append(f"5\n" + "\n".join(f"{i} {1000-i}" for i in range(5)))

        # 17. Test T lớn nhất, A và B đều random
        T = max_T
        ab = [f"{random.randint(min_val, max_val)} {random.randint(min_val, max_val)}" for _ in range(T)]
        test_cases.append(f"{T}\n" + "\n".join(ab))

        # 18. Test T nhỏ nhất, A và B đều min
        test_cases.append("1\n0 0")

        # 19. Test T nhỏ nhất, A và B đều max
        test_cases.append("1\n1000 1000")

        # 20. Test T = max_T, các cặp số đều giống nhau
        test_cases.append(f"{max_T}\n" + "\n".join("1 1" for _ in range(max_T)))

        # 21. Test các tổng là số nguyên tố (chọn các cặp nhỏ)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        ab = [f"{p-1} 1" for p in primes]
        test_cases.append(f"{len(primes)}\n" + "\n".join(ab))

        # 22. Test tổng là số chẵn
        ab = [f"{i} {i}" for i in range(10)]
        test_cases.append(f"{len(ab)}\n" + "\n".join(ab))

        # 23. Test tổng là số lẻ
        ab = [f"{i} {i+1}" for i in range(10)]
        test_cases.append(f"{len(ab)}\n" + "\n".join(ab))

        # 24. Test biên vừa min vừa max
        test_cases.append("4\n0 0\n0 1000\n1000 0\n1000 1000")

        # 25. Test các số lặp lại theo chu kỳ
        ab = [f"{i%1001} {1000-(i%1001)}" for i in range(30)]
        test_cases.append(f"30\n" + "\n".join(ab))

        # 26. Test với số ngẫu nhiên, các số gần biên trên (990-1000)
        ab = [f"{random.randint(990, 1000)} {random.randint(990, 1000)}" for _ in range(10)]
        test_cases.append(f"10\n" + "\n".join(ab))

        # 27. Test các số ngẫu nhiên nhỏ (0-10)
        ab = [f"{random.randint(0, 10)} {random.randint(0, 10)}" for _ in range(10)]
        test_cases.append(f"10\n" + "\n".join(ab))

        # 28. Test các số trùng nhau
        ab = [f"{i} {i}" for i in range(20, 40)]
        test_cases.append(f"{len(ab)}\n" + "\n".join(ab))

        # 29. Test tổng max (A=1000,B=1000)
        test_cases.append("1\n1000 1000")

        # 30. Test tổng min (A=0,B=0)
        test_cases.append("1\n0 0")

        # 31. Test với T = max_T, A luôn = 0, B random
        ab = [f"0 {random.randint(min_val, max_val)}" for _ in range(max_T)]
        test_cases.append(f"{max_T}\n" + "\n".join(ab))

        # 32. Test với T = max_T, B luôn = 0, A random
        ab = [f"{random.randint(min_val, max_val)} 0" for _ in range(max_T)]
        test_cases.append(f"{max_T}\n" + "\n".join(ab))

        # 33. Test với T = max_T, A = max, B random
        ab = [f"1000 {random.randint(min_val, max_val)}" for _ in range(max_T)]
        test_cases.append(f"{max_T}\n" + "\n".join(ab))

        # 34. Test với T = max_T, B = max, A random
        ab = [f"{random.randint(min_val, max_val)} 1000" for _ in range(max_T)]
        test_cases.append(f"{max_T}\n" + "\n".join(ab))

        # 35. Test hiểm hóc: nhiều test case với tổng trùng nhau
        total = 500
        ab = []
        for i in range(total):
            x = random.randint(min_val, max_val)
            ab.append(f"{x} {1000-x if 0 <= 1000-x <= 1000 else 0}")
        test_cases.append(f"{total}\n" + "\n".join(ab))

        # Đảm bảo số lượng test >= 30
        assert len(test_cases) >= 30

        return test_cases