TT_OPENING = [r"\documentclass{article}", 
              r"\usepackage{amsfonts,amsmath,amssymb,mathrsfs,braket,mathtools,booktabs}",
              r"\begin{document}",
              r"This is example text bla bla bla...",
              r"\begin{table}[t]",
              r"\centering"]
TT_BEGIN = r"\begin{tabular}"
TT_TOPRULE = r"\toprule"
TT_MIDRULE = r"\midrule"
TT_CLOSING = [r"\hline",
              r"\end{tabular}", 
              r"\caption{This is cool table!}",
              r"\end{table}",
              r"\end{document}"]


def compile_latex(data):
    ltx = TT_OPENING.copy()
    ltx.append(TT_BEGIN + "{" + " ".join(["c" for _ in range(len(data[0]))]) + "}")
    ltx.append(TT_TOPRULE)
    ltx.append("&".join([f"Column {i + 1}" for i in range(len(data[0]))]) + r" \\")
    ltx.append(TT_MIDRULE)
    for r in data:
        ltx.append("&".join(r) + r" \\")
    ltx.extend(TT_CLOSING)

    return "\n".join(ltx)
