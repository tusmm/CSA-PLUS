import os
import shutil
import zipfile


RUN_DIR = ""
CHECK_EXTENSION = ".py"
RUN_NAME = "pyramids.py"
FILE_NAMES = ["pyramids.py"]
ZIP_NAME = "hw.zip"
MAIN_DIR = os.getcwd()
# assignment-specific setting values


def run_program_python(dir, name):  # manages python file execution
    cmd = "py " + name
    os.chdir(dir)
    os.system(cmd)
    os.chdir(MAIN_DIR)


def run_program(dir, name):  # program run wrapper
    run_program_python(dir, name)


def extract(name, dir):  # extracts zip files
    with zipfile.ZipFile(name, 'r') as zip_ref:
        zip_ref.extractall(dir)


def view(file):  # displays user files in terminal
    for included in FILE_NAMES:
        try:
            path = os.path.join("hw", file)
            run = os.path.join(os.path.join(path, RUN_DIR), included)

            if not os.path.isfile(run):
                print("ERR")
                return

            print("\n---------------------")
            print(included)
            print("---------------------")

            with open(run, "r") as f:  # displays file text
                print(f.read())

            print("\n---------------------")
            design = input("Design comments: ")
            documentation = input("Documentation comments: ")
            style = input("Style comments: ")
            additional = input("Additional comments: ")
            # gets grader comments

            if len(FILE_NAMES) > 1:  # formats comments for single and multi-file projects
                data = "\n< " + included + " >\nDesign: " + design + "\nDocumentation: " + documentation + "\nStyle: " + style + "\n" + additional
            else:
                data = "\nDesign: " + design + "\nDocumentation: " + documentation + "\nStyle: " + style + "\n" + additional

            with open(os.path.join("comments", file + ".txt"), "a") as f:  # writes comments to local file
                f.write(data)
                
            os.rename(run, os.path.join(os.path.join(path, RUN_DIR), RUN_NAME + ".complete"))
        except:
            pass


def run_handle(path):  # handles program run
    print("---------------------")
    run_program(os.path.join(path, RUN_DIR), RUN_NAME)
    # runs program

    print("---------------------")

    complete = ""

    while complete.upper() != "Y" and complete.upper() != "N":  # queries for run completion information
        complete = input("Run complete? (Y/N): ")
                
    if complete.upper() == "N":  # handles incomplete program case
        complete = input("Rerun program (R) or mark incomplete (I): ")

        if complete.upper() == "R":  # reruns program
            complete = run_handle(path)
        else:
            complete = "N"
    
    return complete


def main():
    try:
        extract(ZIP_NAME, "hw")
        os.remove(ZIP_NAME)
        # extracts and removes homework zip file

    except:
        print("No hw.zip file.  Grading continuation program commencing...")

    files = os.listdir("hw")

    for file in files:  # iterates through homework files
        try:
            if file[-4:] == ".zip":
                path = os.path.join("hw", file[:-4])
                extract(os.path.join("hw", file), path)

                print("Student Info:")
                print(file[:-4])
                
                complete = run_handle(path)
                # initiates run handler and gets completion code

                if complete.upper() == "Y":  # queries for behavior comments on successful completion
                    comments = input("Behavior comments: ")
                    os.remove(os.path.join("hw", file))

                    with open(os.path.join("comments", file[:-4] + ".txt"), "w") as f:
                        f.write("Behavior: " + comments)

                    view(file[:-4])

                else:
                    shutil.copyfile(os.path.join("hw", file), os.path.join("incomplete", file))
                    os.remove(os.path.join("hw", file))
                    # puts unsuccessfully run or invalidly named files in the incomplete directory
                
                print("---------------------\n\n")
            
            elif file[-3:] == CHECK_EXTENSION and os.path.isfile(os.path.join("hw", file)):  # handles non-directory (lone) files
                q = input("Mark file " + file + " as incomplete? (Y/N): ")

                if q.upper() == "Y":
                    shutil.copyfile(os.path.join("hw", file), os.path.join("incomplete", file))

                os.remove(os.path.join("hw", file))

                print("---------------------\n\n")

        except Exception as a:  # handles file/other errors
            print(a)
            print("ERROR: SKIPPING")


if __name__ == "__main__":
    main()