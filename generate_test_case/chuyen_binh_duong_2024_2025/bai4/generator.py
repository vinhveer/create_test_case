# Sinh test cho bài toán hoán vị chênh lệch K, bao quát edge/tricky/đặc biệt

from ...generate_test import GenerateTest
import random

class HoanViKTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=8, help="Max n cho test trâu")
        parser.add_argument("--rand_sample", type=bool, default=True, help="Sinh thêm test ngẫu nhiên")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1. Biên nhỏ nhất N=1, K=0
        test_cases.append("1\n0")

        # 2. K = N-1 (chỉ có thể swap đầu/cuối)
        test_cases.append(f"4\n3")
        test_cases.append(f"5\n4")

        # 3. K = 0 (mảng không đổi, chỉ có thể là hoán vị chính nó)
        test_cases.append(f"5\n0")

        # 4. K = 1 (tìm hoán vị lệch 1 vị trí)
        test_cases.append(f"4\n1")

        # 5. K = N//2 (nếu N chẵn, có thể chia khối)
        test_cases.append(f"6\n3")

        # 6. Trường hợp không có đáp án (N lẻ, K = N//2)
        test_cases.append(f"5\n2")

        # 7. N nhỏ, K bất kỳ
        for n in range(2, 9):
            for k in range(1, n):
                test_cases.append(f"{n}\n{k}")

        # 8. Trường hợp đề bài
        test_cases.append("4\n2")

        # 9. N=8, K=4 (tricky, edge max của phép sinh trâu)
        test_cases.append("8\n4")

        # 10. Random N nhỏ
        if getattr(params,"rand_sample",True):
            for _ in range(5):
                n = random.randint(getattr(params,"min_n",1), getattr(params,"max_n",8))
                k = random.randint(0, n-1)
                test_cases.append(f"{n}\n{k}")

        return test_cases