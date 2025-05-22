import argparse
import os
import random
import subprocess
import tempfile
import shutil
import abc
import string

from generate_test_case.chuyen_ptnk_2023_2024.bai2.generator import SODBTestGenerator
from generate_test_case.generate_test import AutoGenerate

# Entry point of the script
if __name__ == "__main__":
    # Create an instance of the specific problem generator
    test_generator = SODBTestGenerator()
    
    # Create auto generator and run the test case generation
    auto_generator = AutoGenerate(test_generator)
    auto_generator.run()