import os
import zipfile


for file in os.listdir("incomplete"):  # iterates through incomplete files

    if file[-4:] == ".zip":  # unzips file if applicable
        with zipfile.ZipFile(os.path.join("incomplete", file), 'r') as zip_ref:
            zip_ref.extractall(os.path.join("incomplete", file[:-4]))

        os.remove(os.path.join("incomplete", file))
        # removes zip file

    with open("incomplete.txt", "r") as f:
        data = f.read()

    with open(os.path.join("incomplete", file + ".txt"), "w") as f:
        f.write(data)

    # creates formatted comments text file in incomplete folder (with specified text)
    # univerally creates file for ALL (non-zip included) files in folder
    # zip/py/java/etc extensions will not be removed before txt added
    # this can be added and changed if desired, but will have no final effect