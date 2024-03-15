import os
import argparse
from csv import DictReader

from app1_1 import compile_latex


TEX_FILE = "app1_output.tex"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--csv-path", type=str, help="Path to csv data file", required=True
    )

    args = parser.parse_args()
    input_file = args.csv_path

    _, ext = os.path.splitext(input_file)
    if not os.path.exists(input_file) or ext != ".csv":
        raise ValueError("File is not valid")
    
    data = []
    with open(input_file) as inp:
        r = DictReader(inp)
        for row in r:
            data.append(list(row.values()))

    ltx = compile_latex(data)
    with open(TEX_FILE, "w+") as f:
        f.write(ltx)
