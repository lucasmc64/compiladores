from sys import argv
from getopt import getopt, error as getopt_error
from argparse import ArgumentParser
from os.path import basename, dirname, join

from lexicon import Lexer
from symbol_table import SymbolTable
from transition_table import TransitionTable
from productions import Productions
from syntactic import Syntactical

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

    symbol_table = SymbolTable()
    transition_table = TransitionTable(symbol_table)

    lexer = Lexer(file_path, transition_table)

    # while True:
    #     token = lexer.get_next_token()

    #     if token == None:
    #         print("Fim do arquivo!")
    #         break

    #     print(f"{token.name} {token.attribute}")

    #     print("\n")

    #productions = Productions(lexer)
    syntactical = Syntactical(file_path, transition_table)

    syntactical.analysis()

if __name__ == "__main__":
    main()
