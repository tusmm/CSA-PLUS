from asyncio import subprocess
import sys
import os
import shutil


<<<<<<< HEAD
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
=======
# HW8 utility


os.chdir(sys.argv[2].replace('"', ""))
pypath = sys.argv[1]


print("\n=======\nAUTO\n=======\n")
print("EXPECTED:\n----------")

print(

"""
Enter parts filename: droid_parts_3.txt
Starting a shift at the droid factory!
Building a new droid with serial number 10001
attaching arms...
attaching legs...
attaching body...
placing unneeded part back on belt: arms
placing unneeded part back on belt: body
attaching head...
Droid 10001 has been assembled!
Building a new droid with serial number 10002
attaching head...
attaching legs...
placing unneeded part back on belt: legs
attaching body...
placing unneeded part back on belt: head
attaching arms...
Droid 10002 has been assembled!
Building a new droid with serial number 10003
attaching arms...
attaching body...
attaching legs...
attaching head...
Droid 10003 has been assembled!
All of the droids have been assembled! Time to clock out and play Sabacc...
"""

)

print("RESULTS:\n----------")

os.system(f'py "{pypath}"')
print("\n")
>>>>>>> d42e7d3e4b499eb60a1d2afa2d94deee3f8d6d98
