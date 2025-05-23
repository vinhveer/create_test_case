from ...generate_test import GenerateTest
import random

class RobotGiftsTestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_n", type=int, default=1, help="Min number of rows")
        parser.add_argument("--max_n", type=int, default=1000, help="Max number of rows")
        parser.add_argument("--min_m", type=int, default=1, help="Min number of columns")
        parser.add_argument("--max_m", type=int, default=1000, help="Max number of columns")
        parser.add_argument("--min_val", type=int, default=1, help="Min gift value")
        parser.add_argument("--max_val", type=int, default=100000, help="Max gift value")
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

    def generate_grid(self, n, m, min_val, max_val, pattern=None):
        """Generate a grid according to the specified pattern"""
        grid = []
        
        # Random pattern (default)
        if pattern is None or pattern == "random":
            for i in range(n):
                row = [random.randint(min_val, max_val) for _ in range(m)]
                grid.append(row)
        
        # Grid with high values in the middle row
        elif pattern == "middle_path":
            middle = n // 2
            for i in range(n):
                if i == middle:
                    row = [random.randint(max_val // 2, max_val) for _ in range(m)]
                else:
                    row = [random.randint(min_val, max_val // 10) for _ in range(m)]
                grid.append(row)
        
        # Grid with high values in diagonal
        elif pattern == "diagonal":
            for i in range(n):
                row = []
                for j in range(m):
                    if abs(i - j % n) <= 1 or abs(i - (m - j - 1) % n) <= 1:
                        row.append(random.randint(max_val // 2, max_val))
                    else:
                        row.append(random.randint(min_val, max_val // 10))
                grid.append(row)
        
        # Grid with all values at max
        elif pattern == "all_max":
            for i in range(n):
                row = [max_val for _ in range(m)]
                grid.append(row)
        
        # Grid with all values at min
        elif pattern == "all_min":
            for i in range(n):
                row = [min_val for _ in range(m)]
                grid.append(row)
        
        # Grid with zigzag pattern of high values
        elif pattern == "zigzag":
            row_idx = 0
            direction = 1  # 1: down, -1: up
            for j in range(m):
                for i in range(n):
                    if i == row_idx:
                        grid[i][j] = random.randint(max_val // 2, max_val)
                    else:
                        grid[i][j] = random.randint(min_val, max_val // 10)
                
                row_idx += direction
                if row_idx == n - 1 or row_idx == 0:
                    direction *= -1
                    
        return grid

    def format_grid(self, grid):
        """Format grid as string"""
        return '\n'.join(' '.join(str(cell) for cell in row) for row in grid)

    def generate_inputs(self, params):
        test_cases = []
        min_n = getattr(params, "min_n", 1)
        max_n = getattr(params, "max_n", 1000)
        min_m = getattr(params, "min_m", 1)
        max_m = getattr(params, "max_m", 1000)
        min_val = getattr(params, "min_val", 1)
        max_val = getattr(params, "max_val", 100000)
        
        # Sample test case from problem statement
        test_cases.append("3 5\n7 3 8 1 5\n8 8 3 14 1\n6 15 19 1 1")
        
        # ===== Subtask 1: 1 ≤ n, m ≤ 500 (50% of tests) =====
        
        # Edge case: n = m = 1
        test_cases.append(f"1 1\n{random.randint(min_val, max_val)}")
        
        # Edge case: n = 1, m > 1
        n, m = 1, 10
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Edge case: n > 1, m = 1
        n, m = 10, 1
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Small test cases
        for size in [5, 10, 20]:
            n = m = size
            grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
            test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Medium test cases
        for size in [50, 100]:
            n = m = size
            grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
            test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Large test case for subtask 1
        n = m = 500
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Special pattern test cases (small size for readability)
        n, m = 20, 30
        
        # Middle path pattern
        grid = []
        middle = n // 2
        for i in range(n):
            row = []
            for j in range(m):
                if i == middle:
                    row.append(random.randint(max_val // 2, max_val))
                else:
                    row.append(random.randint(min_val, max_val // 10))
            grid.append(row)
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Diagonal pattern
        grid = []
        for i in range(n):
            row = []
            for j in range(m):
                if i == (j % n) or i == ((m - j - 1) % n):
                    row.append(random.randint(max_val // 2, max_val))
                else:
                    row.append(random.randint(min_val, max_val // 10))
            grid.append(row)
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Zigzag pattern
        grid = [[0 for _ in range(m)] for _ in range(n)]
        row_idx = 0
        direction = 1  # 1: down, -1: up
        for j in range(m):
            for i in range(n):
                if i == row_idx:
                    grid[i][j] = random.randint(max_val // 2, max_val)
                else:
                    grid[i][j] = random.randint(min_val, max_val // 10)
            
            row_idx += direction
            if row_idx == n - 1 or row_idx == 0:
                direction *= -1
        
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # ===== Subtask 2: 500 < n, m ≤ 800 (30% of tests) =====
        
        # Edge case: n, m just above 500
        n = m = 501
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Medium test case for subtask 2
        n = m = 650
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Large test case for subtask 2
        n = m = 800
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # ===== Subtask 3: 800 < n, m ≤ 1000 (20% of tests) =====
        
        # Edge case: n, m just above 800
        n = m = 801
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Medium test case for subtask 3
        n = m = 900
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Large test case for subtask 3 (maximum allowed)
        n = m = 1000
        grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # ===== Additional special test cases =====
        
        # Non-square grid cases
        for (n, m) in [(10, 100), (100, 10), (50, 200), (200, 50)]:
            grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
            test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Grid with all values at max
        n, m = 50, 50
        grid = [[max_val for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Grid with all values at min
        n, m = 50, 50
        grid = [[min_val for _ in range(m)] for _ in range(n)]
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Grid with alternating max/min values
        n, m = 50, 50
        grid = []
        for i in range(n):
            row = []
            for j in range(m):
                if (i + j) % 2 == 0:
                    row.append(max_val)
                else:
                    row.append(min_val)
            grid.append(row)
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Grid with high values in corners
        n, m = 50, 50
        grid = [[random.randint(min_val, max_val // 10) for _ in range(m)] for _ in range(n)]
        grid[0][0] = max_val
        grid[0][m-1] = max_val
        grid[n-1][0] = max_val
        grid[n-1][m-1] = max_val
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Grid with high values in border
        n, m = 50, 50
        grid = []
        for i in range(n):
            row = []
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    row.append(random.randint(max_val // 2, max_val))
                else:
                    row.append(random.randint(min_val, max_val // 10))
            grid.append(row)
        test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Random test cases with varying sizes
        for _ in range(5):
            n = random.randint(100, 300)
            m = random.randint(100, 300)
            grid = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
            test_cases.append(f"{n} {m}\n" + self.format_grid(grid))
        
        # Make sure we have at least 30 test cases
        return test_cases