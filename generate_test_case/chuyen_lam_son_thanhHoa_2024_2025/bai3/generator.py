from ...generate_test import GenerateTest
import random
import math

class BoiSoTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--max_a", type=int, default=100000, help="Max value for a")
        parser.add_argument("--max_b", type=int, default=100000, help="Max value for b")
        parser.add_argument("--max_n", type=int, default=2000000000, help="Max value for N")
        parser.add_argument("--max_t", type=int, default=100000, help="Max number of test cases")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        max_a = getattr(params, "max_a", 100000)
        max_b = getattr(params, "max_b", 100000)
        max_n = getattr(params, "max_n", 2000000000)
        max_t = getattr(params, "max_t", 100000)

        # ===== Subtask 1: T=1, a=b, N≤2*10^9 (20% số test) =====
        
        # Test 1: a=b=1, N=1 (Trường hợp nhỏ nhất)
        test_cases.append("1\n1 1 1")
        
        # Test 2: a=b=1, N lớn (biên)
        test_cases.append(f"1\n1 1 {max_n}")
        
        # Test 3: a=b nhỏ, N lớn
        test_cases.append(f"1\n5 5 {max_n}")
        
        # Test 4: a=b trung bình, N trung bình
        test_cases.append("1\n1000 1000 1000000")
        
        # Test 5: a=b lớn, N nhỏ
        test_cases.append("1\n100000 100000 10")
        
        # Test 6: a=b lớn, N lớn (thử thách thuật trâu)
        test_cases.append(f"1\n100000 100000 {max_n}")
        
        # ===== Subtask 2: T=1, a!=b, N≤10^4 (30% số test) =====
        
        # Test 7: a=1, b=2, N nhỏ
        test_cases.append("1\n1 2 10")
        
        # Test 8: a và b nguyên tố cùng nhau, N trung bình
        test_cases.append("1\n17 19 1000")
        
        # Test 9: a là bội của b, N trung bình 
        test_cases.append("1\n15 5 1000")
        
        # Test 10: b là bội của a, N trung bình
        test_cases.append("1\n7 14 1000")
        
        # Test 11: a và b có ước chung lớn, N trung bình
        test_cases.append("1\n30 50 1000")
        
        # Test 12: a và b lớn và nguyên tố cùng nhau, N=10^4
        test_cases.append(f"1\n99991 99989 10000")
        
        # Test 13: Sample test từ đề bài
        test_cases.append("1\n4 6 9")
        
        # Test 14: Sample test khác từ đề bài
        test_cases.append("1\n2 3 10")
        
        # Test 15: Sample test khác từ đề bài (a=b)
        test_cases.append("1\n3 3 2")
        
        # ===== Subtask 3: Không ràng buộc thêm (50% số test) =====
        
        # Test 16: T nhỏ, nhiều test cases đa dạng
        t = 5
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            n = random.randint(1, 10000)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 17: T trung bình, các test cases đặc biệt
        t = 100
        lines = [str(t)]
        for i in range(t):
            if i % 4 == 0:  # a=b
                a = random.randint(1, 10000)
                b = a
            elif i % 4 == 1:  # a là bội của b
                b = random.randint(1, 1000)
                a = b * random.randint(2, 10)
            elif i % 4 == 2:  # b là bội của a
                a = random.randint(1, 1000)
                b = a * random.randint(2, 10)
            else:  # a, b nguyên tố cùng nhau
                a = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
                b = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
                while math.gcd(a, b) != 1:
                    b = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
            n = random.randint(1, 10000)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 18: Test với a, b lớn, N lớn (thử thách thuật trâu)
        t = 10
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(90000, 100000)
            b = random.randint(90000, 100000)
            n = random.randint(10**8, 2*10**9)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 19: Test với T lớn, a, b nhỏ, N nhỏ (kiểm tra hiệu suất)
        t = 10000
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            n = random.randint(1, 1000)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 20: Test với T lớn, a, b lớn, N trung bình
        t = 1000
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(10000, 100000)
            b = random.randint(10000, 100000)
            n = random.randint(1000, 10000)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 21: Test với T lớn nhất, a, b nhỏ, N nhỏ
        t = 100000
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            n = random.randint(1, 100)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 22: Test trường hợp đặc biệt a và b có LCM lớn
        t = 10
        lines = [str(t)]
        for _ in range(t):
            # Tạo a, b sao cho LCM lớn (ví dụ: a, b là những số nguyên tố lớn)
            a = random.choice([99991, 99989, 99971, 99961, 99929, 99923, 99907, 99901])
            b = random.choice([99991, 99989, 99971, 99961, 99929, 99923, 99907, 99901])
            while a == b:  # Đảm bảo a != b
                b = random.choice([99991, 99989, 99971, 99961, 99929, 99923, 99907, 99901])
            n = random.randint(1000, 10000)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 23: Test trường hợp đặc biệt LCM(a,b) = a*b (nguyên tố cùng nhau)
        t = 10
        lines = [str(t)]
        for _ in range(t):
            # Chọn những số nguyên tố
            a = random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            b = random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            while a == b:  # Đảm bảo a != b
                b = random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            n = random.randint(10**7, 10**8)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 24: Test biên - a, b nhỏ nhất, N lớn nhất
        test_cases.append(f"1\n1 2 {max_n}")
        
        # Test 25: Test biên - a, b lớn nhất, N lớn nhất
        test_cases.append(f"1\n{max_a} {max_b} {max_n}")
        
        # Test 26: Test hỗn hợp nhiều T, some a=b, some a!=b
        t = 1000
        lines = [str(t)]
        for i in range(t):
            if i % 2 == 0:  # a=b
                a = random.randint(1, max_a)
                b = a
            else:  # a!=b
                a = random.randint(1, max_a)
                b = random.randint(1, max_b)
                while a == b:  # Đảm bảo a != b
                    b = random.randint(1, max_b)
            n = random.randint(1, 10**6)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 27: Test với nhiều a và b nhỏ, N lớn (thử thách thuật trâu)
        t = 100
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(1, 100)
            b = random.randint(1, 100) 
            n = random.randint(10**8, max_n)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 28: Test với a và b làm cho LCM rất lớn
        t = 10
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(90000, 100000)
            b = random.randint(90000, 100000)
            # Đảm bảo a và b không có nhiều ước chung
            while math.gcd(a, b) > 10:
                b = random.randint(90000, 100000)
            n = random.randint(10**7, 10**8)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 29: Test với những cặp a, b đặc biệt (a*b overflows 32-bit int)
        t = 10
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(50000, 100000)
            b = random.randint(50000, 100000)
            n = random.randint(10**7, 10**8)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 30: Test với a=1, b lớn, N lớn (dãy bao gồm mọi số tự nhiên và một số bội của b)
        test_cases.append(f"1\n1 {max_b} {max_n}")
        
        # Test 31: Test với a, b là các số Fibonacci liên tiếp, N lớn
        # Các số Fibonacci 21 và 22: 10946 và 17711
        test_cases.append(f"1\n10946 17711 {10**8}")
        
        # Test 32: Test với a và b là bội số của nhau và N lớn
        test_cases.append(f"1\n1234 12340 {10**8}")
        
        # Test 33: Test max T và nhiều test cases nhỏ
        t = max_t
        lines = [str(t)]
        for _ in range(t):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            n = random.randint(1, 10)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))
        
        # Test 34: Test với nhiều T, a=b=1 (dãy số tự nhiên)
        t = 1000
        lines = [str(t)]
        for _ in range(t):
            n = random.randint(1, 10**6)
            lines.append(f"1 1 {n}")
        test_cases.append("\n".join(lines))
        
        # Test 35: Test kết hợp các trường hợp trên
        t = 100
        lines = [str(t)]
        for i in range(t):
            if i % 5 == 0:  # a=b
                a = random.randint(1, max_a)
                b = a
                n = random.randint(1, max_n)
            elif i % 5 == 1:  # a là bội của b
                b = random.randint(1, 1000)
                a = b * random.randint(2, 10)
                n = random.randint(1, 10**7)
            elif i % 5 == 2:  # b là bội của a
                a = random.randint(1, 1000)
                b = a * random.randint(2, 10)
                n = random.randint(1, 10**7)
            elif i % 5 == 3:  # a, b nguyên tố cùng nhau
                a = random.randint(1000, 10000)
                b = random.randint(1000, 10000)
                while math.gcd(a, b) != 1:
                    b = random.randint(1000, 10000)
                n = random.randint(1, 10**7)
            else:  # a, b lớn và N lớn (thử thách thuật trâu)
                a = random.randint(50000, 100000)
                b = random.randint(50000, 100000)
                n = random.randint(10**8, max_n)
            lines.append(f"{a} {b} {n}")
        test_cases.append("\n".join(lines))

        return test_cases