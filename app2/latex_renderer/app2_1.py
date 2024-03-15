import os
from csv import DictReader


TEX_FILE = "app2_output.tex"
TT_OPENING = [r"\documentclass{article}", 
              r"\usepackage{amsfonts,amsmath,amssymb,mathrsfs,braket,mathtools,booktabs}",
              r"\begin{document}",
              r"This is example text bla bla bla...",
              r"\begin{table}[t]",
              r"\centering"]
TT_BEGIN = r"\begin{tabular}"
TT_TOPRULE = r"\toprule"
TT_MIDRULE = r"\midrule"
TT_IMG_OPENING = r"\begin{center}"
TT_IMG_LINK = r"\includegraphics[width=0.85\linewidth]"
TT_IMG_CLOSING = [r"\end{center}", r"\end{document}"]
TT_CLOSING = [r"\hline",
              r"\end{tabular}", 
              r"\caption{This is cool table!}",
              r"\end{table}"]

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def compile_latex(data, img_path):
    ltx = TT_OPENING.copy()
    ltx.append(TT_BEGIN + "{" + " ".join(["c" for _ in range(len(data[0]))]) + "}")
    ltx.append(TT_TOPRULE)
    ltx.append("&".join([f"Column {i + 1}" for i in range(len(data[0]))]) + r" \\")
    ltx.append(TT_MIDRULE)
    for r in data:
        ltx.append("&".join(r) + r" \\")
    ltx.extend(TT_CLOSING)
    ltx.append(TT_IMG_OPENING)
    ltx.append(TT_IMG_LINK + "{" + img_path + "}")
    ltx.extend(TT_IMG_CLOSING)

    return "\n".join(ltx)


def generate_tex(input_file=None, img_file=None):
    if not input_file:
        input_file = os.path.join(DIR_PATH, "app1_input.csv")
    if not img_file:
        img_file = os.path.join(DIR_PATH, "app2_img.png")

    _, ext = os.path.splitext(input_file)
    if not os.path.exists(input_file) or ext != ".csv":
        raise ValueError("Data file is not valid")
    
    _, ext = os.path.splitext(img_file)
    if not os.path.exists(img_file) or ext != ".png":
        raise ValueError("Image file is not valid")
    
    data = []
    with open(input_file) as inp:
        r = DictReader(inp)
        for row in r:
            data.append(list(row.values()))

    ltx = compile_latex(data, img_file)
    with open(TEX_FILE, "w+") as f:
        f.write(ltx)
