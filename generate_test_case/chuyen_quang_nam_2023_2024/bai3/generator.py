from ...generate_test import GenerateTest
import random
import string

class LONGWORDTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_len", type=int, default=1, help="Min length of S")
        parser.add_argument("--max_len", type=int, default=255, help="Max length of S (small test)")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_len = getattr(params, "min_len", 1)
        max_len = getattr(params, "max_len", 255)

        # 1. Biên nhỏ nhất: 1 ký tự không phải space
        test_cases.append("A")
        # 2. 1 ký tự là space
        test_cases.append(" ")
        # 3. Hai ký tự là hai từ
        test_cases.append("A B")
        # 4. Chỉ toàn space
        test_cases.append(" " * min(10, max_len))
        # 5. Một từ duy nhất, độ dài max
        test_cases.append("A" * max_len)
        # 6. Một từ ở đầu, nhiều space, một từ ở cuối
        test_cases.append("A" + " " * (max_len//2) + "B")
        # 7. Chuỗi có nhiều space ở đầu, cuối, giữa
        test_cases.append(" " * 5 + "Hello" + " " * 8 + "World" + " " * 7)
        # 8. Từ lặp lại, dài bằng nhau
        test_cases.append("abc def ghi abc def ghi")
        # 9. Các từ độ dài tăng dần
        words = ["a", "bb", "ccc", "dddd", "eeeee"]
        test_cases.append(" ".join(words))
        # 10. Các từ độ dài giảm dần
        words = ["zzzzz", "yyyy", "xxx", "ww", "v"]
        test_cases.append(" ".join(words))
        # 11. Xen kẽ chữ hoa, chữ thường, nhiều space giữa các từ
        test_cases.append("HeLLo     WoRLD   tHis  IS   a   TEST")
        # 12. Các từ có ký tự đặc biệt, số, dấu cách bất kỳ
        test_cases.append("!@# $%^ &*() _+123 456abc")
        # 13. Chuỗi có các từ giống nhau nhưng khác viết hoa/thường
        test_cases.append("abc ABC aBc Abc")
        # 14. Chuỗi palindrome từng từ
        test_cases.append("aba bab cdc")
        # 15. Chuỗi gồm 1 từ cực dài ở giữa nhiều space
        test_cases.append(" " * 10 + "X" * (max_len - 20) + " " * 10)
        # 16. Chuỗi có nhiều từ đơn ký tự cách nhau bởi nhiều space
        test_cases.append("A  B   C    D     E")
        # 17. Chuỗi có từ dài nhất ở đầu, cuối, giữa
        test_cases.append("LONG short med LONGEST med short endd LONGEST")
        # 18-20: Random chuỗi, độ dài max_len, random space xen kẽ
        for _ in range(3):
            l = max_len
            S = ""
            while len(S) < l:
                if random.random() < 0.2:
                    S += " " * random.randint(1, 4)
                else:
                    wlen = random.randint(1, min(10, l - len(S)))
                    S += ''.join(random.choices(string.ascii_letters, k=wlen))
            S = S[:l]
            test_cases.append(S)
        # 21. Chuỗi có từ dài nhất xuất hiện nhiều lần
        test_cases.append("maxword a b maxword c d maxword")
        # 22. Chuỗi tất cả các từ độ dài 1, cách nhau bởi nhiều space
        test_cases.append(" ".join(["x"]*20))
        # 23. Chuỗi chỉ toàn 1 ký tự lặp lại, không space
        test_cases.append("y" * max_len)
        # 24. Chuỗi có từ dài nhất ở đầu, các từ nhỏ xen kẽ
        test_cases.append("LONGEST a b c d e")
        # 25. Chuỗi có từ dài nhất ở cuối, các từ nhỏ xen kẽ
        test_cases.append("a b c d e LONGEST")
        # 26. Chuỗi có từ dài nhất ở giữa, các từ nhỏ xen kẽ
        test_cases.append("a b LONGEST c d")
        # 27. Chuỗi có nhiều space liên tiếp ở đầu, đầu vào là palindrome
        test_cases.append("   racecar anna civic  ")
        # 28. Chuỗi có dấu xuống dòng (cắt bỏ, chỉ lấy dòng đầu)
        test_cases.append("one two three\nfour five six")
        # 29-40: Random các chuỗi, độ dài random
        for _ in range(12):
            l = random.randint(1, max_len)
            S = ""
            while len(S) < l:
                if random.random() < 0.15:
                    S += " " * random.randint(1, 4)
                else:
                    wlen = random.randint(1, min(10, l - len(S)))
                    S += ''.join(random.choices(string.ascii_letters, k=wlen))
            S = S[:l]
            test_cases.append(S)
        return test_cases