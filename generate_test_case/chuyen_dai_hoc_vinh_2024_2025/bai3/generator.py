from ...generate_test import GenerateTest
import random
import string

class PasswordTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min number of lines")
        parser.add_argument("--max_n", type=int, default=20000, help="Max number of lines")
        parser.add_argument("--min_line_length", type=int, default=1, help="Min length of each line")
        parser.add_argument("--max_line_length", type=int, default=256, help="Max length of each line")
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
        
    def generate_random_string(self, length, with_spaces=True, with_duplicates=True):
        """Generate a random string with specified properties"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        if with_spaces:
            chars += " "
            
        if with_duplicates:
            return ''.join(random.choice(chars) for _ in range(length))
        else:
            # If no duplicates allowed, ensure length doesn't exceed available chars
            max_possible = len(chars)
            actual_length = min(length, max_possible)
            return ''.join(random.sample(chars, actual_length))
            
    def generate_line_with_password(self, line_length, password_length, password_position="random"):
        """Generate a line with a hidden password of specified length"""
        # Generate a password (all unique chars, no spaces)
        password = self.generate_random_string(password_length, with_spaces=False, with_duplicates=False)
        
        # Calculate remaining length
        remaining_length = line_length - password_length
        
        if remaining_length <= 0:
            return password
            
        # Decide password position
        if password_position == "start":
            prefix_length = 0
            suffix_length = remaining_length
        elif password_position == "end":
            prefix_length = remaining_length
            suffix_length = 0
        else:  # random
            prefix_length = random.randint(0, remaining_length)
            suffix_length = remaining_length - prefix_length
            
        # Generate prefix and suffix
        prefix = self.generate_random_string(prefix_length) if prefix_length > 0 else ""
        suffix = self.generate_random_string(suffix_length) if suffix_length > 0 else ""
        
        return prefix + password + suffix
        
    def generate_line_with_multiple_passwords(self, line_length, min_length=3, max_length=10, count=2):
        """Generate a line with multiple potential passwords of varying lengths"""
        passwords = []
        total_length = 0
        
        # Generate passwords with increasing lengths
        for i in range(count):
            if i == count - 1:  # Last password should be longest
                pwd_length = max_length
            else:
                pwd_length = random.randint(min_length, max_length-1)
                
            password = self.generate_random_string(pwd_length, with_spaces=False, with_duplicates=False)
            passwords.append(password)
            total_length += pwd_length
            
        # Calculate remaining length
        remaining_length = line_length - total_length
        
        if remaining_length < count - 1:  # Need at least count-1 separators
            # Just return the last password if we can't fit everything
            return passwords[-1]
            
        # Create separators (random strings with spaces)
        separators = []
        for i in range(count - 1):
            if i == count - 2:  # Last separator gets all remaining space
                sep_length = remaining_length - sum(len(s) for s in separators)
            else:
                sep_length = random.randint(1, remaining_length // (count - i))
                remaining_length -= sep_length
                
            separator = self.generate_random_string(sep_length)
            separators.append(separator)
            
        # Interleave passwords and separators
        result = ""
        for i in range(count - 1):
            result += passwords[i] + separators[i]
        result += passwords[-1]
        
        return result

    def generate_inputs(self, params):
        test_cases = []
        
        # Sample test from the problem statement
        test_cases.append("3\nGood morning!\nHow are you?\nHave a nice day!")
        
        # ===== Subtask 1: 1 <= n <= 10^4 (50% of tests) =====
        
        # Edge case: n = 1
        test_cases.append("1\nHello World!")
        
        # Edge case: Empty line
        test_cases.append("1\n ")
        
        # Edge case: Single character
        test_cases.append("2\na\nz")
        
        # Edge case: Line with only spaces
        test_cases.append("1\n      ")
        
        # Special case: All characters unique
        test_cases.append("1\nabcdefghijklmnopqrstuvwxyz")
        
        # Special case: All characters duplicated
        test_cases.append("1\naabbccddeeffgghhiijjkkllmm")
        
        # Special case: Line with spaces between each character
        test_cases.append("1\na b c d e f g h i j k")
        
        # Tricky case: Multiple valid passwords of same length
        test_cases.append("2\nabc def ghi\njkl mno pqr")
        
        # Small test with multiple lines
        small_test = ["5"]
        for _ in range(5):
            line_length = random.randint(10, 30)
            pwd_length = random.randint(3, 8)
            line = self.generate_line_with_password(line_length, pwd_length)
            small_test.append(line)
        test_cases.append("\n".join(small_test))
        
        # Medium test with n = 100
        medium_test = ["100"]
        for _ in range(100):
            line_length = random.randint(20, 100)
            pwd_length = random.randint(5, 15)
            line = self.generate_line_with_password(line_length, pwd_length)
            medium_test.append(line)
        test_cases.append("\n".join(medium_test))
        
        # Large test with n = 1000
        large_test_1 = ["1000"]
        for _ in range(1000):
            line_length = random.randint(50, 150)
            pwd_length = random.randint(10, 20)
            line = self.generate_line_with_password(line_length, pwd_length)
            large_test_1.append(line)
        test_cases.append("\n".join(large_test_1))
        
        # Large test with n = 10000
        large_test_2 = ["10000"]
        for _ in range(10000):
            line_length = random.randint(20, 50)  # Shorter lines to keep file size reasonable
            pwd_length = random.randint(5, 10)
            line = self.generate_line_with_multiple_passwords(line_length, min_length=3, max_length=pwd_length, count=2)
            large_test_2.append(line)
        test_cases.append("\n".join(large_test_2))
        
        # ===== Subtask 2: 10^4 < n <= 1.5*10^4 (30% of tests) =====
        
        # Test with n = 12000
        large_test_3 = ["12000"]
        for _ in range(12000):
            line_length = random.randint(15, 40)  # Keep lines shorter for larger n
            pwd_length = random.randint(5, 10)
            line = self.generate_line_with_password(line_length, pwd_length)
            large_test_3.append(line)
        test_cases.append("\n".join(large_test_3))
        
        # Test with n = 15000
        large_test_4 = ["15000"]
        for _ in range(15000):
            line_length = random.randint(10, 30)
            pwd_length = random.randint(3, 8)
            line = self.generate_line_with_password(line_length, pwd_length)
            large_test_4.append(line)
        test_cases.append("\n".join(large_test_4))
        
        # ===== Subtask 3: 1.5*10^4 < n <= 2*10^4 (20% of tests) =====
        
        # Test with n = 17500
        large_test_5 = ["17500"]
        for _ in range(17500):
            line_length = random.randint(10, 25)
            pwd_length = random.randint(3, 7)
            line = self.generate_line_with_password(line_length, pwd_length)
            large_test_5.append(line)
        test_cases.append("\n".join(large_test_5))
        
        # Test with n = 20000 (maximum)
        large_test_6 = ["20000"]
        for _ in range(20000):
            line_length = random.randint(5, 20)  # Smallest lines for largest n
            pwd_length = random.randint(2, 5)
            line = self.generate_line_with_password(line_length, pwd_length)
            large_test_6.append(line)
        test_cases.append("\n".join(large_test_6))
        
        # ===== Additional Test Cases =====
        
        # Case with max line length (256)
        max_line_test = ["10"]
        for _ in range(10):
            pwd_length = random.randint(20, 50)
            line = self.generate_line_with_password(256, pwd_length)
            max_line_test.append(line)
        test_cases.append("\n".join(max_line_test))
        
        # Case with special characters
        special_char_test = ["5"]
        for _ in range(5):
            line = "".join(random.choice(string.punctuation) for _ in range(30))
            special_char_test.append(line)
        test_cases.append("\n".join(special_char_test))
        
        # Case with long passwords at the end
        long_pwd_test = ["5"]
        for _ in range(5):
            line = self.generate_line_with_multiple_passwords(100, min_length=10, max_length=20, count=3)
            long_pwd_test.append(line)
        test_cases.append("\n".join(long_pwd_test))
        
        # Case with many spaces
        space_test = ["5"]
        for _ in range(5):
            spaces = "".join([" " for _ in range(random.randint(10, 30))])
            pwd = self.generate_random_string(random.randint(5, 15), with_spaces=False, with_duplicates=False)
            more_spaces = "".join([" " for _ in range(random.randint(10, 30))])
            line = spaces + pwd + more_spaces
            space_test.append(line)
        test_cases.append("\n".join(space_test))
        
        # Malicious case: Worst-case for brute force algorithm (many potential passwords)
        malicious_test = ["20"]
        for i in range(20):
            # Create a string with many potential passwords of increasing length
            line = ""
            for j in range(1, 10):  # Create passwords of length 1 to 9
                pwd = self.generate_random_string(j, with_spaces=False, with_duplicates=False)
                line += pwd + " "
            # Add longest password at end
            line += self.generate_random_string(10, with_spaces=False, with_duplicates=False)
            malicious_test.append(line)
        test_cases.append("\n".join(malicious_test))
        
        # Mix of various test patterns
        mixed_test = ["30"]
        for i in range(30):
            if i % 5 == 0:
                # Line with many spaces
                line = " ".join(self.generate_random_string(1, with_spaces=False) for _ in range(20))
            elif i % 5 == 1:
                # Line with long unique substring
                line = self.generate_random_string(30, with_spaces=True) + self.generate_random_string(20, with_spaces=False, with_duplicates=False)
            elif i % 5 == 2:
                # Line with multiple potential passwords
                line = self.generate_line_with_multiple_passwords(50, count=4)
            elif i % 5 == 3:
                # Line with no spaces
                line = self.generate_random_string(40, with_spaces=False)
            else:
                # Normal line
                line = self.generate_line_with_password(40, 10)
            mixed_test.append(line)
        test_cases.append("\n".join(mixed_test))
        
        # Ensure we have more than 30 test cases
        return test_cases