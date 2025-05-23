from ...generate_test import GenerateTest
import random
import math

class SongNguyenToTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_l", type=int, default=2, help="Min L value")
        parser.add_argument("--max_l", type=int, default=1000000, help="Max L value")
        parser.add_argument("--min_r", type=int, default=2, help="Min R value")
        parser.add_argument("--max_r", type=int, default=1000000, help="Max R value")
        return parser

    def generate_test_cases(self, params):
        """Override the parent method to ensure all test cases are used"""
        inputs = self.generate_inputs(params)
        test_cases = []
        for i, input_str in enumerate(inputs):
            test_cases.append({
                'id': i + 1,
                'input': input_str
            })
        return test_cases
        
    def is_prime(self, n):
        """Kiểm tra số nguyên tố"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
        
    def sum_of_digits(self, n):
        """Tính tổng các chữ số của n"""
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total
        
    def is_song_nguyen_to(self, n):
        """Kiểm tra số song nguyên tố"""
        return self.is_prime(n) and self.is_prime(self.sum_of_digits(n))

    def generate_inputs(self, params):
        test_cases = []
        
        # Mẫu test từ đề bài
        test_cases.append("10 30")
        
        # ===== Test không thỏa mãn điều kiện (10% test cases) =====
        
        # L <= 1
        test_cases.append("0 100")
        test_cases.append("1 500")
        
        # L > R
        test_cases.append("50 30")
        test_cases.append("1000 500")
        
        # R > 10^6
        test_cases.append("100 1000001")
        test_cases.append("500000 2000000")
        
        # ===== Test với 1 < L <= 10^4 (70% test cases) =====
        
        # Trường hợp biên: L gần 2
        test_cases.append("2 100")
        test_cases.append("2 1000")
        test_cases.append("2 10000")
        
        # Khoảng nhỏ
        test_cases.append("10 20")
        test_cases.append("23 50")
        test_cases.append("97 150")
        test_cases.append("499 550")
        
        # Khoảng trung bình
        test_cases.append("1000 2000")
        test_cases.append("5000 6000")
        test_cases.append("9000 10000")
        
        # L = R (khoảng chỉ có 1 phần tử)
        test_cases.append("2 2")        # 2 là số song nguyên tố
        test_cases.append("23 23")      # 23 là số song nguyên tố
        test_cases.append("4 4")        # 4 không phải số song nguyên tố
        test_cases.append("27 27")      # 27 không phải số nguyên tố
        
        # Trường hợp đặc biệt: khoảng chứa nhiều số song nguyên tố
        test_cases.append("10 50")
        test_cases.append("100 200")
        test_cases.append("1000 1100")
        
        # Trường hợp đặc biệt: khoảng ít số song nguyên tố
        test_cases.append("900 950")
        test_cases.append("9900 10000")
        
        # Random với L <= 10^4
        for _ in range(5):
            l = random.randint(2, 10000)
            r = random.randint(l, min(l + 10000, 1000000))
            test_cases.append(f"{l} {r}")
        
        # ===== Test với 10^4 < L <= 10^6 (20% test cases) =====
        
        # Trường hợp biên: L gần 10^4
        test_cases.append("10001 20000")
        test_cases.append("10001 50000")
        
        # Khoảng trung bình
        test_cases.append("50000 60000")
        test_cases.append("100000 110000")
        test_cases.append("500000 510000")
        
        # Trường hợp biên: L gần 10^6
        test_cases.append("990000 1000000")
        test_cases.append("999000 1000000")
        test_cases.append("999900 1000000")
        
        # L = R (khoảng chỉ có 1 phần tử) với L lớn
        test_cases.append("100003 100003")  # 100003 là số nguyên tố
        test_cases.append("999983 999983")  # 999983 là số nguyên tố
        
        # Test hiểm hóc: khoảng cực lớn (sẽ khiến thuật trâu TLE)
        test_cases.append("2 1000000")
        test_cases.append("500000 1000000")
        
        # Random với 10^4 < L <= 10^6
        for _ in range(5):
            l = random.randint(10001, 900000)
            r = random.randint(l, min(l + 100000, 1000000))
            test_cases.append(f"{l} {r}")
        
        # Các trường hợp đặc biệt khác
        
        # Test với các số có tổng chữ số là số nguyên tố nhưng bản thân không phải số nguyên tố
        test_cases.append("100 150")  # Chứa số 121: tổng chữ số là 4, không phải số nguyên tố
        
        # Test với số nguyên tố đặc biệt
        test_cases.append("11 11")    # 11: cả số và tổng chữ số đều là số nguyên tố
        test_cases.append("113 113")  # 113: cả số và tổng chữ số đều là số nguyên tố
        
        # Test hiểm hóc: khoảng chứa nhiều số có tổng chữ số lớn
        test_cases.append("199999 200010")  # Có các số lớn với tổng chữ số lớn
        
        # Đảm bảo trên 30 test case
        return test_cases