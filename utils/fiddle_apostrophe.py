import glob
import re

apos_tab = "’	"

period = re.compile("^[.]+	")
decade = re.compile("^[0-9]+	")

filenames = glob.glob("*tsv")
for filename in filenames:
    with open(filename, encoding="utf-8") as fin:
        lines = fin.readlines()
    change = False

    line_idx = 0
    while line_idx < len(lines):
        if (decade.match(lines[line_idx]) and
            line_idx < len(lines) - 1 and
            lines[line_idx+1].startswith("s	O")):# and
            #lines[line_idx].split("\t", maxsplit=1)[1].replace("B-", "I-") == lines[line_idx+1].split("\t", maxsplit=1)[1]):
            lines[line_idx] = lines[line_idx].split("\t", maxsplit=1)[0] + "s	" + lines[line_idx].split("\t", maxsplit=1)[1]
            lines = lines[:line_idx+1] + lines[line_idx+2:]
            change = True
        line_idx += 1
    if change:
        with open(filename, "w", encoding="utf-8") as fout:
            for line in lines:
                fout.write(line)
