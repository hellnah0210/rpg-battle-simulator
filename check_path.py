import os
import sys

print(os.getcwd())
print(__file__)
print("Module paths:")

for path in sys.path:
    print(path)
    
print(len(sys.path))