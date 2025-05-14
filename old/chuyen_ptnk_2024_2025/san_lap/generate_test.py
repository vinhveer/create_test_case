import argparse
import os
import random
import subprocess
import tempfile
import shutil

def compile_cpp(source_path, output_path):
    """Compile the C++ source file to an executable."""
    cmd = ["g++", "-std=c++17", source_path, "-O2", "-o", output_path]
    subprocess.check_call(cmd)

def run_executable(exe_path, input_data):
    """Run the executable with given input and return its output."""
    process = subprocess.Popen([exe_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)
    if process.returncode != 0:
        raise RuntimeError(f"Executable error {process.returncode}: {stderr}")
    return stdout

def generate_one_island_board(m, n):
    """
    Generate a board of size m x n that has exactly one island.
    The simplest way is to fill the entire grid with 1 (all land).
    This guarantees a single island.
    """
    board = []
    for _ in range(m):
        row = [1]*n
        board.append(row)
    return board

def generate_random_board(m, n):
    """
    Generate a random board of size m x n with 0 and 1.
    There's no guarantee on how many islands.
    """
    board = []
    for _ in range(m):
        row = [random.randint(0,1) for __ in range(n)]
        board.append(row)
    return board

def board_to_str(board):
    """
    Convert the 2D board array to the input format:
      m n
      row1
      row2
      ...
    """
    m = len(board)
    n = len(board[0]) if m > 0 else 0
    lines = [f"{m} {n}"]
    for r in board:
        lines.append(" ".join(map(str, r)))
    return "\n".join(lines)

def generate_input(i, total_cases):
    """
    Generate input for the Islands problem according to the constraints:
      - 20% of tests: exactly one island
      - 40% of tests: dimensions <= 50
      - 40% of tests: no further limit
    """
    ratio = i / float(total_cases+1)
    if ratio <= 0.2:
        # 20% of tests: exactly one island
        # Small dimension to keep it manageable
        m = random.randint(2, 20)
        n = random.randint(2, 20)
        board = generate_one_island_board(m, n)
    elif ratio <= 0.6:
        # 40% of tests: dimension <= 50
        m = random.randint(2, 50)
        n = random.randint(2, 50)
        board = generate_random_board(m, n)
    else:
        # 40% of tests: no limit (up to 1000)
        m = random.randint(2, 1000)
        n = random.randint(2, 1000)
        board = generate_random_board(m, n)

    return board_to_str(board)

def main():
    parser = argparse.ArgumentParser(description="Generate test cases for the Islands problem using a C++ oracle.")
    parser.add_argument("solution", help="Path to C++ solution file (.cpp)")
    parser.add_argument("--cases", type=int, default=10, help="Number of test cases to generate")
    parser.add_argument("--output-dir", default="islands_tests", help="Directory to store .in and .out files")
    parser.add_argument("--compress", action="store_true", help="Compress output directory into a zip file")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    exe_path = os.path.join(tempfile.gettempdir(), "islands_oracle_exec")

    print(f"Compiling {args.solution}...")
    compile_cpp(args.solution, exe_path)
    print("Compilation finished.")

    for i in range(1, args.cases + 1):
        input_data = generate_input(i, args.cases)
        output_data = run_executable(exe_path, input_data)

        in_path = os.path.join(args.output_dir, f"{i}.in")
        out_path = os.path.join(args.output_dir, f"{i}.out")
        with open(in_path, "w") as f_in:
            f_in.write(input_data + "\n")
        with open(out_path, "w") as f_out:
            f_out.write(output_data.strip() + "\n")
        print(f"Generated test {i}: {in_path}, {out_path}")

    if args.compress:
        zip_name = shutil.make_archive(args.output_dir, 'zip', root_dir=args.output_dir)
        print(f"Compressed tests into {zip_name}")

if __name__ == "__main__":
    main()