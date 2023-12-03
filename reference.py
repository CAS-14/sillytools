import os

# this file serves as reference to remember the best way of doing certain things

# absolute path of script's parent directory
# python 3.9 (__file__ is ALWAYS absolute in 3.9 and later)
os.path.dirname(__file__)
# earlier than 3.9
os.path.dirname(os.path.abspath(__file__))

# os.walk usage
for root, dirs, files in os.walk("."):
    for name in files:
        print(f"file: {os.path.join(root, name)}")
    for name in dirs:
        print(f"dir: {os.path.join(root, name)}")