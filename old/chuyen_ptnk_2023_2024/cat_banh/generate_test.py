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
    process = subprocess.Popen(
        [exe_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_data)
    if process.returncode != 0:
        raise RuntimeError(f"Executable error {process.returncode}: {stderr}")
    return stdout

def generate_input(i, total_cases):
    """
    Generate one test input for the CAKE problem based on constraints:
    - 30% of cases: K = 1
    - 30% of cases: M, N <= 4000
    - 40% of cases: No restrictions
    """
    ratio = i / total_cases
    if ratio <= 0.3:
        # 30% of cases: K = 1
        M = random.randint(1, 100)
        N = random.randint(1, 100)
        K = 1
    elif ratio <= 0.6:
        # 30% of cases: M, N <= 4000
        M = random.randint(1, 4000)
        N = random.randint(1, 4000)
        K = random.randint(1, min(1000, (M * N) // 4))  # Ensure 4*K cherries fit
    else:
        # 40% of cases: No restrictions
        M = random.randint(1, 10000)
        N = random.randint(1, 10000)
        K = random.randint(1, min(10000, (M * N) // 4))  # Ensure 4*K cherries fit

    # Generate cherry positions
    cherries = set()
    while len(cherries) < 4 * K:
        x = random.randint(1, M)
        y = random.randint(1, N)
        cherries.add((x, y))

    cherries_list = "\n".join(f"{x} {y}" for x, y in cherries)
    input_data = f"{M} {N} {K}\n{cherries_list}"
    return input_data

def main():
    parser = argparse.ArgumentParser(
        description="Generate test cases for the CAKE problem using a C++ oracle."
    )
    parser.add_argument("solution", help="Path to C++ solution file (.cpp)")
    parser.add_argument("--cases", type=int, default=10,
                        help="Number of test cases to generate")
    parser.add_argument("--output-dir", default="cake_tests",
                        help="Directory to store .in and .out files")
    parser.add_argument("--compress", action="store_true",
                        help="Compress output directory into a zip file")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    exe_path = os.path.join(tempfile.gettempdir(), "cake_oracle_exec")

    print(f"Compiling {args.solution}...")
    compile_cpp(args.solution, exe_path)
    print("Compilation finished.")

    for i in range(1, args.cases + 1):
        input_data = generate_input(i, args.cases)
        # Ensure newline at end for stdin
        input_data_with_nl = input_data + "\n"
        output_data = run_executable(exe_path, input_data_with_nl)

        in_path = os.path.join(args.output_dir, f"{i}.in")
        out_path = os.path.join(args.output_dir, f"{i}.out")
        with open(in_path, "w") as f_in:
            f_in.write(input_data_with_nl)
        with open(out_path, "w") as f_out:
            f_out.write(output_data.strip() + "\n")

        print(f"Generated test {i}: {in_path}, {out_path}")

    if args.compress:
        zip_name = shutil.make_archive(args.output_dir, 'zip',
                                       root_dir=args.output_dir)
        print(f"Compressed tests into {zip_name}")

if __name__ == "__main__":
    main()