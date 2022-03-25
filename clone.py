#!/usr/bin/python3
# 3/22/2022 - TyLaud
# Purpose: Recursively clones the contents of the source
#          directory to the destination directory with only
#          the files and directories not in the destination
#          directory. (does not overwrite and files that have
#          the same name in the destination directory from the
#          source.)

# Developed with Python 3.10
# Execute Command -> python3.10 clone.py source_dir dest_dir
import os
import sys
import shutil

def add_missing_files_helper(from_dir, to_dir,
                             from_dir_contents, to_dir_contents):

    difference = from_dir_contents.difference(to_dir_contents)
    if not len(difference):
        print(f"\nNothing to Add\ndirectory {from_dir} and {to_dir}\nSTATUS: EQUAL")
        return

    print("Files missing:")
    print(*difference, sep="\n")
    print()
    print("Adding files: ")
    for file in difference:
        if os.path.isdir(f"{from_dir}//{file}"):
            #file is a directory
            if os.path.exists(to_dir + "\\" + file):
                add_missing_files_helper(f"{from_dir}\\{file}", f"{to_dir}\\{file}",
                                         set(os.listdir(f"{from_dir}\\{file}")), 
                                         set(os.listdir(f"{to_dir}\\{file}")))
            else:
                os.mkdir(f"{to_dir}\\{file}")
                add_missing_files_helper(f"{from_dir}\\{file}", f"{to_dir}\\{file}",
                                         set(os.listdir(f"{from_dir}\\{file}")), 
                                         set(os.listdir(f"{to_dir}\\{file}")))
        else:
            #file is not a directory
            shutil.copy(f"{from_dir}\\{file}", to_dir)
            print(f"Added file {file} in {to_dir}")

def add_missing_files(from_dir, to_dir):
    folder1_content = set(os.listdir(from_dir))
    folder2_content = set(os.listdir(to_dir))
                            
    add_missing_files_helper(from_dir, to_dir,
                             folder1_content, folder2_content)

#add missing files between folder1 and folder2 to make them equal
if not len(sys.argv) == 3:
    print(f"Usage {sys.argv[0]} source_dir dest_dir")
    print("Purpose: Make two directories contain the same contents")
    sys.exit(-1)
else:
    dir_one = os.path.abspath(sys.argv[1])
    dir_two = os.path.abspath(sys.argv[2])
    print(dir_one)
    print(dir_two)
    add_missing_files(dir_one, dir_two)
                            



