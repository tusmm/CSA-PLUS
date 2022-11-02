import sys
import os
import shutil


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

os.system(f'py "{pypath}" < input.txt')
print("\n")