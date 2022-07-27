#!/usr/bin/env python3
import os
import random
import numpy
import sys
import argparse
from itertools import repeat, combinations
from concurrent.futures import ProcessPoolExecutor


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

def rarefaction(iteration, allseqsdict, subpopsize, cutoff):
    """
    Run rarefaction by counting sites for sampled
    population present in ≥Threshold% taxa
    """
    #Get random genome sample
    subsamplekeys = random.sample(list(allseqsdict.keys()), subpopsize)
    #Iterate each sequence and record gaps
    indexdict={}
    for key in subsamplekeys:
        seq = allseqsdict.get(key)
        pos =0
        for nuc in seq:
            if nuc in ("-", "N"):
                if pos in indexdict:
                    indexdict[pos] = indexdict.get(pos) + 1
                else:
                    indexdict[pos] = 1
            counter+=1
    seqlen = len(allseqsdict.get(subsamplekeys[0]))
    threshold_genomes = (round(subpopsize)/100)*cutoff
    noncoresites = 0
    for pos in indexdict:
        if indexdict.get(pos)<threshold_genomes:
            noncoresites+=1
    coresites = seqlen-noncoresites
    return(coresites)


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

    allresults = []
    for i in range(args.minpop,popsize,args.step):
        listofsizes=[]
        nproc = args.nproc
        if nproc ==1:
            for j in range(0,args.iterations):
                listofsizes.append(rarefaction(i, allseqsdict))
                print(f'Iteration {i}')
            print(f'Finished popsize {popsize}')
            #outline= ','.join(str(x) for x in aln_lengths)
            outline= ','.join(listofsizes)
            output.write(f'{popsize},{outline}\n')
        else:
            chunk_size = args.iterations/nproc
            rangelist = list(range(0,args.iterations))
            chunks = [
                rangelist[i : i + chunk_size] for i in range(0, len(rangelist), chunk_size)
            ]
            subpopsize=i

            with ProcessPoolExecutor(nproc) as executor:
                results = executor.map(rarefaction(chunks, repeat(allseqsdict), repeat(subpopsize), repeat(args.cutoff) )))

                allresults.append(results):
        print(f"Finished popsize: {i}")
    print(allresults)
