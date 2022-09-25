import sys
import os
import shutil


# Example utility test run file


txtpath = os.path.join(sys.argv[2].replace('"', ""), "rockyou.txt")
shutil.copy("rockyou.txt", txtpath)

pypath = os.path.join(sys.argv[2].replace('"', ""), sys.argv[1])

print("\n=======\nRUN\n=======\n")
os.system(f'py "{pypath}"')

print("\n=======\nAUTO\n=======\n")

print("EXPECTED:\n----------")
print("< Often used > < No special character >")
print("< No special character >")
print("< Too short > < Often used > <No digit > < No special character >")
print("< Password strong >")
print("< No special character >")
print("----------\n")

os.system(f'py "{pypath}" < input.txt')
print("\n")

os.remove(txtpath)