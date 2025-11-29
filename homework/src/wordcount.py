# Ejemplo para casos de uso
# python3 -m homework data/input data/output
import argparse
import sys

from ._internals.read_all_lines import read_all_lines


def parse_args():
    parser = argparse.ArgumentParser(description="Count words in files.")
    parser.add_argument(
        "input",
        type=str,
        help="Path to the input folder containing the files to process.",
    )
    parser.add_argument("output", type=str, help="Path to the output folder.")
    parsed_args = parser.parse_args()
    return parsed_args.input, parsed_args.output
    # también servirían:
    # 1. return sys.argv[1], sys.argv[2]
    # 2. input = sys.argv[1]; output = sys.argv[2]; return input, output


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
