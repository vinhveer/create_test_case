from ...generate_test import GenerateTest
import random

# Hàm so sánh 2 số nguyên dương lớn dưới dạng chuỗi
def cmp_str_num(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    return (a > b) - (a < b)  # trả về 1 nếu a > b, -1 nếu a < b, 0 nếu bằng nhau

class LargestNumberWithoutSGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_N", type=int, default=1, help="Min số chữ số của P")
        parser.add_argument("--max_N", type=int, default=8, help="Max số chữ số của P cho test trâu")
        parser.add_argument("--max_big_N", type=int, default=100000, help="Max số chữ số của P cho test lớn")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # Các test case như bản cũ (không đổi)

        # 1. Edge: P nhỏ nhất
        test_cases.append("1\n1")

        # 2. S là 1 chữ số, P nhỏ
        test_cases.append("123\n2")

        # 3. S là nhiều chữ số liên tiếp
        test_cases.append("7890\n789")

        # 4. S là 1, P là số toàn 9 (max số không forbidden)
        test_cases.append("999\n1")

        # 5. P là số có nhiều chữ số, S là 1 chữ số không xuất hiện trong P
        test_cases.append("654321\n9")

        # 6. S là tất cả các chữ số trừ 1
        test_cases.append("87654321\n234567890")

        # 7. P = 2024, S = 23 (test mẫu đề)
        test_cases.append("2024\n23")

        # 8. S có chữ số đầu của P
        test_cases.append("3456\n3")

        # 9. S có chữ số cuối của P
        test_cases.append("1234\n4")

        # 10. S có nhiều chữ số, P là số toàn 1
        test_cases.append("1111\n123456789")

        # 11. S là số lẻ, P là số chẵn
        test_cases.append("8642\n13579")

        # 12. S là số chẵn, P là số lẻ
        test_cases.append("97531\n2468")

        # 13. P = 1e8, S = 0 (không chứa 0)
        test_cases.append("100000000\n0")

        # 14. Tất cả chữ số bị cấm, không có số nào thỏa mãn
        test_cases.append("1234\n1234567890")

        # 15. Random N nhỏ
        for _ in range(4):
            N = random.randint(getattr(params,"min_N",1), getattr(params,"max_N",8))
            # Số đầu không 0
            P = str(random.randint(10**(N-1), 10**N-1))
            S_digits = random.sample([str(i) for i in range(1,10)], random.randint(1,8))
            S = ''.join(S_digits)
            test_cases.append(f"{P}\n{S}")

        # 16. Random N lớn (test hiểm hóc)
        N = getattr(params,"max_big_N",100000)
        P = '9'*N
        S = ''.join(random.sample([str(i) for i in range(1,10)], random.randint(1,8)))
        test_cases.append(f"{P}\n{S}")

        # 17. Random P gồm nhiều chữ số giống nhau
        P = '1'*random.randint(5,8)
        S = ''.join(random.sample([str(i) for i in range(1,10)], random.randint(1,8)))
        test_cases.append(f"{P}\n{S}")

        # 18. P là số giảm dần, S trùng với chữ số đầu/cuối
        P = ''.join(str(i) for i in range(9,0,-1))
        S = f"{P[0]}{P[-1]}"
        test_cases.append(f"{P}\n{S}")

        # 19. P là số tăng dần, S là tập con của P (sửa lại, không dùng stoll để so sánh!)
        P = ''.join(str(i) for i in range(1,10))
        S = ''.join(random.sample(list(P), 3))
        test_cases.append(f"{P}\n{S}")

        # 20. P nhỏ, S là 0 (không có số 0)
        test_cases.append("7\n0")

        return test_cases