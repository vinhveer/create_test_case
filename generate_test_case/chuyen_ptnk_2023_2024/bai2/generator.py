from ...generate_test import GenerateTest
import random

class CAKETestGenerator(GenerateTest):
    def get_argument_parser(self):
        parser = super().get_argument_parser()
        parser.add_argument("--min_m", type=int, default=1, help="Min rows")
        parser.add_argument("--max_m", type=int, default=100000, help="Max rows")
        parser.add_argument("--min_n", type=int, default=1, help="Min columns")
        parser.add_argument("--max_n", type=int, default=100000, help="Max columns")
        parser.add_argument("--min_k", type=int, default=1, help="Min cherries per quadrant")
        parser.add_argument("--max_k", type=int, default=50000, help="Max cherries per quadrant")
        return parser

    def generate_inputs(self, params):
        test_cases = []
        
        # Calculate test case distribution according to subtasks
        subtask1_count = 9  # 30% with K=1
        subtask2_count = 9  # 30% with N,M≤4000
        subtask3_count = 12  # 40% with general constraints
        
        # Faster helper function to generate cherries
        def generate_cherries_for_quadrants(m, n, k, h_cut, v_cut):
            cherries = []
            
            # Efficiently generate coordinates for each quadrant
            quadrants = [
                # (row_min, row_max, col_min, col_max)
                (1, h_cut, 1, v_cut),           # top-left
                (1, h_cut, v_cut + 1, n),       # top-right
                (h_cut + 1, m, 1, v_cut),       # bottom-left
                (h_cut + 1, m, v_cut + 1, n)    # bottom-right
            ]
            
            for quadrant in quadrants:
                row_min, row_max, col_min, col_max = quadrant
                
                # For each quadrant, generate k unique positions
                positions = set()
                row_range = row_max - row_min + 1
                col_range = col_max - col_min + 1
                
                # If there's not enough space in the quadrant for k cherries
                if row_range * col_range < k:
                    # Extend the range slightly if possible
                    row_max = min(m, row_max + 1)
                    col_max = min(n, col_max + 1)
                    row_range = row_max - row_min + 1
                    col_range = col_max - col_min + 1
                
                # If we still don't have enough space, just do our best
                max_possible = min(k, row_range * col_range)
                
                # For small k, we can use random generation
                if max_possible <= 1000:
                    while len(positions) < max_possible:
                        x = random.randint(row_min, row_max)
                        y = random.randint(col_min, col_max)
                        positions.add((x, y))
                else:
                    # For large k, use systematic generation to avoid slow random checks
                    i = 0
                    while len(positions) < max_possible and i < row_range * col_range:
                        row = row_min + (i // col_range)
                        col = col_min + (i % col_range)
                        positions.add((row, col))
                        i += 1
                
                cherries.extend(positions)
            
            return cherries
        
        # Convert generated cake to test case string
        def cake_to_test_case(m, n, k, cherries):
            cherries = cherries[:4*k]  # Ensure we have exactly 4*k cherries
            test_case = f"{m} {n} {k}\n"
            for x, y in cherries:
                test_case += f"{x} {y}\n"
            return test_case.strip()
        
        # SUBTASK 1: K=1 (30% of test cases)
        
        # 1. Sample test case from problem
        test_cases.append("3 4 1\n2 2\n3 2\n1 4\n3 4")
        subtask1_count -= 1
        
        # 2. Edge case: Minimum grid size (2x2) with K=1
        m, n, k = 2, 2, 1
        cherries = [(1, 1), (1, 2), (2, 1), (2, 2)]
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask1_count -= 1
        
        # 3. Edge case: Larger grid with K=1, one valid cut
        m, n, k = 10, 10, 1
        h_cut, v_cut = 5, 5
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask1_count -= 1
        
        # 4. Special case: Two valid cuts with K=1
        m, n, k = 10, 10, 1
        # First set of cherries for cut at (5,5)
        cherries1 = [(2, 3), (3, 7), (7, 3), (7, 7)]
        # Additional cherries for cut at (6,6)
        cherries2 = [(2, 3), (3, 7), (7, 3), (7, 7)]
        test_cases.append(cake_to_test_case(m, n, k, cherries1))
        subtask1_count -= 1
        
        # 5. Special case: Cherries on the boundary
        m, n, k = 8, 8, 1
        cherries = [(1, 4), (4, 1), (8, 4), (4, 8)]
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask1_count -= 1
        
        # Generate remaining subtask 1 tests
        grid_sizes = [(5, 5), (7, 9), (20, 15), (100, 100)]
        for i in range(subtask1_count):
            m, n = grid_sizes[i % len(grid_sizes)]
            k = 1
            h_cut = random.randint(1, m-1)
            v_cut = random.randint(1, n-1)
            cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
            test_cases.append(cake_to_test_case(m, n, k, cherries))
        
        # SUBTASK 2: N,M≤4000 (30% of test cases)
        
        # 6. Medium grid with small K
        m, n, k = 1000, 1000, 5
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask2_count -= 1
        
        # 7. Medium grid with medium K
        m, n, k = 2000, 2000, 50
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask2_count -= 1
        
        # 8. Maximum size for subtask 2 with small K
        m, n, k = 4000, 4000, 10
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask2_count -= 1
        
        # Generate remaining subtask 2 tests
        grid_sizes = [(500, 500), (1000, 1000), (2000, 2000), (3000, 3000), (4000, 3000), (3000, 4000)]
        k_values = [3, 10, 20, 30, 100, 200]
        
        for i in range(subtask2_count):
            m, n = grid_sizes[i % len(grid_sizes)]
            k = k_values[i % len(k_values)]
            h_cut = random.randint(m//4, 3*m//4)
            v_cut = random.randint(n//4, 3*n//4)
            cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
            test_cases.append(cake_to_test_case(m, n, k, cherries))
        
        # SUBTASK 3: General constraints (40% of test cases)
        
        # 9. Large grid with small K
        m, n, k = 50000, 50000, 10
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask3_count -= 1
        
        # 10. Large grid with medium K
        m, n, k = 75000, 75000, 100
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask3_count -= 1
        
        # 11. Maximum grid with small K
        m, n, k = 100000, 100000, 50
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask3_count -= 1
        
        # 12. Smaller grid with large K
        m, n, k = 20000, 20000, 5000
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask3_count -= 1
        
        # 13. Uneven grid dimensions
        m, n, k = 10000, 90000, 100
        h_cut, v_cut = m // 2, n // 2
        cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
        test_cases.append(cake_to_test_case(m, n, k, cherries))
        subtask3_count -= 1
        
        # Generate remaining subtask 3 tests
        grid_sizes = [(30000, 30000), (60000, 60000), (90000, 90000), (100000, 50000), (50000, 100000)]
        k_values = [10, 50, 100, 500, 1000, 2000, 5000]
        
        for i in range(subtask3_count):
            m, n = grid_sizes[i % len(grid_sizes)]
            k = k_values[i % len(k_values)]
            h_cut = random.randint(m//4, 3*m//4)
            v_cut = random.randint(n//4, 3*n//4)
            cherries = generate_cherries_for_quadrants(m, n, k, h_cut, v_cut)
            test_cases.append(cake_to_test_case(m, n, k, cherries))
        
        return test_cases