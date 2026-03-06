# compare all 3 policies given 1 input

from algorithms.fifo import fifo
from algorithms.lru import lru
from algorithms.optff import optff

def read_input(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
        k = int(lines[0].strip().split()[0])
        m = int(lines[0].strip().split()[1])
        requests = [int(n) for n in lines[1].strip().split()]
    return k, m, requests

def print_output(fifo_misses, lru_misses, optff_misses, outputfile = ""):
    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")
    
    if outputfile:
        with open(outputfile, "w") as f:
            f.write(f"FIFO  : {fifo_misses}\n")
            f.write(f"LRU   : {lru_misses}\n")
            f.write(f"OPTFF : {optff_misses}\n")  

if __name__ == "__main__":

    # MANUAL SET THESE, IF BLANK, WILL PROMPT USER
    input_file = "inputs/question2.in"
    output_file = "outputs/question2.out"

    if len(input_file) == 0:
        input_file = input("Enter the input file name: ")
    if len(output_file) == 0:
        output_file = input("Enter the output file name (leave blank to print to disregard): ")

    k, m, requests = read_input(input_file)

    # verify input
    if k <= 0:
        print("Cache capacity must be a positive integer.")
        exit(1)

    
    fifo_misses = fifo(k, m, requests)
    lru_misses = lru(k, m, requests)
    optff_misses = optff(k, m, requests)


    print_output(fifo_misses, lru_misses, optff_misses, output_file)