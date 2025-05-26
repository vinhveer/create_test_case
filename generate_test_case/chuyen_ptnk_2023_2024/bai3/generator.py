from ...generate_test import GenerateTest
import random

class SUBRECTTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=8000, help="Max n")
        parser.add_argument("--min_val", type=int, default=1, help="Min value for array elements")
        parser.add_argument("--max_val", type=int, default=100, help="Max value for array elements")
        parser.add_argument("--min_k", type=int, default=1, help="Min sum k")
        parser.add_argument("--max_k", type=int, default=1000000, help="Max sum k")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        
        # Số lượng test cho mỗi nhóm
        small_n_tests = 10  # Tests với n nhỏ
        medium_n_tests = 10  # Tests với n trung bình
        large_n_tests = 12  # Tests với n lớn
        
        # 1. Test mẫu từ đề bài
        test_cases.append("5\n2 4 1 5 3\n30")
        
        # 2. Trường hợp biên: n = 1 (nhỏ nhất)
        n = 1
        a = [random.randint(1, 10)]  # Giá trị dương để tránh chia cho 0
        k = a[0] * a[0]  # Tạo kết quả chính xác
        test_cases.append(f"{n}\n{a[0]}\n{k}")
        
        # 3. Thay test case toàn số 0 bằng test với số nhỏ
        n = 5
        a = [1] * n  # Toàn số 1 thay vì số 0
        k = n  # Tổng của một hàng/cột
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 4. Test case toàn số 1 với k phù hợp
        n = 5
        a = [1] * n
        k = 9  # Tổng của hình chữ nhật 3x3
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 5. Trường hợp không có giải pháp
        n = 5
        a = [1, 2, 3, 4, 5]
        k = 1000000  # Giá trị quá lớn
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 6. Trường hợp k = 1 (nhỏ nhất)
        n = 5
        a = [1, 2, 3, 4, 5]  # Mảng toàn số dương
        k = 1
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 7. Trường hợp k lớn nhất với n nhỏ
        n = 10
        a = [100] * n  # Toàn giá trị lớn nhất
        k = 1000000  # k lớn nhất
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 8-17. Tests với n nhỏ (n ≤ 100)
        for _ in range(small_n_tests):
            n = random.randint(5, 100)
            # Chỉ dùng giá trị dương từ 1-100 để tránh tổng bằng 0
            a = [random.randint(1, 100) for _ in range(n)]
            
            # Chọn k một cách chiến lược
            if random.random() < 0.3:
                # 30% cơ hội chọn k có thể có giải pháp
                row_start = random.randint(0, n-1)
                row_end = random.randint(row_start, min(row_start+10, n-1))
                col_start = random.randint(0, n-1)
                col_end = random.randint(col_start, min(col_start+10, n-1))
                
                # Tính tổng của hình chữ nhật
                sum_rect = 0
                for i in range(row_start, row_end+1):
                    for j in range(col_start, col_end+1):
                        sum_rect += a[i] * a[j]
                
                k = max(1, min(sum_rect, 1000000))
            else:
                # 70% cơ hội cho k ngẫu nhiên
                k = random.randint(1, 1000000)
            
            test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 18-27. Tests với n trung bình (100 < n ≤ 1000)
        for _ in range(medium_n_tests):
            n = random.randint(101, 1000)
            
            # Tạo mảng với cấu trúc đặc biệt
            if random.random() < 0.5:
                # 50% cơ hội cho mảng có mẫu cấu trúc
                pattern_type = random.randint(1, 4)
                
                if pattern_type == 1:
                    # Giá trị xen kẽ nhỏ/lớn
                    a = [(i % 2) * 50 + random.randint(1, 50) for i in range(n)]
                elif pattern_type == 2:
                    # Mẫu tuần hoàn
                    period = random.randint(2, 10)
                    a = [i % period * (100 // period) + random.randint(1, 10) for i in range(n)]
                elif pattern_type == 3:
                    # Nhiều giá trị lớn ở các vị trí ngẫu nhiên
                    a = [1] * n  # Đảm bảo tất cả phần tử > 0
                    for i in range(n // 10):
                        a[random.randint(0, n-1)] = random.randint(50, 100)
                else:
                    # Tăng rồi giảm
                    mid = n // 2
                    a = [min(i, n-i) for i in range(n)]
                    a = [v * 100 // mid + 1 for v in a]  # +1 để đảm bảo > 0
            else:
                # 50% cơ hội cho mảng hoàn toàn ngẫu nhiên
                a = [random.randint(1, 100) for _ in range(n)]
            
            # Chọn k một cách chiến lược
            if random.random() < 0.3:
                # Chọn ước của một tích phổ biến
                common_products = []
                for i in range(min(100, n)):
                    row_sum = sum(a[max(0, i-5):min(n, i+6)])
                    if 1 <= row_sum <= 1000:
                        common_products.append(row_sum)
                
                if common_products:
                    factor1 = random.choice(common_products)
                    factor2 = min(1000000 // factor1, 1000)
                    k = factor1 * factor2
                else:
                    k = random.randint(1, 1000000)
            else:
                k = random.randint(1, 1000000)
                
            test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # 28-39. Tests với n lớn (1000 < n ≤ 8000)
        for i in range(large_n_tests):
            if i == 0:
                # Một test với n lớn nhất
                n = 8000
            else:
                n = random.randint(1001, 8000)
            
            # Sinh mảng với các đặc tính khác nhau
            array_type = i % 5
            
            if array_type == 0:
                # Chủ yếu là giá trị nhỏ
                a = [random.randint(1, 20) for _ in range(n)]
            elif array_type == 1:
                # Nhiều giá trị 1 với một số giá trị lớn
                a = [1] * n
                for j in range(n // 5):
                    a[random.randint(0, n-1)] = random.randint(2, 100)
            elif array_type == 2:
                # Mảng nhị phân (chỉ có 1 và 2)
                a = [random.randint(1, 2) for _ in range(n)]
            elif array_type == 3:
                # Cấu trúc khối
                block_size = random.randint(100, 500)
                a = []
                for j in range(0, n, block_size):
                    block_val = random.randint(1, 100)
                    a.extend([block_val] * min(block_size, n-j))
            else:
                # Ngẫu nhiên với xác suất cao cho số 1 và 2
                a = []
                for _ in range(n):
                    r = random.random()
                    if r < 0.4:
                        a.append(1)
                    elif r < 0.7:
                        a.append(2)
                    else:
                        a.append(random.randint(3, 100))
            
            # Chọn k một cách chiến lược
            if i % 2 == 0:
                # Tìm k có thể có giải pháp
                factor1 = random.randint(1, 1000)
                factor2 = random.randint(1, min(1000, 1000000 // factor1))
                k = factor1 * factor2
            else:
                # k ngẫu nhiên
                k = random.randint(1, 1000000)
            
            test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # Thêm vài test đặc biệt để đủ 37 test
        # Test có chính xác một giải pháp
        n = 20
        a = [1] * n
        a[0] = 2  # Tạo hình chữ nhật góc trên bên trái đặc biệt
        k = 4     # 2*2 = 4
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # Test có nhiều giải pháp giống nhau
        n = 15
        a = [3] * n  # Toàn số 3
        k = 9     # 3*3 = 9, sẽ có nhiều hình chữ nhật thỏa mãn
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        # Test có k là số nguyên tố lớn
        n = 30
        a = [random.randint(1, 100) for _ in range(n)]
        k = 999983  # Số nguyên tố lớn gần 10^6
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{k}")
        
        return test_cases