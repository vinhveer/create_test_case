from ...generate_test import GenerateTest
import random
import string
import math

class StringReversalTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_s_len", type=int, default=2, help="Độ dài nhỏ nhất của xâu S")
        parser.add_argument("--max_s_len", type=int, default=2*10**5, help="Độ dài lớn nhất của xâu S")
        parser.add_argument("--min_m", type=int, default=1, help="Số lượng thao tác nhỏ nhất")
        parser.add_argument("--max_m", type=int, default=10**5, help="Số lượng thao tác lớn nhất")
        parser.add_argument("--subtask1_only", action="store_true", help="Chỉ tạo test cho subtask 1 (|S|≤10^3, m≤10^3)")
        return parser

    def generate_random_string(self, length):
        """Tạo xâu ngẫu nhiên chỉ gồm chữ cái thường."""
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def generate_valid_operations(self, s_length, num_ops):
        """Tạo các thao tác hợp lệ với điều kiện |S|/2 < k ≤ |S|."""
        min_k = s_length // 2 + 1  # Đảm bảo k > |S|/2
        max_k = s_length  # k ≤ |S|
        return [random.randint(min_k, max_k) for _ in range(num_ops)]

    def calculate_file_size(self, s, m, operations):
        """Ước tính kích thước file test (KB)."""
        size = len(s) + 1  # Xâu S + xuống dòng
        size += len(str(m)) + 1  # Số m + xuống dòng
        size += sum(len(str(op)) for op in operations) + m - 1  # Các thao tác + khoảng trắng
        return size / 1024  # Chuyển đổi sang KB

    def adjust_to_fit_limit(self, s, m, operations, max_size_kb=50):
        """Điều chỉnh test để không vượt quá giới hạn kích thước."""
        file_size = self.calculate_file_size(s, m, operations)
        
        # Nếu đã dưới giới hạn, không cần điều chỉnh
        if file_size <= max_size_kb:
            return s, m, operations
            
        # Ưu tiên giảm số lượng thao tác trước
        while file_size > max_size_kb and m > 1:
            m = m // 2
            operations = operations[:m]
            file_size = self.calculate_file_size(s, m, operations)
            
        # Nếu vẫn vượt quá, giảm độ dài xâu
        while file_size > max_size_kb and len(s) > 2:
            s = s[:len(s)//2]
            # Cập nhật lại các thao tác cho phù hợp với độ dài xâu mới
            operations = self.generate_valid_operations(len(s), m)
            file_size = self.calculate_file_size(s, m, operations)
            
        return s, m, operations

    def generate_inputs(self, params):
        test_cases = []
        min_s_len = getattr(params, "min_s_len", 2)
        max_s_len = getattr(params, "max_s_len", 2*10**5)
        min_m = getattr(params, "min_m", 1)
        max_m = getattr(params, "max_m", 10**5)
        subtask1_only = getattr(params, "subtask1_only", False)
        
        if subtask1_only:
            max_s_len = min(max_s_len, 10**3)
            max_m = min(max_m, 10**3)
        
        # 1. Test case mẫu từ đề bài
        test_cases.append("abcdef\n3\n5 6 4")
        
        # 2. Test nhỏ nhất (|S|=2, m=1)
        s = self.generate_random_string(2)
        operations = [2]  # Với |S|=2, k chỉ có thể là 2
        test_cases.append(f"{s}\n1\n2")
        
        # 3. Xâu toàn một ký tự
        s_len = random.randint(50, 200)
        s = 'a' * s_len
        m = random.randint(10, 30)
        operations = self.generate_valid_operations(s_len, m)
        test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 4. Xâu đối xứng
        half_len = random.randint(25, 100)
        half = self.generate_random_string(half_len)
        s = half + half[::-1]
        m = random.randint(10, 30)
        operations = self.generate_valid_operations(len(s), m)
        test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 5. Thao tác liên tục với cùng một k
        s_len = random.randint(50, 200)
        s = self.generate_random_string(s_len)
        m = random.randint(10, 50)
        k = random.randint(s_len // 2 + 1, s_len)
        operations = [k] * m
        test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 6. Test với k ở cận biên (gần |S|/2)
        s_len = random.randint(100, 300)
        s = self.generate_random_string(s_len)
        m = random.randint(20, 50)
        min_k = s_len // 2 + 1
        max_k = min_k + 5
        operations = [random.randint(min_k, max_k) for _ in range(m)]
        test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 7. Test với k ở cận biên (gần |S|)
        s_len = random.randint(100, 300)
        s = self.generate_random_string(s_len)
        m = random.randint(20, 50)
        min_k = s_len - 5
        max_k = s_len
        operations = [random.randint(min_k, max_k) for _ in range(m)]
        test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 8. Test với xâu có pattern lặp lại
        pattern = self.generate_random_string(5)
        repeat = random.randint(20, 40)
        s = pattern * repeat
        m = random.randint(20, 50)
        operations = self.generate_valid_operations(len(s), m)
        test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 9-13. Tests nhỏ (subtask 1) với độ dài và thao tác ngẫu nhiên
        for _ in range(5):
            s_len = random.randint(min_s_len, min(max_s_len, 10**3))
            m = random.randint(min_m, min(max_m, 10**3))
            s = self.generate_random_string(s_len)
            operations = self.generate_valid_operations(s_len, m)
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 14-18. Tests lớn (TLE cases) cho subtask 2
        if not subtask1_only:
            # Test gây TLE với |S| lớn và m lớn
            s_len = min(max_s_len, 2*10**5)
            m = min(max_m, 10**5)
            s = self.generate_random_string(s_len)
            operations = self.generate_valid_operations(s_len, m)
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
            
            # Test với |S| trung bình nhưng m lớn
            s_len = random.randint(10**4, 5*10**4)
            m = min(max_m, 10**5)
            s = self.generate_random_string(s_len)
            operations = self.generate_valid_operations(s_len, m)
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
            
            # Test với |S| lớn nhưng m trung bình
            s_len = min(max_s_len, 2*10**5)
            m = random.randint(10**4, 5*10**4)
            s = self.generate_random_string(s_len)
            operations = self.generate_valid_operations(s_len, m)
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
            
            # Test với m thao tác xoay quanh điểm giữa
            s_len = random.randint(10**4, 10**5)
            m = random.randint(10**4, 5*10**4)
            s = self.generate_random_string(s_len)
            k_val = s_len // 2 + 1
            operations = [k_val] * m
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
            
            # Test với m thao tác xoay quanh điểm gần cuối
            s_len = random.randint(10**4, 10**5)
            m = random.randint(10**4, 5*10**4)
            s = self.generate_random_string(s_len)
            k_val = s_len - 1
            operations = [k_val] * m
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        # 19-35. Thêm các test ngẫu nhiên để đạt tổng số 35 test
        num_remaining = 35 - len(test_cases)
        for _ in range(num_remaining):
            # Chia đều giữa subtask 1 và subtask 2
            if _ % 2 == 0 or subtask1_only:
                # Test cho subtask 1
                s_len = random.randint(min_s_len, min(max_s_len, 10**3))
                m = random.randint(min_m, min(max_m, 10**3))
            else:
                # Test cho subtask 2
                s_len = random.randint(10**3 + 1, min(max_s_len, 2*10**5))
                m = random.randint(10**3 + 1, min(max_m, 10**5))
            
            s = self.generate_random_string(s_len)
            operations = self.generate_valid_operations(s_len, m)
            s, m, operations = self.adjust_to_fit_limit(s, m, operations)
            test_cases.append(f"{s}\n{m}\n{' '.join(map(str, operations))}")
        
        return test_cases