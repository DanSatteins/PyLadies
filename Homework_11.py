# This program reads the receipt for Gallo Pinto from the input file, 
# replaces all the numbers in it with words, requires the number of guests
# expected and allows to add the name of the cook and if an egg is wished.

import argparse

# Definition of the numbers that shall be replaced by words. The receipt
# shall be read line by line and the replacements done.
def repl_numbers(line):
    ingr_words = {"0.25": "1/4",
                 "0.75": "3/4",
                 "1": "One",
                 "2": "Two",
                 "3": "Three",
                 "4": "Fourths"}

    for numb, ingr_word in ingr_words.items():
        line = line.replace(numb, ingr_word)
    return line

# The input file is opened in reading-mode to avoid an accidental
# over-writing. The output file is opened/created in write-mode.
def whole_file(input_file, output_file, guests, cook, egg):
    with open(input_file, "r", encoding="utf-8") as infile:
        line = infile.read()

    line = repl_numbers(line)

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(line)

    # Number of guests expected, line is added to file. Required.
    with open(output_file, "a") as f:
        f.write(f"Number of expected guests: {guests}\n")

    # Name of the cook, line is added to file when a name is provided.
    with open(output_file, "a") as f:
        if cook:
            f.write(f"The name of the cook is: {cook}\n")
 
    # Egg is added in a new line if provided (boolean is set to True).
    with open(output_file, "a") as f:
        if egg:
            f.write(f"Please add an egg")

# Argparse arguments, options and help are defined.
parser = argparse.ArgumentParser(description="Replace numbers by words in a famous Gallo Pinto receipt")
parser.add_argument("--input", dest="input_file", help="Original receipt")
parser.add_argument("--output", dest="output_file", help="File with the numbers replaced by words")
parser.add_argument("--guests", type=int, required = True, help="The number of expected guests")
parser.add_argument("-c", "--cook", default="Unknown", help="The name of the cook")
parser.add_argument("--egg", action="store_true", default=False, help="Indicates if an egg shall be added")

args = parser.parse_args()

# Exception to be printed if no input file is provided.
if args.input_file is not None:
    input_file = args.input_file
    output_file = args.output_file
    whole_file(input_file=args.input_file, output_file=args.output_file, guests=args.guests, cook=args.cook, egg=args.egg)
else:
    print("Please provide an input file using the --input option.")
    