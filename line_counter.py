import pathlib
import sys

if len(sys.argv) < 3:
	print("syntax: py line_counter.py \"path\" \"filter\"\nfilters:\n*    - return all files\n*.py - return all .py files")
	quit()

path = sys.argv[1]
filt = sys.argv[2]

directory = pathlib.Path(path)

files = directory.rglob(filt)

total_lines = 0

for file in files:
	print(file)
	line_count = len( open(file, 'rt', errors="ignore").readlines() )
	print( "lines: ", line_count )
	total_lines += line_count

print("        Total lines: ", total_lines)

