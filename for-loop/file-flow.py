import os
from time import sleep


def look_for_files() -> bool:
    print("Look for files... BEGIN")
    subdir = "./files-input"
    foundquit = False
    for filename in os.listdir(subdir):
        print("file: ", str(filename))
        filepath = "{}/{}".format(subdir,filename)
        file1 = open(filepath, 'r')
        for line in file1:
            if not line:
                break
            print("Line content: {}".format(line.strip()))
            if (line == "quit"):
                foundquit = True
        file1.close()
        os.remove(filepath)
    print("Look for files... END")
    return foundquit


while (True):
    if look_for_files() is True:
        print("The quit word was found! So let us end the program")
        break
    sleep(5)