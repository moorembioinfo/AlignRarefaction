#!/usr/bin/env python3
import os
import random
import numpy

def add_args(a):
    """
    Parses arguments for program.
    """
    parser = argparse.ArgumentParser(description=""" Test description """)
    parser.add_argument(
        "--alignment",
        "-a",
        help="Provide path and filename of alignment",
        required=True,
    )
    parser.add_argument(
        "--cutoff",
        "-c",
        help="Per-site percent core (integer). Default=95(%)",
        type=int,
        default=95,
    )
    parser.add_argument(
        "--nproc", "-p", help="Number of processes. Default: 1. ", type=int, default=1
    )
    parser.add_argument(
        "--step",
        help="Step for random population size sampling. Default=10",
        type=int,
        default=10,
    )
    parser.add_argument(
        "--minpop",
        help="Minimum (starting) random population size. Default=20",
        type=int,
        default=20,
    )
    parser.add_argument(
        "--iterations",
        help="Number of iterations per population size. Default=100",
        type=int,
        default=100,
    )

    args = parser.parse_args(a)
    return args



if __name__ == "__main__":

    args = add_args(sys.argv[1:])
    fn = args.alignment
    outname = f"{fn}.1l"
    output = open(outname, "w")
    popsize = 0

    for record in screed.open(fn):
        if not args.keepref:
            if record.name == "Reference":
                pass
            else:
                output.write(">" + record.name + "\n")
                output.write(record.sequence + "\n")
                popsize += 1
        else:
            output.write(">" + record.name + "\n")
            output.write(record.sequence + "\n")
            popsize += 1

    percentcore = args.cutoff
    output.close()
    print("Finished alignment format conversion")

    for i in range(args.minpop,popsize,args.step):
        listofsizes = []
        for j in range(0,args.iterations):
            listofsizes.append(rarefaction(i, allseqsdict))
            print(f'Iteration {i}')
        print(f'Finished popsize {popsize}')
        #outline= ','.join(str(x) for x in aln_lengths)
        outline= ','.join(listofsizes)
        output.write(f'{popsize},{outline}\n')
