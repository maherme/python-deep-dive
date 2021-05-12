# With this code the order of the arguments does not matter
# Example: python example4.py --yob 2000 --last-name surname --first-name name

import sys

keys = sys.argv[1::2]
values = sys.argv[2::2]

args = {k: v for k, v in zip(keys, values)}

print(args)

first_name = args.get('--first-name', None)
last_name = args.get('--last-name', None)
yob = int(args.get('--yob', None))

print(first_name, last_name, yob)