import sys

prev_reading = -1
inc_count = -1
for line in sys.stdin:
	if int(line) > prev_reading:
		inc_count += 1
	prev_reading = int(line)

print(inc_count)