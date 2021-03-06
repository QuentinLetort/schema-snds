import os

from src.byproducts.main import generate_byproducts
from src.constants import BYPRODUCTS_DIR, ROOTED_BYPRODUCTS_DIR

EXPECTED_BYPRODUCTS_DIR = 'expected_byproducts'


def test_generated_byproducts_equal_files():
    generate_byproducts()
    for root, dirs, files in os.walk(ROOTED_BYPRODUCTS_DIR):
        for file in files:
            actual_file_path = os.path.join(root, file)
            expected_file_path = actual_file_path.replace(BYPRODUCTS_DIR, EXPECTED_BYPRODUCTS_DIR)
            with open(actual_file_path, encoding="utf-8") as f:
                actual = f.read().split("\n")
            with open(expected_file_path, encoding="utf-8") as f:
                expected = f.read().split("\n")
            assert expected == actual
