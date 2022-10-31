from asyncio import subprocess
import sys
import os
import shutil


# HW9 utility


pypath = os.path.join(sys.argv[2].replace('"', ""), sys.argv[1])



print("\n=======\nRUN\n=======\n")
os.system(f'python3 "{pypath}" 2018')

print("\n=======\nAUTO\n=======\n")

print("EXPECTED:\n----------")
print("Enter a name to investigate (return to quit): Liam")
print("year: 2018")
print("name: Liam")
print("count: 19860")
print("0.57% of all names")
print("Enter a name to investigate (return to quit): Zibah")
print("Zibah is not in the data.")
print("Enter a name to investigate (return to quit): Maria")
print("year: 2018")
print("name: Maria")
print("count: 2595")
print("0.07% of all names")
print("\n")

print("RESULTS:\n----------")

os.system(f'python3 "{pypath}" 2018 < input.txt')

print("\n")
