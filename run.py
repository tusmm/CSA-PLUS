import sys
import os
import shutil


# HW7 utility


txtpath1 = os.path.join(sys.argv[2].replace('"', ""), "word_list.txt")
txtpath2 = os.path.join(sys.argv[2].replace('"', ""), "words_sorted.txt")

shutil.copy("word_list.txt", txtpath1)
shutil.copy("words_sorted.txt", txtpath2)

pypath = os.path.join(sys.argv[2].replace('"', ""), sys.argv[1])

print("\n=======\nRUN\n=======\n")
os.system(f'py "{pypath}"')
print("\n")

print("\n=======\nAUTO\n=======\n")

print("\nBinary:\n");
print("EXPECTED:\n----------")
print("< boy >")
print("< cold >")
print("< dog >")
print("< bass >\n")
print("RESULTS:\n----------")

os.system(f'py "{pypath}" < input1.txt')
print("\n")

print("\nLinear:\n");
print("EXPECTED:\n----------")
print("< back >")
print("< cat >")
print("< dog >\n")
print("RESULTS:\n----------")

os.system(f'py "{pypath}" < input2.txt')
print("\n")

os.remove(txtpath1)
os.remove(txtpath2)