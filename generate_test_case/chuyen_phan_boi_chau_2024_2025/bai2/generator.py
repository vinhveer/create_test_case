from ...generate_test import GenerateTest
import random
import string

class GIAIMATestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--max_test_size", type=int, default=50_000, help="Max size (bytes) for each test case")
        return parser

    def encode_T(self, S, ch):
        K = ''.join([c for c in S if c != ch])
        return S + K

    def generate_inputs(self, params):
        test_cases = []

        # Các test nhỏ và đa dạng trước
        test_cases.append("ab\na")
        test_cases.append("abcde\nz")
        test_cases.append("aaaaa\na")
        test_cases.append("abcabc\nx")
        test_cases.append("abcab\nc")
        test_cases.append("abcabcc\nb")
        test_cases.append("a\na")
        test_cases.append("bb\nc")
        test_cases.append("aa\na")
        test_cases.append("ab\na")
        test_cases.append("bc\na")
        test_cases.append("abcde\nc")
        test_cases.append("abcdeabcdf\na")

        # Đa dạng các trường hợp đặc biệt/hiểm hóc
        S = "abacadae"; ch = "a"
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "a" + ''.join(random.choices(string.ascii_lowercase.replace("a", ""), k=10)); ch = "a"
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = ''.join(random.choices(string.ascii_lowercase.replace("b", ""), k=10)) + "b"; ch = "b"
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = ''.join(random.sample(string.ascii_lowercase, 10)); ch = random.choice(S)
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "tttttt"; ch = 't'
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "".join(['a' if i%2==0 else 'b' for i in range(20)]); ch = 'a'
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "".join(['b' if i%2==0 else 'a' for i in range(20)]); ch = 'b'
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "acbacbacb"; ch = 'c'
        test_cases.append(f"{S+S}\n{ch}")
        S = ''.join(random.choices(string.ascii_lowercase, k=50)); ch = 'a'
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = ''.join(random.choices(string.ascii_lowercase, k=50)); ch = 'z'
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "abcabcabcabc"; ch = "b"
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        test_cases.append("abcdefghi\nj")
        S = "bbbbbbbb"; ch = "a"
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "cccccccc"; ch = "c"
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = ''.join(random.choices('bdefghijklmnopqrs', k=100)); ch = 'a'
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")
        S = "aaaaabbbbb"; ch = "a"; T = S + "xxxxxxx"
        test_cases.append(f"{T}\n{ch}")
        S = "abcabcabca"; ch = "a"; T = self.encode_T(S, ch); T_wrong = T[:5] + "z" + T[5:]
        test_cases.append(f"{T_wrong}\n{ch}")
        L = random.randint(10, 30); ch = 'z'; S = 'z'*L
        test_cases.append(f"{self.encode_T(S, ch)}\n{ch}")

        # Các test dài nhưng không vượt max_test_size bytes
        max_size = params.max_test_size
        # S dài nhất không có ch
        S = ''.join(random.choices('bcdefghijklmnopqrstuvwxyz', k=max_size//2))
        ch = 'a'
        T = self.encode_T(S, ch)
        if len(T) + 2 <= max_size:  # +2 cho \n và ký tự ch
            test_cases.append(f"{T}\n{ch}")

        # S dài nhất, nhiều ch
        S = ''.join(random.choices('ab', k=max_size//2))
        ch = 'a'
        T = self.encode_T(S, ch)
        if len(T) + 2 <= max_size:
            test_cases.append(f"{T}\n{ch}")

        # S dài nhất, ch bất kỳ, đúng quy tắc
        S = ''.join(random.choices(string.ascii_lowercase, k=max_size//2))
        ch = random.choice(string.ascii_lowercase)
        T = self.encode_T(S, ch)
        if len(T) + 2 <= max_size:
            test_cases.append(f"{T}\n{ch}")

        # S dài nhất, T = S+S (sai quy tắc)
        S = ''.join(random.choices(string.ascii_lowercase, k=max_size//2))
        ch = random.choice(string.ascii_lowercase)
        T = S + S
        if len(T) + 2 <= max_size:
            test_cases.append(f"{T}\n{ch}")

        # S nhiều ký tự lặp lại, ch xen kẽ, đúng quy tắc
        S = "ab" * (max_size//4)
        ch = "b"
        T = self.encode_T(S, ch)
        if len(T) + 2 <= max_size:
            test_cases.append(f"{T}\n{ch}")

        # Đảm bảo tổng kích thước không vượt 1MB (cả .in + .out)
        # Nếu muốn chắc chắn, nên chỉ lấy tối đa 20 test lớn nhất (50KB*20=1000KB), còn lại là test nhỏ/trung bình
        acc_size = 0
        filtered_cases = []
        MAX_TOTAL = 1_048_576  # 1MB
        for tc in test_cases:
            # Giả sử .out không quá 2*input, lấy biên an toàn là *3
            est_total = acc_size + 3*len(tc.encode('utf-8'))
            if est_total > MAX_TOTAL:
                break
            filtered_cases.append(tc)
            acc_size += len(tc.encode('utf-8'))
        return filtered_cases