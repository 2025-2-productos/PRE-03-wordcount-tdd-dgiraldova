# Ejemplo para casos de uso
# python3 -m homework data/input data/output

import argparse

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


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
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(word_counts, output_folder)
