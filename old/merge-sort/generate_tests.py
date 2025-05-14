#!/usr/bin/env python3
import argparse
import concurrent.futures
import os
import random
import subprocess
import tempfile
import shutil
import sys
import time
from pathlib import Path


def compile_cpp(source_path, output_path):
    """Compile C++ source code with error handling."""
    try:
        cmd = ["g++", "-std=c++17", source_path, "-O2", "-o", output_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Compilation error: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("Error: g++ compiler not found. Please ensure it's installed and in your PATH.", file=sys.stderr)
        return False


def run_executable(exe_path, input_data, timeout=5):
    """Run executable with input data and timeout protection."""
    try:
        process = subprocess.run(
            [exe_path], 
            input=input_data, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        if process.returncode != 0:
            raise RuntimeError(f"Error code {process.returncode}: {process.stderr}")
        return process.stdout
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Execution timed out after {timeout} seconds")


def generate_input(params):
    """Generate random test input based on parameters."""
    n = random.randint(params.min_n, params.max_n)
    
    # Generate array efficiently
    if params.max_n > 10000:  # For large arrays, use more efficient method
        a = [random.randint(params.min_val, params.max_val) for _ in range(n)]
    else:
        a = random.choices(range(params.min_val, params.max_val + 1), k=n)
    
    return f"{n}\n{' '.join(map(str, a))}"


def process_test_case(i, exe_path, params, output_dir, timeout):
    """Process a single test case with error handling."""
    try:
        input_data = generate_input(params)
        output_data = run_executable(exe_path, input_data, timeout)

        in_path = os.path.join(output_dir, f"{i}.in")
        out_path = os.path.join(output_dir, f"{i}.out")
        
        with open(in_path, "w") as f_in:
            f_in.write(input_data)
        with open(out_path, "w") as f_out:
            f_out.write(output_data)
            
        return i, True, None
    except Exception as e:
        return i, False, str(e)


def main():
    parser = argparse.ArgumentParser(description="Generate test cases for sorting algorithms.")
    parser.add_argument("solution", help="Path to C++ solution file (.cpp)")
    parser.add_argument("--cases", type=int, default=10, help="Number of test cases")
    parser.add_argument("--min-n", type=int, default=1, help="Min array length")
    parser.add_argument("--max-n", type=int, default=100000, help="Max array length")
    parser.add_argument("--min-val", type=int, default=-1000000000, help="Min value")
    parser.add_argument("--max-val", type=int, default=1000000000, help="Max value")
    parser.add_argument("--output-dir", default="sorting_tests", help="Output directory")
    parser.add_argument("--compress", action="store_true", help="Compress output to zip")
    parser.add_argument("--seed", type=int, help="Random seed for reproducibility")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout in seconds for each test case")
    parser.add_argument("--threads", type=int, default=os.cpu_count(), help="Number of parallel threads")
    args = parser.parse_args()

    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        print(f"Using random seed: {args.seed}")

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Verify solution file exists
    solution_path = Path(args.solution)
    if not solution_path.exists():
        print(f"Error: Solution file '{args.solution}' not found", file=sys.stderr)
        return 1
    
    # Create temporary executable
    exe_path = tempfile.mktemp(prefix="sorting_exec_")
    
    print(f"Compiling {args.solution}...")
    start_time = time.time()
    if not compile_cpp(args.solution, exe_path):
        print("Compilation failed. Exiting.", file=sys.stderr)
        return 1
    
    compile_time = time.time() - start_time
    print(f"Compilation successful ({compile_time:.2f}s)")
    
    # Generate test cases in parallel
    print(f"\nGenerating {args.cases} test cases using {min(args.threads, args.cases)} threads...")
    start_time = time.time()
    success_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(args.threads, args.cases)) as executor:
        futures = [
            executor.submit(process_test_case, i, exe_path, args, str(output_dir), args.timeout)
            for i in range(1, args.cases + 1)
        ]
        
        for future in concurrent.futures.as_completed(futures):
            i, success, error = future.result()
            if success:
                success_count += 1
                print(f"Test case {i}: Generated successfully")
            else:
                print(f"Test case {i}: Failed - {error}", file=sys.stderr)
    
    generation_time = time.time() - start_time
    print(f"\nGenerated {success_count}/{args.cases} test cases in {generation_time:.2f}s")
    
    # Clean up executable
    try:
        os.unlink(exe_path)
    except OSError:
        pass
    
    # Compress output if requested
    if args.compress and success_count > 0:
        zip_path = f"{args.output_dir}.zip"
        try:
            shutil.make_archive(args.output_dir, 'zip', args.output_dir)
            print(f"Compressed test cases to {zip_path}")
        except Exception as e:
            print(f"Failed to create zip archive: {e}", file=sys.stderr)
    
    return 0 if success_count == args.cases else 1


if __name__ == "__main__":
    sys.exit(main())