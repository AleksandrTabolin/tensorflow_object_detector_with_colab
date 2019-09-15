#!/usr/bin/env python

from PIL import Image
import os, sys
import argparse

def resizeImage(file_name, input_dir, output_dir, size=(1024,768)):
    input = input_dir + os.path.sep + file_name
        
    if os.path.isfile(input):
        output = output_dir + os.path.sep + file_name

        im = Image.open(input).resize(size, Image.ANTIALIAS) 
        im.save(output, "JPEG")

        print('resized: ', input, '; saved to ', output)    


def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(description="image resizer")
    parser.add_argument("-i",
                        "--inputDir",
                        help="Path to the folder where the input image files are stored",
                        type=str)
    parser.add_argument("-o",
                        "--outputDir",
                        help="Path to the folder where the output image files will be stored", type=str)
    parser.add_argument("-i_w",
                        "--imageWidth",
                        help="image width",
                        type=int)
    parser.add_argument("-i_h",
                        "--imageHeight",
                        help="image_height",
                        type=int)

    args = parser.parse_args()

    if(args.inputDir is None):
        args.inputDir = os.getcwd()
    if(args.outputDir is None):
        args.outputDir = args.inputDir + os.path.sep + "resized"
    if(args.imageWidth is None):
        args.imageWidth = 1024
    if(args.imageHeight is None):
        args.imageHeight = 768        

    assert(os.path.isdir(args.inputDir))

    if not os.path.exists(args.outputDir):
        os.mkdir(args.outputDir)    

    for file in os.listdir(args.inputDir):
        resizeImage(file, args.inputDir, args.outputDir, size=(args.imageWidth, args.imageHeight))

    print('All iamges resized successfully')


if __name__ == '__main__':
    main()