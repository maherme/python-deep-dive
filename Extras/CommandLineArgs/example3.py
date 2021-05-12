import sys

print(sys.argv[1:])
# This example is designed to catch the arguments and options in pairs
# Example: python example3.py --opt1 param1 --opt2 param2
for i in range(1, len(sys.argv), 2):
    print(sys.argv[i], sys.argv[i+1])