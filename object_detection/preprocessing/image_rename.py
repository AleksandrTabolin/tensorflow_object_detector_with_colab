#!/usr/bin/env python

import os, sys
import argparse

def renameImage(position, file_name, input_dir, prefix = None):
    if (prefix is None):
        new_file_name = str(position)		
    else:
        new_file_name = prefix + "_" + str(position)

    input = input_dir + os.path.sep + file_name

    if os.path.isfile(input):
        extension = os.path.splitext(input)[1]

        output = input_dir + os.path.sep + new_file_name + extension

        try:
            os.rename(input, output)
            print('renamed: ', input, '; saved to ', output)    
        except FileExistsError as e:
            print('fail to rename:', input, 'already exists')        
        
    else:
        print('fail to rename:', input, 'is not a file')    

def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(description="image resizer")
    parser.add_argument("-i",
                        "--inputDir",
                        help="Path to the folder where the input image files are stored",
                        type=str)
    parser.add_argument("-p",
                        "--prefix",
                        help="output filename prefix",
                        type=str)    

    args = parser.parse_args()

    if(args.inputDir is None):
        args.inputDir = os.getcwd()
    
    assert(os.path.isdir(args.inputDir))

    for position, file in enumerate(os.listdir(args.inputDir)):
        renameImage(position, file, args.inputDir, args.prefix)

    print('All iamges renamed successfully')


if __name__ == '__main__':
    main()