# === Stage 55: Add a setting to disable colorized output ===
# Project: BillWatch
import sys

def parse_args():
    args = sys.argv[1:]
    if "--no-color" in args:
        args.remove("--no-color")
        sys.stderr.write("Color output disabled.\n")
        return args, False
    return args, True
