from sys import argv
from getopt import getopt, error as getopt_error
from argparse import ArgumentParser
from os.path import basename, dirname, join

from lexicon import Lexer

def main():
    # The first element is the script name
    args = argv[1:]
    shortopts = 'hf:o:'
    longopts = ["help=", "file=", "output="]

    file_path = None
    output_path = None

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", nargs=1, required=True, type=str, help="Specifies the file to be compiled")
    parser.add_argument("-o", "--output", nargs=1, required=False, type=str, help="Defines a custom location and name for the generated file. By default the file will be created in the same folder with the name \"filename.agl.ir.ll\".")
    parser.parse_args()

    try:
        flags = getopt(args, shortopts, longopts)[0]

        for flag, value in flags:
            if flag in ["-f", "--file"]:
                file_path = value
            elif flag in ["-o", "--output"]:
                output_path = value

        if output_path == None:
            file_name = basename(file_path)
            output_name = f"{file_name[:file_name.rindex('.')]}.agl.ir.ll"
            output_path = join(dirname(file_path), output_name)

    except getopt_error as error:
        print(error)

    file = open(file_path)

    # lexer = Lexer()
    
    file.close()

if __name__ == "__main__":
    main()
