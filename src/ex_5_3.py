""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import argparse
import numpy as np
from argparse import ArgumentParser
import os

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    arg_obj = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile")
    arg_obj.add_argument("infile", type=argparse.FileType('r'))
    arg_obj.add_argument("outfile", type=argparse.FileType('w'))
    args_p_args = arg_obj.parse_args()
    os.makedirs(root_dir / "outputs", exist_ok=True)
    fldata = np.loadtxt(args_p.infile)
    mean_ = np.mean(fldata)
    zero_mean = fldata - mean_
    std1 = np.std(zero_mean)
    processed = zero_mean_data / std1
    np.savetxt(args_p.outfile, processed,fmt='%.2e')

