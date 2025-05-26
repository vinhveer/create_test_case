from ...generate_test import GenerateTest
import random

class MERGETestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min n")
        parser.add_argument("--max_n", type=int, default=100000, help="Max n")
        parser.add_argument("--min_m", type=int, default=1, help="Min m")
        parser.add_argument("--max_m", type=int, default=100000, help="Max m")
        parser.add_argument("--min_val", type=int, default=-1000000000, help="Min value for a, b")
        parser.add_argument("--max_val", type=int, default=1000000000, help="Max value for a, b")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        
        # Calculate how many tests we need for each subtask
        total_tests = 30  # We'll create exactly 30 tests
        subtask1_tests = total_tests // 2  # 50% for subtask 1 (n,m ≤ 5000)
        subtask2_tests = total_tests - subtask1_tests  # 50% for subtask 2 (larger n,m)
        
        # SUBTASK 1: n,m <= 5000 (50% of tests)
        
        # 1. Sample test from problem statement
        test_cases.append("3\n1 4 9\n4\n5 2 4 5")
        subtask1_tests -= 1
        
        # 2. Minimum case: n=1, m=1
        test_cases.append("1\n5\n1\n10")
        subtask1_tests -= 1
        
        # 3. Case where both arrays are already sorted
        n, m = 10, 15
        a = [i for i in range(1, n+1)]
        b = [i for i in range(n, n+m)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 4. Case where a is sorted, b is reverse sorted
        n, m = 10, 15
        a = [i for i in range(1, n+1)]
        b = [m-i for i in range(m)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 5. Case where a is reverse sorted, b is sorted
        n, m = 10, 15
        a = [n-i for i in range(n)]
        b = [i for i in range(1, m+1)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 6. Case where both arrays are reverse sorted
        n, m = 10, 15
        a = [n-i for i in range(n)]
        b = [m-i for i in range(m)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 7. Case with all equal elements
        n, m = 10, 15
        a = [5] * n
        b = [5] * m
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 8. Case where a[max] < b[min], optimal is to take all elements
        n, m = 20, 25
        a = [i for i in range(1, n+1)]
        b = [i+n for i in range(1, m+1)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 9. Case where a[min] > b[max], optimal is to take either all of a or all of b
        n, m = 20, 25
        a = [i+m for i in range(1, n+1)]
        b = [i for i in range(1, m+1)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 10. Case with negative numbers
        n, m = 20, 25
        a = [-50 + i*5 for i in range(n)]
        b = [-20 + i*3 for i in range(m)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 11. Case where only first element of a and last element of b can be used
        n, m = 100, 100
        a = [1] + [1000] * (n-1)
        b = [2000] * (m-1) + [3000]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 12. Edge case: Maximum n,m for subtask 1
        n, m = 5000, 5000
        a = [random.randint(-10000, 10000) for _ in range(n)]
        a.sort()  # Sorted to ensure some valid solution
        b = [random.randint(-5000, 20000) for _ in range(m)]
        b.sort()  # Sorted to ensure some valid solution
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 13. Sawtooth pattern in both arrays
        n, m = 100, 100
        a = []
        for i in range(n):
            if i % 2 == 0:
                a.append(i)
            else:
                a.append(i-2)
        
        b = []
        for i in range(m):
            if i % 2 == 0:
                b.append(i+n)
            else:
                b.append(i+n-2)
        
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 14. Case where the optimal is to take very few elements from a
        n, m = 1000, 1000
        a = [i*10 for i in range(n)]
        # Make b start with a small value to force taking few elements from a
        b = [5] + [1000 + i for i in range(1, m)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # 15. Case where the optimal is to take very few elements from b
        n, m = 1000, 1000
        a = [i for i in range(n)]
        # Make b mostly decreasing with few increasing elements at the end
        b = [1000 - i for i in range(m-5)] + [2000 + i for i in range(5)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask1_tests -= 1
        
        # Generate remaining subtask 1 tests with random data within constraints
        while subtask1_tests > 0:
            n = random.randint(100, 5000)
            m = random.randint(100, 5000)
            
            # Generate arrays with various patterns
            if subtask1_tests % 3 == 0:
                # Mostly sorted with some disruptions
                a = sorted([random.randint(-10000, 10000) for _ in range(n)])
                for i in range(n//10):  # Disrupt 10% of elements
                    idx = random.randint(0, n-1)
                    a[idx] = random.randint(-10000, 10000)
                
                b = sorted([random.randint(-10000, 10000) for _ in range(m)])
                for i in range(m//10):  # Disrupt 10% of elements
                    idx = random.randint(0, m-1)
                    b[idx] = random.randint(-10000, 10000)
            
            elif subtask1_tests % 3 == 1:
                # Plateaus pattern
                a = []
                val = random.randint(-1000, 1000)
                for i in range(n):
                    if i % 10 == 0:
                        val = random.randint(-1000, 1000)
                    a.append(val)
                
                b = []
                val = random.randint(-1000, 1000)
                for i in range(m):
                    if i % 10 == 0:
                        val = random.randint(-1000, 1000)
                    b.append(val)
            
            else:
                # Complete random
                a = [random.randint(-100000, 100000) for _ in range(n)]
                b = [random.randint(-100000, 100000) for _ in range(m)]
            
            test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
            subtask1_tests -= 1
        
        # SUBTASK 2: n,m <= 10^5 (50% of tests)
        
        # 16. Edge case: Maximum n,m for problem
        n, m = 100000, 100000
        # Generate sorted arrays for maximum n,m to avoid TLE in solution checking
        a = []
        val = -1000000000
        step = 2000000000 // n
        for i in range(n):
            a.append(val)
            val += step
        
        b = []
        val = -500000000
        step = 1500000000 // m
        for i in range(m):
            b.append(val)
            val += step
        
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 17. Case with maximum values: extreme ends of the allowed range
        n, m = 50000, 50000
        a = [random.randint(-1000000000, -999000000) for _ in range(n//2)] + [random.randint(999000000, 1000000000) for _ in range(n - n//2)]
        a.sort()  # Sort to ensure some valid solution
        b = [random.randint(-1000000000, -999000000) for _ in range(m//2)] + [random.randint(999000000, 1000000000) for _ in range(m - m//2)]
        b.sort()  # Sort to ensure some valid solution
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 18. Case where optimal is to take only a[1]
        n, m = 20000, 20000
        a = [1] + [i for i in range(1000, 1000 + n - 1)]  # Start with 1, then large values
        b = [2] + [i for i in range(3, 3 + m - 1)]  # Small increasing sequence
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 19. Case where optimal is to take only b[m]
        n, m = 20000, 20000
        a = [i for i in range(n)]  # Increasing sequence
        b = [i for i in range(m-1)] + [m*10]  # End with large value
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 20. Alternating pattern: will challenge the search for left and right boundaries
        n, m = 20000, 20000
        a = []
        for i in range(n):
            if i % 2 == 0:
                a.append(i)
            else:
                a.append(i-2)
        
        b = []
        for i in range(m):
            if i % 2 == 0:
                b.append(i+n)
            else:
                b.append(i+n-2)
        
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 21. Only first few elements of a are in non-decreasing order
        n, m = 30000, 30000
        a = [i for i in range(100)] + [random.randint(-100, 100) for _ in range(n-100)]
        b.sort()  # Ensure b is sorted for a clear pattern
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 22. Only last few elements of b are in non-decreasing order
        n, m = 30000, 30000
        a.sort()  # Ensure a is sorted for a clear pattern
        b = [random.randint(-100, 100) for _ in range(m-100)] + [i for i in range(100)]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 23. Case with very large jumps
        n, m = 40000, 40000
        a = []
        val = -1000000000
        for i in range(n):
            a.append(val)
            val += random.randint(10000, 50000)
        
        b = []
        val = -500000000
        for i in range(m):
            b.append(val)
            val += random.randint(10000, 50000)
        
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # 24. Case with sparse valid elements
        n, m = 50000, 50000
        a = [i if i % 100 == 0 else 1000000000 for i in range(n)]  # Only every 100th element is small
        b = [i if i % 100 == 0 else -1000000000 for i in range(m)]  # Only every 100th element is large
        b.reverse()  # Reverse to challenge the algorithm
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
        subtask2_tests -= 1
        
        # Generate remaining subtask 2 tests with random data within constraints
        while subtask2_tests > 0:
            n = random.randint(5001, 100000)
            m = random.randint(5001, 100000)
            
            # Generate arrays with various patterns
            if subtask2_tests % 3 == 0:
                # Mostly sorted with some disruptions
                a = sorted([random.randint(-1000000000, 1000000000) for _ in range(n)])
                for i in range(n//20):  # Disrupt 5% of elements
                    idx = random.randint(0, n-1)
                    a[idx] = random.randint(-1000000000, 1000000000)
                
                b = sorted([random.randint(-1000000000, 1000000000) for _ in range(m)])
                for i in range(m//20):  # Disrupt 5% of elements
                    idx = random.randint(0, m-1)
                    b[idx] = random.randint(-1000000000, 1000000000)
            
            elif subtask2_tests % 3 == 1:
                # Plateaus pattern
                a = []
                val = random.randint(-1000000000, 1000000000)
                for i in range(n):
                    if i % 1000 == 0:
                        val = random.randint(-1000000000, 1000000000)
                    a.append(val)
                
                b = []
                val = random.randint(-1000000000, 1000000000)
                for i in range(m):
                    if i % 1000 == 0:
                        val = random.randint(-1000000000, 1000000000)
                    b.append(val)
            
            else:
                # Complete random
                a = [random.randint(-1000000000, 1000000000) for _ in range(n)]
                b = [random.randint(-1000000000, 1000000000) for _ in range(m)]
            
            test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{m}\n{' '.join(map(str, b))}")
            subtask2_tests -= 1
        
        return test_cases