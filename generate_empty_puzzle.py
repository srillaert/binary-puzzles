import sys

if len(sys.argv) < 2:
	print("Usage: python " + sys.argv[0] + " <number_of_columns>")
	sys.exit(1)

size = int(sys.argv[1])
if size % 2 != 0:
	print("Argument <number_of_columns> of " + str(size) + " is not a multiple of 2")
	sys.exit(1)

line = "." * size
for i in range(size):
	print(line)
