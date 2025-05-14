import argparse
import os
import random
import subprocess
import tempfile
import shutil
import abc
import string


class GenerateTest(abc.ABC):
    """
    Abstract base class for generating test cases.
    This class should be extended for each specific problem.
    """
    @abc.abstractmethod
    def generate_inputs(self, params):
        """
        Generate input data for all test cases at once.
        
        Args:
            params: Command line arguments
            
        Returns:
            List of strings, each containing input data for one test case
        """
        pass

    def get_argument_parser(self):
        """
        Get the argument parser with problem-specific arguments.
        Override this method to add custom arguments.
        
        Returns:
            argparse.ArgumentParser object
        """
        parser = argparse.ArgumentParser(description="Generate test cases")
        parser.add_argument("solution", help="Path to C++ solution file (.cpp)")
        parser.add_argument("--cases", type=int, default=10, help="Number of test cases")
        parser.add_argument("--output-dir", default="test_cases", help="Output directory")
        parser.add_argument("--compress", action="store_true", help="Compress output to zip")
        
        # Problem-specific arguments should be added here by subclasses
        return parser


class AutoGenerate:
    """
    Fixed class to handle test case generation, execution, and management.
    """
    def __init__(self, test_generator):
        """
        Initialize with a specific test generator.
        
        Args:
            test_generator: An instance of a GenerateTest subclass
        """
        self.test_generator = test_generator
        
    def compile_cpp(self, source_path, output_path):
        """
        Compile a C++ source file.
        
        Args:
            source_path: Path to C++ source file
            output_path: Path for compiled executable
        """
        cmd = ["g++", "-std=c++17", source_path, "-O2", "-o", output_path]
        subprocess.check_call(cmd)
        
    def run_executable(self, exe_path, input_data):
        """
        Run an executable with the given input data.
        
        Args:
            exe_path: Path to executable
            input_data: Input data as string
            
        Returns:
            Output data as string
        """
        process = subprocess.Popen(
            [exe_path], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        stdout, stderr = process.communicate(input=input_data)
        if process.returncode != 0:
            raise RuntimeError(f"Error code {process.returncode}: {stderr}")
        return stdout
        
    def run(self):
        """
        Main execution method to generate test cases, run solution, and save results.
        """
        # Parse arguments
        parser = self.test_generator.get_argument_parser()
        args = parser.parse_args()
        
        # Prepare output directory
        os.makedirs(args.output_dir, exist_ok=True)
        
        # Compile solution
        exe_path = os.path.join(tempfile.gettempdir(), "solution_exec")
        print(f"Compiling {args.solution}...")
        self.compile_cpp(args.solution, exe_path)
        print("Done.")
        
        # Generate all test cases at once
        print("Generating test cases...")
        all_inputs = self.test_generator.generate_inputs(args)
        print(f"Generated {len(all_inputs)} test cases.")
        
        # Process each test case
        for i, input_data in enumerate(all_inputs, 1):
            print(f"Processing test case {i}...")
            output_data = self.run_executable(exe_path, input_data)
            
            in_path = os.path.join(args.output_dir, f"{i}.in")
            out_path = os.path.join(args.output_dir, f"{i}.out")
            
            with open(in_path, "w") as f_in:
                f_in.write(input_data + "\n")
            with open(out_path, "w") as f_out:
                f_out.write(output_data)
                
            print(f"Saved test case {i}: {in_path}, {out_path}")
            
        # Compress if requested
        if args.compress:
            zip_name = shutil.make_archive(args.output_dir, 'zip', args.output_dir)
            print(f"Compressed to {zip_name}")