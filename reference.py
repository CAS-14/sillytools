import os

# this file serves as reference to remember the best way of doing certain things

# absolute path of script's parent directory in python 3.9+ (__file__ always abs.)
os.path.dirname(__file__)
# absolute path of script's parent directory before python 3.9
os.path.dirname(os.path.abspath(__file__))

# os.walk demo
for root, dirs, files in os.walk(".", topdown=False, onerror=None, followlinks=False):
    for file_name in files:
        file_path = os.path.join(root, file_name)
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)