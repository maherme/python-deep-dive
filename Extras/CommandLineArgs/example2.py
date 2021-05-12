import sys

numbers = [int(a) for a in sys.argv[1:]] # The arguments are strings
print(sum(numbers))