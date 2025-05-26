from ...generate_test import GenerateTest
import random
import string

class PASSWORDTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min number of lines")
        parser.add_argument("--max_n", type=int, default=20000, help="Max number of lines")
        parser.add_argument("--min_len", type=int, default=1, help="Min length of each line")
        parser.add_argument("--max_len", type=int, default=256, help="Max length of each line")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        
        # Common characters to use in test generation
        all_chars = string.ascii_letters + string.digits + string.punctuation + " "
        letters_only = string.ascii_letters
        alphanumeric = string.ascii_letters + string.digits
        special_chars = string.punctuation
        
        # 1. Sample from the problem statement
        test_cases.append("3\nGood morning!\nHow are you?\nHave a nice day!")
        
        # 2. Minimum valid case (n=1, short string)
        test_cases.append("1\nHello")
        
        # 3. Case with multiple candidates of the same max length
        test_cases.append("1\nabcde uvwxy 12345")
        
        # 4. Edge case: Maximum password length equals line length
        unique_letters = "abcdefghijklmnopqrstuvwxyz"
        test_cases.append(f"1\n{unique_letters}")
        
        # PERFORMANCE STRESS TESTS - designed to make brute force TLE
        
        # 5. Test with many nearly maximum-length lines
        # This will force the brute force to check O(n²) substrings for each line
        n = 100
        lines = []
        for _ in range(n):
            # Create string with length 250-256 with many unique character sequences
            line_length = random.randint(250, 256)
            
            # Generate a line with many different characters to create many candidate passwords
            line = ""
            for i in range(line_length):
                # Every few characters, start a new potential password segment
                if i % 5 == 0:
                    line += random.choice(alphanumeric)
                else:
                    # Mix in some repeats and spaces to create boundaries
                    if random.random() < 0.2:
                        line += " "
                    else:
                        line += random.choice(alphanumeric + special_chars)
            
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 6. Worst case for brute force: Almost all unique characters, very long lines
        n = 50
        lines = []
        for _ in range(n):
            line_length = 256  # Maximum length
            
            # Create a string with many unique character sequences separated by occasional spaces
            chars = list(alphanumeric + special_chars)
            random.shuffle(chars)
            
            line = ""
            for i in range(line_length):
                if i % 20 == 19:  # Add occasional space
                    line += " "
                else:
                    if chars:
                        line += chars.pop()  # Use each character only once when possible
                    else:
                        # If we run out, use random characters
                        line += random.choice(alphanumeric + special_chars)
            
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 7. Test with maximum n and medium-length strings (balancing total size)
        n = 20000
        lines = []
        for _ in range(n):
            line_length = random.randint(30, 50)  # Medium-length lines
            
            # Create strings with multiple candidate passwords
            chars = list(alphanumeric + special_chars)
            random.shuffle(chars)
            
            # Create a pattern with potential password candidates
            segments = []
            remaining_length = line_length
            
            while remaining_length > 0:
                # Create segments of 5-10 unique characters
                segment_length = min(remaining_length, random.randint(5, 10))
                segment = ''.join(random.sample(alphanumeric, segment_length))
                segments.append(segment)
                
                remaining_length -= segment_length
                
                # Add a space between segments if there's room
                if remaining_length > 0:
                    segments.append(" ")
                    remaining_length -= 1
            
            line = ''.join(segments)
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 8. Test with extremely pathological case for brute force
        # Create maximum length strings with almost all unique characters
        n = 200  # 200 lines of max length should be enough to make brute force time out
        lines = []
        for _ in range(n):
            # Create a base of unique characters
            unique_chars = list(set(alphanumeric + special_chars.replace(' ', '')))
            random.shuffle(unique_chars)
            
            # Create a string where first 80% are unique characters
            unique_segment_length = min(200, len(unique_chars))
            unique_segment = ''.join(unique_chars[:unique_segment_length])
            
            # Fill the rest with random characters and occasional spaces
            remaining_length = 256 - unique_segment_length
            filler = ''.join(random.choice(alphanumeric + " ") for _ in range(remaining_length))
            
            line = unique_segment + filler
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 9. Test specifically targeting the sliding window efficiency
        # Create strings with a maximum valid substring near the end
        n = 1000
        lines = []
        for _ in range(n):
            line_length = 256
            
            # First part is full of duplicates and spaces
            first_part_length = 200
            first_part = ''.join(random.choice("abcde ") for _ in range(first_part_length))
            
            # Last part has a long sequence of unique characters
            last_part_length = line_length - first_part_length
            unique_chars = list(set(alphanumeric + special_chars.replace(' ', '')))
            random.shuffle(unique_chars)
            last_part = ''.join(unique_chars[:last_part_length])
            
            line = first_part + last_part
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 10. Test with a mixture of very long and very short lines
        n = 10000
        lines = []
        for i in range(n):
            if i % 10 == 0:  # Every 10th line is very long
                line_length = 256
                # Create a string with many unique character segments
                segments = []
                remaining_length = line_length
                
                while remaining_length > 0:
                    # Create segments of 10-20 unique characters
                    segment_length = min(remaining_length, random.randint(10, 20))
                    segment = ''.join(random.sample(alphanumeric, segment_length))
                    segments.append(segment)
                    
                    remaining_length -= segment_length
                    
                    # Add a space between segments if there's room
                    if remaining_length > 0:
                        segments.append(" ")
                        remaining_length -= 1
                
                line = ''.join(segments)
            else:  # Other lines are short
                line_length = random.randint(5, 20)
                line = ''.join(random.choice(all_chars) for _ in range(line_length))
            
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 11. Test with maximum n and long strings
        # This is designed to maximize the total workload
        n = 5000  # Smaller n to keep total size reasonable
        lines = []
        for _ in range(n):
            line_length = random.randint(200, 256)  # Long lines
            
            # Create strings with a mixture of unique segments and spaces
            segments = []
            remaining_length = line_length
            
            while remaining_length > 0:
                # Create segments of varying length with unique characters
                segment_length = min(remaining_length, random.randint(5, 30))
                segment = ''.join(random.sample(alphanumeric + special_chars, segment_length))
                segments.append(segment)
                
                remaining_length -= segment_length
                
                # Add a space between segments if there's room
                if remaining_length > 0:
                    segments.append(" ")
                    remaining_length -= 1
            
            line = ''.join(segments)
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 12. Ultra-pathological case: maximize substring checks
        # For a length-n string, there are n(n+1)/2 possible substrings
        # Create strings where many of these substrings have unique characters
        n = 100
        lines = []
        for _ in range(n):
            line_length = 256
            
            # Use characters with high probability of being unique when combined
            available_chars = list(alphanumeric + special_chars.replace(' ', ''))
            random.shuffle(available_chars)
            
            # Try to use as many unique characters as possible
            line = ''.join(available_chars[:line_length])
            
            # Insert a few spaces to create challenging boundaries
            for _ in range(5):
                pos = random.randint(0, line_length - 1)
                line = line[:pos] + ' ' + line[pos+1:]
            
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 13-20. More challenging tests with decreasing string length
        for length_factor in range(8, 0, -1):
            n = 1000
            max_str_length = 30 * length_factor
            
            lines = []
            for _ in range(n):
                line_length = random.randint(max_str_length - 10, max_str_length)
                
                # Create a string with multiple potential password candidates
                line = ""
                pos = 0
                
                while pos < line_length:
                    # Add a segment of unique characters
                    segment_length = min(line_length - pos, random.randint(3, 15))
                    segment = ''.join(random.sample(alphanumeric + special_chars, segment_length))
                    line += segment
                    pos += segment_length
                    
                    # Add a space if there's room
                    if pos < line_length:
                        line += " "
                        pos += 1
                
                lines.append(line)
            
            test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 21-30. Tests with varying n values to cover all subtasks
        for n_factor in range(10):
            # Calculate n to cover all subtasks
            if n_factor < 5:  # First 5 tests in subtask 1
                n = 1000 + 1800 * n_factor  # 1000 to 10000
            elif n_factor < 8:  # Next 3 tests in subtask 2
                n = 10001 + 1666 * (n_factor - 5)  # 10001 to 15000
            else:  # Last 2 tests in subtask 3
                n = 15001 + 2500 * (n_factor - 8)  # 15001 to 20000
            
            # Keep string length reasonable to fit file size limits
            max_str_length = 50 - (n // 1000)  # Reduce string length as n increases
            
            lines = []
            for _ in range(n):
                line_length = random.randint(10, max_str_length)
                
                # Create a string with challenging password patterns
                line = ""
                pos = 0
                
                while pos < line_length:
                    if random.random() < 0.7:  # 70% chance for a potential password segment
                        segment_length = min(line_length - pos, random.randint(3, 10))
                        segment = ''.join(random.sample(alphanumeric, segment_length))
                        line += segment
                        pos += segment_length
                    else:  # 30% chance for a non-password segment (duplicates or spaces)
                        segment_length = min(line_length - pos, random.randint(1, 5))
                        segment = ''.join(random.choice(" " + alphanumeric[:5]) for _ in range(segment_length))
                        line += segment
                        pos += segment_length
                
                lines.append(line)
            
            test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 31. Extreme case: Maximum n with each line containing many unique substrings
        n = 20000
        lines = []
        for _ in range(n):
            line_length = random.randint(20, 30)  # Keep length moderate to fit file size
            
            # Create a line with many potential password candidates
            chars = list(alphanumeric)
            random.shuffle(chars)
            
            # Use as many unique characters as possible
            line = ''.join(chars[:line_length])
            
            # Insert a couple of spaces to create boundaries
            for _ in range(2):
                if line_length > 2:  # Ensure we have enough characters
                    pos = random.randint(0, line_length - 1)
                    line = line[:pos] + ' ' + line[pos+1:]
            
            lines.append(line)
        test_cases.append(f"{n}\n" + "\n".join(lines))
        
        # 32-35. Final stress tests with varying patterns
        # Fixed the pattern functions to properly create strings
        pattern_functions = [
            # Pattern 1: Many small unique segments
            lambda: ''.join(''.join(random.sample(alphanumeric, 3)) + ' ' for _ in range(10)),
            
            # Pattern 2: A few larger unique segments
            lambda: ' '.join(''.join(random.sample(alphanumeric, 15)) for _ in range(3)),
            
            # Pattern 3: Alternating unique and duplicate segments
            lambda: ''.join(''.join(random.sample(alphanumeric, 5)) + ' ' + 'a' * 5 + ' ' for _ in range(5)),
            
            # Pattern 4: One long unique segment with spaces on both sides
            lambda: ' ' * 10 + ''.join(random.sample(alphanumeric + special_chars, 30)) + ' ' * 10
        ]
        
        for pattern_idx in range(4):
            pattern_fn = pattern_functions[pattern_idx]
            n = 5000
            lines = [pattern_fn() for _ in range(n)]
            test_cases.append(f"{n}\n" + "\n".join(lines))
        
        return test_cases