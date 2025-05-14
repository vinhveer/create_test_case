import argparse
import os
import random
import subprocess
import tempfile
import shutil

def compile_cpp(source_path, output_path):
    cmd = ["g++", "-std=c++17", source_path, "-O2", "-o", output_path]
    subprocess.check_call(cmd)

def run_executable(exe_path, input_data):
    process = subprocess.Popen([exe_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)
    if process.returncode != 0:
        raise RuntimeError(f"Error code {process.returncode}: {stderr}")
    return stdout

def generate_input(params):
    n = random.randint(params.min_n, params.max_n)
    x = random.randint(params.min_val, params.max_val)
    # Generate sorted array with possible duplicates
    a = sorted([random.randint(params.min_val, params.max_val) for _ in range(n)])
    # Format input: first line is n x, second line is n sorted integers
    return f"{n} {x}\n{' '.join(map(str, a))}"

def main():
    parser = argparse.ArgumentParser(description="Generate test cases for Binary Search.")
    parser.add_argument("solution", help="Path to C++ solution file (.cpp)")
    parser.add_argument("--cases", type=int, default=10, help="Number of test cases")
    parser.add_argument("--min-n", type=int, default=1, help="Min array length")
    parser.add_argument("--max-n", type=int, default=100000, help="Max array length")
    parser.add_argument("--min-val", type=int, default=-1000000000, help="Min value")
    parser.add_argument("--max-val", type=int, default=1000000000, help="Max value")
    parser.add_argument("--output-dir", default="binary_search_tests", help="Output directory")
    parser.add_argument("--compress", action="store_true", help="Compress output to zip")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    exe_path = os.path.join(tempfile.gettempdir(), "binary_search_exec")

    print(f"Compiling {args.solution}...")
    compile_cpp(args.solution, exe_path)
    print("Done.")

    for i in range(1, args.cases + 1):
        input_data = generate_input(args)
        output_data = run_executable(exe_path, input_data)

        in_path = os.path.join(args.output_dir, f"{i}.in")
        out_path = os.path.join(args.output_dir, f"{i}.out")
        with open(in_path, "w") as f_in:
            f_in.write(input_data + "\n")
        with open(out_path, "w") as f_out:
            f_out.write(output_data)
        print(f"Test case {i}: {in_path}, {out_path}")

    if args.compress:
        zip_name = shutil.make_archive(args.output_dir, 'zip', args.output_dir)
        print(f"Compressed to {zip_name}")

if __name__ == "__main__":
    main()