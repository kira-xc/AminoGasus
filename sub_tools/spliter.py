#!/usr/bin/env python3
import sys,getopt
from os.path import exists,isdir
from os import _exit,mkdir
import shutil




def spliter_func(lines_per_file=300,patho="file.txt"): 
    try:
        lines_per_file=int(lines_per_file)
    except:
        print("size is not integer number!!")
        _exit(1)
    try:
        lines_per_file=int(lines_per_file)
        smallfile = None
        with open(patho) as bigfile:
            for lineno, line in enumerate(bigfile):
                if lineno % lines_per_file == 0:
                    if smallfile:
                        smallfile.close()
                    small_filename = 'splited_files_aminos/small_file_{}.txt'.format(str(lineno) +"_"+str(lineno+lines_per_file))
                    smallfile = open(small_filename, "w")
                if lineno % lines_per_file == lines_per_file-1:
                    smallfile.write(line.strip())
                else:
                    smallfile.write(line)
                
            if smallfile:
                smallfile.close()
        print("\ndone!\nall splited files is on 'splited_files_aminos' folder in workdir ")
    except Exception as e:
        print(e)
        _exit(1)

def main(argv):
    input_file=""
    size=""
    try:
        opts, args = getopt.getopt(argv, "i:s:", ["input=", "size="])
    except getopt.GetoptError:
        print("usage : spliter.py -i file.txt -s 300 ")
        print("        spliter.py --input=file.txt --size=300")
        sys.exit(2)
    if opts==[]:
        print("usage : spliter.py -i file.txt -s 300 ")
        print("        spliter.py --input=file.txt --size=300")
        print("        spliter.py --input file.txt --size 300")
        sys.exit(2)        
    for opt, arg in opts:
        if opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-s", "--size"):
            size = arg

    if exists(input_file):
        if exists("splited_files_aminos"):
            if isdir("splited_files_aminos"):
                shutil.rmtree("splited_files_aminos")
        mkdir("splited_files_aminos")
        spliter_func(size,input_file)
    else:
        print(input_file, "not exists ")
        _exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])