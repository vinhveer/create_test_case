from ...generate_test import GenerateTest
import random

class EvenSumTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_l", type=int, default=1, help="Min L value")
        parser.add_argument("--max_l", type=int, default=2000000000, help="Max L value")
        parser.add_argument("--min_r", type=int, default=1, help="Min R value")
        parser.add_argument("--max_r", type=int, default=2000000000, help="Max R value")
        parser.add_argument("--small_tests", type=int, default=20, help="Number of small tests (L,R <= 10^4)")
        parser.add_argument("--large_tests", type=int, default=10, help="Number of large tests")
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

    def generate_inputs(self, params):
        test_cases = []
        
        # Sample test cases (provided in problem statement)
        test_cases.append("2 9")  # Sample 1: Sum = 20
        test_cases.append("3 3")  # Sample 2: Sum = 0
        
        # Edge cases with small values
        test_cases.append("1 1")  # No even numbers
        test_cases.append("2 2")  # One even number
        test_cases.append("1 2")  # Range contains one even number at the end
        test_cases.append("2 3")  # Range contains one even number at the start
        
        # Edge cases with L and R having different parity
        test_cases.append("3 5")  # Both L and R are odd, no even at boundaries
        test_cases.append("4 10")  # Both L and R are even, even at both boundaries
        test_cases.append("3 8")   # L is odd, R is even, even at right boundary
        test_cases.append("2 7")   # L is even, R is odd, even at left boundary
        
        # Ranges with consecutive numbers
        test_cases.append("1 10")   # Standard small range
        test_cases.append("999 1001") # Range around 1000
        test_cases.append("9999 10001") # Range around 10^4
        
        # Ranges with only odd numbers
        test_cases.append("3 7") # [3,5,7] - only odd numbers
        test_cases.append("11 15") # [11,13,15] - only odd numbers
        
        # Small consecutive ranges with all possible combinations of L,R parity
        # (odd,odd), (odd,even), (even,odd), (even,even)
        test_cases.append("101 103") # (odd,odd)
        test_cases.append("101 104") # (odd,even)
        test_cases.append("102 103") # (even,odd)
        test_cases.append("102 104") # (even,even)
        
        # Random small tests (L,R <= 10^4)
        for _ in range(5):
            L = random.randint(getattr(params, "min_l", 1), min(getattr(params, "max_l", 2000000000), 10000))
            R = random.randint(L, min(getattr(params, "max_r", 2000000000), 10000))
            test_cases.append(f"{L} {R}")
        
        # Medium range tests (10^4 < L,R <= 10^6)
        for _ in range(5):
            L = random.randint(10001, 1000000)
            R = random.randint(L, 1000000)
            test_cases.append(f"{L} {R}")
        
        # Large range tests (10^6 < L,R <= 2*10^9)
        for _ in range(5):
            L = random.randint(1000001, getattr(params, "max_l", 2000000000))
            R = random.randint(L, getattr(params, "max_r", 2000000000))
            test_cases.append(f"{L} {R}")
        
        # Boundary values and special cases
        max_val = getattr(params, "max_r", 2000000000)
        
        # Maximum range
        test_cases.append(f"1 {max_val}")
        
        # Maximum values
        test_cases.append(f"{max_val-1} {max_val}")
        test_cases.append(f"{max_val} {max_val}")
        
        # Close to maximum values with different parities
        test_cases.append(f"{max_val-1} {max_val-1}") # (odd,odd) if max_val is even, (even,even) if max_val is odd
        test_cases.append(f"{max_val-1} {max_val}")   # (odd,even) if max_val is even, (even,odd) if max_val is odd
        
        # Powers of 10 ranges
        test_cases.append("10 100")
        test_cases.append("100 1000")
        test_cases.append("1000 10000")
        test_cases.append("10000 100000")
        
        # Ranges with specific patterns
        # 1. Range that starts with an odd number and has exactly one even number
        test_cases.append("99 100")
        # 2. Range that ends with an odd number and has exactly one even number
        test_cases.append("100 101")
        # 3. Range with exactly two even numbers
        test_cases.append("99 102")
        
        # Random ranges with various sizes
        sizes = [10, 100, 1000, 10000, 100000, 1000000]
        for size in sizes:
            L = random.randint(1, max_val - size)
            R = L + size
            test_cases.append(f"{L} {R}")
            
        # Edge case: L = R (even)
        test_cases.append("100 100")  # Sum = 100
        
        # Edge case: L = R (odd)
        test_cases.append("101 101")  # Sum = 0
        
        # Edge case: Single even number between odd bounds
        test_cases.append("9 11")  # Only 10 is even
        
        # Edge case: Two consecutive even numbers
        test_cases.append("8 10")  # 8 and 10 only
        
        return test_cases