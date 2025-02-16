import aifeynman
import sys
import os

# 現在の作業ディレクトリを最優先に追加
current_dir = os.path.abspath(".")
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# aifeynman.get_demos("example_data") # Download examples from server


vars_name = [
    # "kb",
    # "xdis",
    # "ydis",
    # "UMAP-1",
    # "UMAP-2",
    # "similarity",
    # "mw",
    # "Ne/Na",
    # "homo",
    # "lumo",
    # "Eiv",
    # "Eav",
    # "Vm",
    # "alpha",
    # "alpha/Vm",
    # "log10(R2)",
    # "G",
    # "log10(Q)",
    # "log10(RA)",
    # "mu",
    # "min(esp)",
    # "max(esp)",
    # "min(mbo)",
    # "max(mbo)",
    # "dEw",
    # "dEo",
    # "dEacid",
    # "dEbase",
    # "Tb",
    "q1",
    # "Ef",
    "q2",
    "epsilon",
    'r',
    # "mu",
    # "Nn",
    "F",
    # "m",
    # "g",
    # "z",
    # "U"
]


# aifeynman.run_aifeynman(
#    "/large/6_sasaki/AI-Feynman/example_data/",
#    "I.12.2",
#    10,
#    "14ops.txt",
#    polyfit_deg=1,
#    NN_epochs=500,
#    vars_name=vars_name,
# )
aifeynman.run_aifeynman(
    "/large/6_sasaki/AI-Feynman/example_data/",
    "example1.txt",
    60,
    "14ops.txt",
    polyfit_deg=3,
    NN_epochs=500,
)
