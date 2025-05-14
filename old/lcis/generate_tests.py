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
        raise RuntimeError(f"Executable returned error code {process.returncode}: {stderr}")
    return stdout

def generate_input(params):
    """Generate a random test input for LCIS problem."""
    n = random.randint(params.min_n, params.max_n)
    m = random.randint(params.min_m, params.max_m)
    # Generate two sequences a and b
    a = [random.randint(params.min_val, params.max_val) for _ in range(n)]
    b = [random.randint(params.min_val, params.max_val) for _ in range(m)]
    # Format input: first line is n m, second line is n integers, third line is m integers
    return f"{n} {m}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}"

def main():
    parser = argparse.ArgumentParser(description="Generate test cases for LCIS problem using a C++ solution as oracle.")
    parser.add_argument("solution", help="Path to C++ solution file (.cpp)")
    parser.add_argument("--cases", type=int, default=10, help="Number of test cases to generate")
    parser.add_argument("--min-n", type=int, default=1, help="Minimum length of sequence a")
    parser.add_argument("--max-n", type=int, default=1000, help="Maximum length of sequence a")
    parser.add_argument("--min-m", type=int, default=1, help="Minimum length of sequence b")
    parser.add_argument("--max-m", type=int, default=1000, help="Maximum length of sequence b")
    parser.add_argument("--min-val", type=int, default=-1000000000, help="Minimum value in sequences")
    parser.add_argument("--max-val", type=int, default=1000000000, help="Maximum value in sequences")
    parser.add_argument("--output-dir", default="lcis_tests", help="Directory to write .in and .out files")
    parser.add_argument("--compress", action="store_true", help="Compress output directory into a zip file after generation")
    args = parser.parse_args()

    # Prepare output directory
    os.makedirs(args.output_dir, exist_ok=True)
    exe_path = os.path.join(tempfile.gettempdir(), "lcis_solution_exec")

    # Compile the C++ solution
    print(f"Compiling {args.solution}...")
    compile_cpp(args.solution, exe_path)
    print("Compilation finished.")

    # Generate test cases
    for i in range(1, args.cases + 1):
        input_data = generate_input(args)
        output_data = run_executable(exe_path, input_data)

        in_path = os.path.join(args.output_dir, f"{i}.in")
        out_path = os.path.join(args.output_dir, f"{i}.out")
        with open(in_path, "w") as f_in:
            f_in.write(input_data + "\n")
        with open(out_path, "w") as f_out:
            f_out.write(output_data)
        print(f"Generated test case {i}: {in_path}, {out_path}")

    # Compress if requested
    if args.compress:
        zip_name = shutil.make_archive(args.output_dir, 'zip', root_dir=args.output_dir)
        print(f"Compressed tests into {zip_name}")

if __name__ == "__main__":
    main()