from ...generate_test import GenerateTest
import random

class COPHIEUTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=100000, help="Max n for brute force")
        parser.add_argument("--min_val", type=int, default=1, help="Min value of a_i")
        parser.add_argument("--max_val", type=int, default=100000, help="Max value of a_i")
        parser.add_argument("--max_test_size", type=int, default=51200, help="Max bytes per test")
        return parser

    def generate_inputs(self, params):
        tests = []
        max_test_size = getattr(params, "max_test_size", 51200)

        # Helper: only add test if size <= max_test_size bytes
        def add_test(tc):
            if len(tc.encode('utf-8')) <= max_test_size:
                tests.append(tc)

        # 1. Biên nhỏ nhất
        add_test("1\n1")

        # 2. Hai ngày, giảm dần
        add_test("2\n2 1")

        # 3. Hai ngày, tăng dần
        add_test("2\n1 2")

        # 4. Ba ngày, tăng đều
        add_test("3\n1 2 3")

        # 5. Ba ngày, giảm đều
        add_test("3\n3 2 1")

        # 6. Ba ngày, tăng rồi giảm
        add_test("3\n1 3 2")

        # 7. Bốn ngày, giá trị lặp lại
        add_test("4\n2 2 2 2")

        # 8. Dãy tăng dần
        n = 10
        add_test(f"{n}\n{' '.join(str(i) for i in range(1, n+1))}")

        # 9. Dãy giảm dần
        n = 10
        add_test(f"{n}\n{' '.join(str(i) for i in range(n, 0, -1))}")

        # 10. Dãy lặp lại giá trị nhỏ nhất
        n = 10
        add_test(f"{n}\n{' '.join(['1']*n)}")

        # 11. Dãy lặp lại giá trị lớn nhất
        n = 10
        add_test(f"{n}\n{' '.join(['100000']*n)}")

        # 12. Dãy tăng rồi giảm
        n = 10
        vals = list(range(1, 6)) + list(range(5, 0, -1))
        add_test(f"{n}\n{' '.join(str(x) for x in vals)}")

        # 13. Dãy giảm rồi tăng
        n = 10
        vals = list(range(5, 0, -1)) + list(range(1, 6))
        add_test(f"{n}\n{' '.join(str(x) for x in vals)}")

        # 14. Dãy ngẫu nhiên nhỏ
        n = 20
        a = [random.randint(1, 100) for _ in range(n)]
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 15. Dãy ngẫu nhiên lớn nhất cho brute -- kiểm soát size
        n = min(getattr(params,"max_n",100000), 100000)
        a = [random.randint(getattr(params,"min_val",1), getattr(params,"max_val",100000)) for _ in range(n)]
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 16. Dãy xen kẽ max/min
        n = 20
        a = [1, 100000]*10
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 17. Dãy toàn max
        n = 20
        a = [100000]*n
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 18. Dãy toàn min
        n = 20
        a = [1]*n
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 19. Dãy zigzag
        n = 20
        a = [((i%2)*100000+1) for i in range(n)]
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 20. Dãy có 1 phần tử max, còn lại min
        n = 20
        a = [1]*n
        a[10] = 100000
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 21. Dãy có 1 phần tử min, còn lại max
        n = 20
        a = [100000]*n
        a[5] = 1
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 22. Dãy random, 1 phần tử tăng đột biến ở cuối
        n = 20
        a = [random.randint(1, 100) for _ in range(n-1)] + [100000]
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 23. Dãy random, 1 phần tử giảm đột biến ở đầu
        n = 20
        a = [1] + [random.randint(50000, 100000) for _ in range(n-1)]
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 24. Dãy có nhiều plateau (giá trị bằng nhau liên tiếp)
        n = 20
        a = [random.choice([10,20,30,40,50]) for _ in range(n)]
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 25. Dãy tăng giảm luân phiên
        n = 20
        a = []
        for i in range(n):
            a.append(1 if i%2==0 else 100000)
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 26. Dãy có giá trị ở giữa lớn nhất
        n = 21
        a = [1]*10 + [100000] + [1]*10
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 27. Dãy có giá trị ở giữa nhỏ nhất
        n = 21
        a = [100000]*10 + [1] + [100000]*10
        add_test(f"{n}\n{' '.join(map(str, a))}")

        # 28. Dãy random max size, chỉ 2 giá trị, đảo vị trí
        n = min(getattr(params,"max_n",100000), 100000)
        a = [random.choice([1,100000]) for _ in range(n)]
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 29. Dãy random max size, gần như tăng dần xen kẽ noise nhỏ
        n = min(getattr(params,"max_n",100000), 100000)
        a = [i + random.randint(-2,2) for i in range(1, n+1)]
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 30. Dãy random max size, nhiều đoạn tăng giảm xen kẽ
        n = min(getattr(params,"max_n",100000), 100000)
        a = []
        for i in range(n):
            if (i//100)%2==0:
                a.append(1 + (i%100))
            else:
                a.append(100000 - (i%100))
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 31. Dãy random, mỗi 1000 phần tử lại đảo ngược 1 đoạn
        n = min(getattr(params,"max_n",100000), 100000)
        a = list(range(1, n+1))
        for i in range(0, n, 1000):
            a[i:i+500] = reversed(a[i:i+500])
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 32. Dãy random, xen kẽ giá trị gần nhau
        n = min(getattr(params,"max_n",100000), 100000)
        a = []
        val = 1
        for i in range(n):
            if i%2==0:
                a.append(val)
            else:
                a.append(val+1)
                val += 1
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 33. Test mẫu đề 1
        add_test("6\n10 8 5 3 9 45")

        # 34. Test mẫu đề 2
        add_test("7\n16 4 6 3 2 18 15")

        # 35. Dãy random max size, nhiều giá trị giống nhau
        n = min(getattr(params,"max_n",100000), 100000)
        a = [random.choice([7777,8888,9999]) for _ in range(n)]
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        # 36. Dãy random max size, nhiều giá trị ngẫu nhiên
        n = min(getattr(params,"max_n",100000), 100000)
        a = [random.randint(1, 100000) for _ in range(n)]
        s = f"{n}\n{' '.join(map(str, a))}"
        add_test(s)

        return tests