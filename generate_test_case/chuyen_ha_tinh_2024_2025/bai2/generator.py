import random
from ...generate_test import GenerateTest

"""
  -----------------------------
  Test Generator for "Đếm ước" (Bài 2)
  -----------------------------

  Ràng buộc bài toán:
    - 1 ≤ n ≤ 10^6
    - 1 ≤ a[i] ≤ 10^6

  Trong ví dụ này, chúng ta giới hạn n ở mức tương đối nhỏ (<= 50) để đảm bảo đầu ra không vượt 1MB,
  nhưng vẫn cố gắng sinh thêm nhiều test khó, mạo hiểm:
    - Trường hợp n lớn vừa phải, giá trị a[i] lớn xen kẽ a[i] nhỏ.
    - Trường hợp toàn giá trị 1 (có nhiều ước và trùng lặp).
    - Trường hợp giá trị chẵn/lẻ xen kẽ tạo nhiều ước.
    - Trường hợp các giá trị lũy thừa (2^k, 3^k, ...), dễ gây nhiều ước.
    - Trường hợp có số nguyên tố lớn, số 1, ...
    - Trường hợp ngẫu nhiên cỡ trung bình.

  Yêu cầu test:
    - Phải bao quát các tình huống biên, lũy thừa, xen kẽ, ...
    - Đa dạng để "làm khó" các giải pháp.
"""

class TICHTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min N")
        parser.add_argument("--max_n", type=int, default=50, help="Max N to keep under 1MB for demonstration")
        return parser

    def generate_inputs(self, params):
        test_cases = []

        # 1) n = 1, a = 1 (nhỏ nhất)
        test_cases.append("1\n1")

        # 2) n = 3, các số khác nhau hoàn toàn
        test_cases.append("3\n1 2 3")

        # 3) n = 5, all same (2)
        test_cases.append("5\n2 2 2 2 2")

        # 4) n = 5, near 10^6
        test_cases.append("5\n999999 1000000 1000000 999999 500000")

        # 5) n = 10, random trong [1..100]
        arr = [random.randint(1, 100) for _ in range(10)]
        test_cases.append(f"10\n{' '.join(map(str, arr))}")

        # 6) n = 15, random trong [1..10^6]
        arr = [random.randint(1, 10**6) for _ in range(15)]
        test_cases.append(f"15\n{' '.join(map(str, arr))}")

        # 7) n = 20, random trong [1..10^6]
        arr = [random.randint(1, 10**6) for _ in range(20)]
        test_cases.append(f"20\n{' '.join(map(str, arr))}")

        # 8) n = 8, trộn lẫn số 1, số nguyên tố, số chẵn, số lũy thừa
        #    Ví dụ: 1, 2, 16, 17, 36, 999983 (prime), 500000, 999991 (prime)
        #    => Tạo "khó" do 999983 và 999991 là số nguyên tố lớn.
        tricky_arr = [1, 2, 16, 17, 36, 999983, 500000, 999991]
        test_cases.append(f"{len(tricky_arr)}\n{' '.join(map(str, tricky_arr))}")

        # 9) n = 7, toàn lũy thừa của 2 => nhiều ước
        #    2, 4, 8, 16, 32, 64, 128
        powers_of_2 = [2**i for i in range(1, 8)]
        test_cases.append(f"7\n{' '.join(map(str, powers_of_2))}")

        # 10) n = 7, toàn lũy thừa của 3 => test ước (3^x)
        #     3, 9, 27, 81, 243, 729, 2187
        powers_of_3 = [3**i for i in range(1, 8)]
        test_cases.append(f"7\n{' '.join(map(str, powers_of_3))}")

        # 11) n = 10, trộn: nhiều 1 + nhiều số chẵn + 1 số lẻ lớn
        arr_mixed = [1, 1, 2, 2, 2, 4, 16, 256, 999999, 1000000]
        test_cases.append(f"{len(arr_mixed)}\n{' '.join(map(str, arr_mixed))}")

        return test_cases