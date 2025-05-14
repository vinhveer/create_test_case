# Dựa theo yêu cầu của bạn, class sinh test đầy đủ các trường hợp

from ...generate_test import GenerateTest
import random

class MAHS_TestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_len", type=int, default=6, help="Min số chữ số")
        parser.add_argument("--max_len", type=int, default=7, help="Max số chữ số")
        return parser

    def make_valid_mahs(self, length):
        """Sinh ra một mã học sinh hợp lệ, trả về dạng string"""
        mul = [9, 7, 3, 9, 7, 3, 9]
        while True:
            digits = [random.randint(1,9)] + [random.randint(0,9) for _ in range(length-1)]
            # Chỉnh lại chữ số cuối để tổng kiểm tra %10 == 0
            # Tính tổng kiểm tra với các chữ số hiện tại
            total = sum(digits[i]*mul[i] for i in range(length))
            # Điều chỉnh số cuối để tổng kiểm tra %10 == 0
            # (giả sử không phải vị trí đầu)
            for i in range(length):
                orig = digits[i]
                for d in range(0 if i>0 else 1, 10):
                    digits[i] = d
                    total2 = sum(digits[j]*mul[j] for j in range(length))
                    if total2 % 10 == 0:
                        # Tìm được số hợp lệ
                        return ''.join(str(x) for x in digits)
                digits[i] = orig

    def generate_inputs(self, params):
        test_cases = []

        # 1. Edge: mã 6 số, ? ở đầu (nhưng đầu luôn khác 0)
        for d in range(1, 10):
            digits = [str(d)] + [str(random.randint(0, 9)) for _ in range(5)]
            # Tính tổng kiểm tra, sửa số cuối để hợp lệ
            mul = [9, 7, 3, 9, 7, 3, 9]
            total = sum(int(digits[i]) * mul[i] for i in range(6))
            digits[-1] = str((10 - (total - int(digits[-1]) * mul[5]) % 10) % 10)
            # Thay số đầu thành ?
            digits[0] = '?'
            test_cases.append(''.join(digits))

        # 2. Edge: mã 7 số, ? ở cuối
        s = self.make_valid_mahs(7)
        s2 = s[:-1] + '?'
        test_cases.append(s2)

        # 3. Edge: ? ở giữa
        s = self.make_valid_mahs(6)
        for i in range(1, 6):
            t = list(s)
            t[i] = '?'
            test_cases.append(''.join(t))

        # 4. All digits are same except ?
        for l in [6, 7]:
            digits = [str(5)] * l
            # Tính tổng kiểm tra, sửa số cuối
            mul = [9, 7, 3, 9, 7, 3, 9]
            total = sum(int(digits[i]) * mul[i] for i in range(l))
            digits[-1] = str((10 - (total - int(digits[-1]) * mul[l-1]) % 10) % 10)
            # Chọn vị trí ? bất kỳ khác 0
            pos = random.randint(1, l-1)
            digits[pos] = '?'
            test_cases.append(''.join(digits))

        # 5. Trường hợp đảo ngược
        s = self.make_valid_mahs(7)[::-1]
        pos = random.randint(1, 6)
        s = s[:pos] + '?' + s[pos+1:]
        test_cases.append(s)

        # 6. Dãy số xen kẽ 1/9
        for l in [6, 7]:
            digits = [str(1 if i % 2 == 0 else 9) for i in range(l)]
            # Tính tổng kiểm tra, sửa số cuối
            mul = [9, 7, 3, 9, 7, 3, 9]
            total = sum(int(digits[i]) * mul[i] for i in range(l))
            digits[-1] = str((10 - (total - int(digits[-1]) * mul[l-1]) % 10) % 10)
            pos = random.randint(1, l-1)
            digits[pos] = '?'
            test_cases.append(''.join(digits))

        # 7. Random hợp lệ với ? random
        for _ in range(10):
            l = random.randint(getattr(params, "min_len", 6), getattr(params, "max_len", 7))
            s = self.make_valid_mahs(l)
            pos = random.randint(1, l-1)
            t = list(s)
            t[pos] = '?'
            test_cases.append(''.join(t))

        # 8. Tricky: mã bắt đầu bằng 1, nhiều số 0 ở cuối
        digits = ["1"] + ["0"] * 5
        mul = [9, 7, 3, 9, 7, 3, 9]
        total = sum(int(digits[i]) * mul[i] for i in range(6))
        digits[-1] = str((10 - (total - int(digits[-1]) * mul[5]) % 10) % 10)
        digits[random.randint(1,5)] = '?'
        test_cases.append(''.join(digits))

        # 9. Trường hợp đề bài
        test_cases.append("1?90272")

        return test_cases