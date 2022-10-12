import os
import zipfile


os.chdir("incomplete")


# rezips files in incomplete directory
for file in os.listdir():
    if os.path.isdir(file):
        with zipfile.ZipFile(file + ".zip", "w") as zf:
            
            os.chdir(file)

            for zfd in os.listdir():
            
                if os.path.isfile(zfd):  # zips files
                    zf.write(zfd)

                else:

                    for sub in os.walk(zfd):  # zips files in subfolders
                        for fin in sub[2]:
                            zf.write(os.path.join(sub[0], fin))
                            
        os.chdir("..")