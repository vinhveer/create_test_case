from ...generate_test import GenerateTest
import random

class TuongTuTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=2, help="Min n (1 < n)")
        parser.add_argument("--max_n", type=int, default=50000, help="Max n (n ≤ 5×10^4)")
        parser.add_argument("--min_val", type=int, default=1, help="Min value for elements (1 ≤ ai,bi)")
        parser.add_argument("--max_val", type=int, default=1000000000, help="Max value for elements (ai,bi ≤ 10^9)")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 2)
        max_n = getattr(params, "max_n", 50000)
        min_val = getattr(params, "min_val", 1)
        max_val = getattr(params, "max_val", 1000000000)

        # ======= Subtask 1: Invalid n values (10% of tests) =======
        # Test 1: n = 0 (Invalid)
        test_cases.append("0")

        # Test 2: n = 1 (Invalid)
        test_cases.append("1\n5\n10")

        # Test 3: n > 5×10^4 (Invalid)
        test_cases.append("50001\n" + " ".join(["1"] * 5) + "\n" + " ".join(["1"] * 5))
        
        # Test 4: n = -5 (Invalid)
        test_cases.append("-5")

        # ======= Subtask 2: Valid small cases (n ≤ 10^4) =======
        # Test 5: Minimal valid case (n=2), similar sequences
        test_cases.append("2\n1 2\n3 4")

        # Test 6: Minimal valid case (n=2), not similar (a_i = a_j but b_i ≠ b_j)
        test_cases.append("2\n1 1\n2 3")

        # Test 7: Minimal valid case (n=2), not similar (a_i ≠ a_j but b_i = b_j)
        test_cases.append("2\n1 2\n3 3")

        # Test 8: Sample test case 1 from problem statement
        test_cases.append("5\n1 2 3 1 3\n3 2 1 3 1")

        # Test 9: Sample test case 2 from problem statement
        test_cases.append("5\n1 2 3 1 3\n1 2 3 3 3")

        # Test 10: All elements the same in both sequences
        n = 10
        test_cases.append(f"{n}\n{' '.join(['5'] * n)}\n{' '.join(['10'] * n)}")

        # Test 11: All elements unique in both sequences (similar)
        n = 15
        a = list(range(1, n+1))
        b = list(range(n+1, 2*n+1))
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 12: Complex pattern with repeats (similar)
        n = 20
        a = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 7, 10, 11, 12, 10, 13, 14]
        b = [10, 20, 30, 10, 20, 30, 40, 50, 60, 40, 70, 80, 90, 70, 100, 110, 120, 100, 130, 140]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 13: Complex pattern with repeats (not similar - first condition)
        n = 20
        a = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 7, 10, 11, 12, 10, 13, 14]
        b = [10, 20, 30, 15, 20, 30, 40, 50, 60, 40, 70, 80, 90, 70, 100, 110, 120, 100, 130, 140]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 14: Complex pattern with repeats (not similar - second condition)
        n = 20
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        b = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 10]
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 15: Medium size with large numbers (similar)
        n = 100
        a = []
        b = []
        for i in range(n):
            val_a = random.randint(10**8, 10**9)
            val_b = random.randint(10**8, 10**9)
            if i % 5 == 0 and i > 0:  # Add some repeats
                a.append(a[i-5])
                b.append(b[i-5])
            else:
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 16: Medium size with large numbers (not similar)
        n = 100
        a = []
        b = []
        for i in range(n):
            val_a = random.randint(10**8, 10**9)
            val_b = random.randint(10**8, 10**9)
            if i % 5 == 0 and i > 0:  # Add some repeats that violate similarity
                a.append(a[i-5])
                if i % 10 == 0:  # Violation
                    b.append(val_b)
                else:
                    b.append(b[i-5])
            else:
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 17: Many duplicates (similar)
        n = 500
        a = []
        b = []
        for i in range(n):
            val_a = random.randint(1, 10)  # Limited range to ensure many duplicates
            if val_a in a:
                idx = a.index(val_a)
                a.append(val_a)
                b.append(b[idx])
            else:
                val_b = random.randint(1, 10)
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 18: Many duplicates (not similar - first condition)
        n = 500
        a = []
        b = []
        violation_pos = random.randint(n//2, n-1)
        for i in range(n):
            val_a = random.randint(1, 10)
            if val_a in a:
                idx = a.index(val_a)
                a.append(val_a)
                if i == violation_pos:
                    b.append(random.randint(11, 20))  # Different b for same a
                else:
                    b.append(b[idx])
            else:
                val_b = random.randint(1, 10)
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 19: Many duplicates (not similar - second condition)
        n = 500
        a = []
        b = []
        for i in range(n):
            if i > 0 and i % 10 == 0:
                # Create a violation: different a maps to same b
                prev_b = b[i-1]
                a.append(a[i-1] + 1)  # Different a
                b.append(prev_b)      # Same b
            else:
                val_a = random.randint(100, 200)
                val_b = random.randint(1000, 2000)
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 20: Almost similar (just one violation - first condition)
        n = 1000
        a = list(range(1, n+1))
        b = list(range(1000, 1000+n))
        # Create violation at random position
        violation_pos = random.randint(1, n-1)
        idx = random.randint(0, violation_pos-1)
        a[violation_pos] = a[idx]  # Same a value
        b[violation_pos] = b[violation_pos]  # But different b value
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 21: Almost similar (just one violation - second condition)
        n = 1000
        a = list(range(1, n+1))
        b = list(range(1000, 1000+n))
        # Create violation
        violation_pos = random.randint(1, n-1)
        b[violation_pos] = b[0]  # Same b value for different a values
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 22: Maximum valid n for subtask 2 (n = 10000, similar)
        n = 10000
        a = []
        b = []
        mapping = {}  # Ensure consistent mapping
        for i in range(n):
            val_a = random.randint(1, min(n, 1000))  # Limited range to ensure duplicates
            if val_a in mapping:
                a.append(val_a)
                b.append(mapping[val_a])
            else:
                val_b = random.randint(1, min(n, 1000))
                while val_b in mapping.values():  # Ensure one-to-one mapping
                    val_b = random.randint(1, min(n, 1000))
                mapping[val_a] = val_b
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 23: Maximum valid n for subtask 2 (n = 10000, not similar)
        n = 10000
        a = []
        b = []
        mapping = {}
        violation_count = n // 100  # Add some violations
        violations = set(random.sample(range(n), violation_count))
        for i in range(n):
            val_a = random.randint(1, min(n, 1000))
            if i in violations:
                a.append(val_a)
                b.append(random.randint(1, min(n, 1000)))  # Random mapping for violations
            elif val_a in mapping:
                a.append(val_a)
                b.append(mapping[val_a])
            else:
                val_b = random.randint(1, min(n, 1000))
                while val_b in mapping.values():
                    val_b = random.randint(1, min(n, 1000))
                mapping[val_a] = val_b
                a.append(val_a)
                b.append(val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # ======= Subtask 3: Maximum sized cases (10^4 < n ≤ 5×10^4) =======
        # Test 24: Large n with many unique values (similar)
        n = 20000
        a = []
        b = []
        mapping = {}
        for i in range(n):
            if i < n // 2:
                val_a = i + 1  # Unique values for first half
                a.append(val_a)
                b.append(val_a * 10)  # Simple mapping for similarity
                mapping[val_a] = val_a * 10
            else:
                # Reuse values from first half to create duplicates with consistent mapping
                idx = i % (n // 2)
                a.append(a[idx])
                b.append(b[idx])
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 25: Large n with many unique values (not similar)
        n = 20000
        a = []
        b = []
        for i in range(n):
            if i < n // 2:
                val_a = i + 1
                val_b = (i + 1) * 10
                a.append(val_a)
                b.append(val_b)
            else:
                idx = i % (n // 2)
                a.append(a[idx])
                if i % 100 == 0:  # Occasional violations
                    b.append(b[idx] + 1)  # Different b for same a
                else:
                    b.append(b[idx])
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 26: Maximum n with large values (similar)
        n = 50000
        a = []
        b = []
        mapping = {}
        distinct_values = min(n // 5, 10000)  # Use a subset of distinct values
        
        # Create a mapping for distinct values
        for i in range(distinct_values):
            val_a = random.randint(10**8, 10**9)
            val_b = random.randint(10**8, 10**9)
            mapping[val_a] = val_b
        
        # Generate the sequences using the mapping
        keys = list(mapping.keys())
        for i in range(n):
            key_idx = random.randint(0, len(keys) - 1)
            key = keys[key_idx]
            a.append(key)
            b.append(mapping[key])
            
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 27: Maximum n with large values (not similar)
        n = 50000
        a = []
        b = []
        mapping = {}
        distinct_values = min(n // 5, 10000)
        violation_positions = set(random.sample(range(n), n // 1000))  # Add some violations
        
        # Create a mapping for distinct values
        for i in range(distinct_values):
            val_a = random.randint(10**8, 10**9)
            val_b = random.randint(10**8, 10**9)
            mapping[val_a] = val_b
        
        # Generate the sequences using the mapping, with violations
        keys = list(mapping.keys())
        for i in range(n):
            key_idx = random.randint(0, len(keys) - 1)
            key = keys[key_idx]
            a.append(key)
            if i in violation_positions:
                b.append(random.randint(10**8, 10**9))  # Random non-consistent value
            else:
                b.append(mapping[key])
            
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 28: Edge case - maximum n with all values the same (similar)
        n = 50000
        test_cases.append(f"{n}\n{' '.join(['1000000000'] * n)}\n{' '.join(['1'] * n)}")

        # Test 29: Case designed to challenge hash map implementations
        n = 30000
        a = []
        b = []
        for i in range(n):
            if i < n // 3:
                a.append(i)
                b.append(i * 2)
            else:
                # Create pairs with high hash collision potential
                collision_val_a = 10**9 - (i % 1000)
                collision_val_b = 10**9 - 2 * (i % 1000)
                a.append(collision_val_a)
                b.append(collision_val_b)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 30: Maximum n with alternating patterns (to stress the checking)
        n = 50000
        a = []
        b = []
        pattern_a = [i for i in range(1, 101)]  # 100 values pattern
        pattern_b = [i * 10 for i in range(1, 101)]
        for i in range(n):
            a.append(pattern_a[i % 100])
            b.append(pattern_b[i % 100])
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 31: One element different makes the sequences not similar
        n = 40000
        a = []
        b = []
        mapping = {i: i*10 for i in range(1, 101)}  # Create a mapping
        for i in range(n):
            val_a = i % 100 + 1
            a.append(val_a)
            if i == n - 1:  # Last element violates the mapping
                b.append(mapping[val_a] + 1)
            else:
                b.append(mapping[val_a])
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 32: Special case - almost all duplicates in a, unique in b (not similar)
        n = 45000
        a = [1] * n
        b = list(range(1, n+1))
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 33: Almost n repeating patterns (similar)
        n = 48000
        pattern_len = 6000
        a = []
        b = []
        for i in range(pattern_len):
            val_a = random.randint(1, 10**5)
            val_b = random.randint(1, 10**5)
            a.append(val_a)
            b.append(val_b)
        
        # Repeat the pattern
        repeats = n // pattern_len
        a = a * repeats
        b = b * repeats
        
        # Add remaining elements
        remaining = n - len(a)
        for i in range(remaining):
            a.append(a[i])
            b.append(b[i])
            
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 34: Maximum n, specific adversarial pattern for nested loops (similar)
        n = 50000
        a = []
        b = []
        for i in range(n):
            if i < 5000:  # First 10% are all different
                a.append(i)
                b.append(i * 2)
            else:  # Remaining 90% reference the first 10%
                ref_idx = i % 5000
                a.append(a[ref_idx])
                b.append(b[ref_idx])
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        # Test 35: Maximum n, with maximum values (similar)
        n = 50000
        a = []
        b = []
        for i in range(n):
            if i % 2 == 0:
                a.append(10**9)
                b.append(10**9)
            else:
                a.append(10**9 - 1)
                b.append(10**9 - 1)
        test_cases.append(f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}")

        return test_cases