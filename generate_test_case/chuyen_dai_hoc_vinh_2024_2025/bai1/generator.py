from ...generate_test import GenerateTest
import random
import math

class SoSongNguyenToTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_L", type=int, default=2, help="Giá trị nhỏ nhất cho L")
        parser.add_argument("--max_R", type=int, default=1000000, help="Giá trị lớn nhất cho R")
        parser.add_argument("--invalid_ratio", type=float, default=0.1, help="Tỷ lệ test không hợp lệ")
        parser.add_argument("--small_ratio", type=float, default=0.7, help="Tỷ lệ test nhỏ (L,R <= 10^4)")
        parser.add_argument("--large_ratio", type=float, default=0.2, help="Tỷ lệ test lớn (L,R <= 10^6)")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        MAX_R = 1000000  # 10^6, giới hạn cao nhất của đề bài
        
        # Lấy các tham số từ dòng lệnh hoặc sử dụng giá trị mặc định
        min_L = getattr(params, "min_L", 2)
        max_R = getattr(params, "max_R", MAX_R)
        invalid_ratio = getattr(params, "invalid_ratio", 0.1)
        small_ratio = getattr(params, "small_ratio", 0.7)
        large_ratio = getattr(params, "large_ratio", 0.2)
        
        # Bắt đầu với test mẫu từ đề bài
        test_cases.append("10 30")
        
        # 1. Các test không hợp lệ (~10%)
        # L <= 1
        test_cases.append("1 100")
        test_cases.append("0 1000000")
        test_cases.append("-5 500000")
        
        # L > R
        test_cases.append("1000 500")
        test_cases.append("1000000 999999")
        
        # R > 10^6
        test_cases.append("500000 2000000")
        test_cases.append("2 10000000")
        
        # 2. Các test biên quan trọng
        # Biên dưới
        test_cases.append("2 1000000")  # Toàn bộ phạm vi hợp lệ
        test_cases.append("2 999999")   # Gần như toàn bộ phạm vi
        
        # Các test với R = MAX_R = 10^6
        test_cases.append("500000 1000000")  # Nửa trên của phạm vi
        test_cases.append("900000 1000000")  # 10% cuối
        test_cases.append("990000 1000000")  # 1% cuối
        test_cases.append("999900 1000000")  # 0.1% cuối
        
        # 3. Các test nhỏ (1 < L ≤ 10^4) - chiếm 70%
        # Test với khoảng cách lớn
        test_cases.append("2 10000")        # Toàn bộ phạm vi nhỏ
        test_cases.append("100 10000")      # Phần lớn phạm vi nhỏ
        test_cases.append("5000 1000000")   # Từ giữa phạm vi nhỏ đến max
        test_cases.append("9000 1000000")   # Từ gần cuối phạm vi nhỏ đến max
        
        # Thêm các test nhỏ khác với khoảng cách đa dạng
        L_values = [2, 10, 50, 100, 500, 1000, 2000, 5000, 8000, 9000, 9900]
        for L in L_values:
            # Đảm bảo R - L lớn hơn nhiều
            R = random.randint(min(L + 10000, MAX_R - 1), MAX_R)
            test_cases.append(f"{L} {R}")
        
        # 4. Các test lớn (10^4 < L ≤ 10^6) - chiếm 20%
        # Test với các khoảng bắt đầu từ mỗi mức 10^5
        for start in [10001, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]:
            # Đảm bảo khoảng cách R - L lớn, nhưng R <= 10^6
            R = random.randint(min(start + 50000, MAX_R - 1), MAX_R)
            test_cases.append(f"{start} {R}")
        
        # 5. Các test với khoảng rộng cực lớn (nhiều nhất có thể để gây TLE)
        large_gaps = [
            (2, 900000),          # Gần như toàn bộ phạm vi
            (2, 800000),          # 80% phạm vi
            (2, 700000),          # 70% phạm vi
            (2, 600000),          # 60% phạm vi
            (2, 500000),          # Nửa phạm vi
            (100000, 1000000),    # 90% phạm vi cao
            (200000, 1000000),    # 80% phạm vi cao
            (300000, 1000000),    # 70% phạm vi cao
            (10001, 900000),      # Từ sau phạm vi nhỏ đến gần max
            (50000, 950000),      # Khoảng giữa, rộng
            (100, 999000),        # Từ gần biên dưới đến gần biên trên
        ]
        
        for L, R in large_gaps:
            test_cases.append(f"{L} {R}")
        
        # 6. Thêm một số test ngẫu nhiên để đảm bảo đủ số lượng và đa dạng
        while len(test_cases) < 40:
            # 50% khả năng sinh test lớn với khoảng rộng
            if random.random() < 0.5:
                L = random.randint(10001, 800000)
                R = random.randint(L + 100000, MAX_R)
            else:
                L = random.randint(2, 10000)
                R = random.randint(L + 50000, MAX_R)
            
            test_cases.append(f"{L} {R}")
        
        return test_cases