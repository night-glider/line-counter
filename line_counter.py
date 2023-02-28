import pathlib
import sys

if len(sys.argv) < 3:
	print("syntax: line_counter \"path\" \"filter\"\nfilters:\n*    - return all files\n*.py - return all .py files")
	sys.exit()

path = sys.argv[1]
filt = sys.argv[2]

directory = pathlib.Path(path)

files = directory.rglob(filt)

total_lines = 0

for file in files:
	print(file)
	try:
		line_count = len( open(file, 'rt', errors="ignore").readlines() )
		print( "lines: ", line_count )
		total_lines += line_count
	except:
		print("Can't open file")

print("        Total lines: ", total_lines)

