import os

# this file serves as reference to remember the best way of doing certain things

# absolute path of script's parent directory
# python 3.9 (__file__ is ALWAYS absolute in 3.9 and later)
os.path.dirname(__file__)
# earlier than 3.9
os.path.dirname(os.path.abspath(__file__))

