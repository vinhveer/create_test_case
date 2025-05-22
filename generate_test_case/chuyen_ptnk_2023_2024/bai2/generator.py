from ...generate_test import GenerateTest
import random
import math

class SODBTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_T", type=int, default=1, help="Minimum number of test cases")
        parser.add_argument("--max_T", type=int, default=1000000, help="Maximum number of test cases")
        parser.add_argument("--min_val", type=int, default=1, help="Minimum value for L")
        parser.add_argument("--max_val", type=int, default=1000000, help="Maximum value for R")
        parser.add_argument("--small_tests", action="store_true", help="Generate small test cases (R<=1000)")
        parser.add_argument("--medium_tests", action="store_true", help="Generate medium test cases (R<=100000)")
        parser.add_argument("--large_tests", action="store_true", help="Generate large test cases (R<=1000000)")
        return parser

    def is_prime(self, n):
        """Check if a number is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def get_special_numbers(self, limit):
        """Generate list of special numbers up to limit"""
        special_numbers = []
        
        # Case 1: p³ (cube of a prime)
        p = 2
        while p**3 <= limit:
            if self.is_prime(p):
                special_numbers.append(p**3)
            p += 1
        
        # Case 2: p×q (product of two distinct primes)
        primes = []
        for i in range(2, int(math.sqrt(limit)) + 1):
            if self.is_prime(i):
                primes.append(i)
        
        for i in range(len(primes)):
            p = primes[i]
            for j in range(i, len(primes)):
                q = primes[j]
                if p != q and p * q <= limit:
                    special_numbers.append(p * q)
        
        return sorted(special_numbers)

    def generate_inputs(self, params):
        test_cases = []
        special_numbers = self.get_special_numbers(getattr(params, "max_val", 1000000))
        
        # 1. Example cases from the problem statement
        test_cases.append("3\n6 9\n10 15\n20 33")
        
        # 2. Edge case - smallest possible values
        test_cases.append("1\n1 10")
        
        # 3. Edge case - L = R for special number
        test_cases.append("1\n6 6")
        
        # 4. Edge case - L = R for non-special number
        test_cases.append("1\n7 7")
        
        # 5. Range with no special numbers
        test_cases.append("1\n3 5")
        
        # 6. Larger ranges with different densities of special numbers
        if getattr(params, "small_tests", True) or len(test_cases) < 10:
            # Small tests (R <= 1000)
            T_small = min(30, getattr(params, "max_T", 1000000))
            small_tests = []
            
            for _ in range(T_small):
                R = random.randint(10, 1000)
                L = random.randint(1, R)
                small_tests.append(f"{L} {R}")
            
            test_cases.append(f"{T_small}\n" + "\n".join(small_tests))
        
    
        return test_cases