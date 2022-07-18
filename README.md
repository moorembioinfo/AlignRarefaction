# AlignRarefaction

![Python](https://badges.aleen42.com/src/python.svg) 

Generate rarefaction data from read-mapped (reference-based) bacterial whole-genome alignments. A population of bacterial genomes is input and varying population sizes sampled to assess the impact of increased number and diversity of genomes

## Usage

1. Run the main script `AlignRarefaction.py` referencing the path to your sample of (fasta format) genomes:

    ```shell
    python AlignRarefaction.py --alignment </path/to/alignment/alignmentfile> 
    ```

## Input

Multi-fasta whole genome alignment derived from mapping to a reference and variant calling such as from [snippy](https://github.com/tseemann/snippy), `snippy-core` and `snippy-clean_full_aln`:

```shell
snippy-core --ref ref.fa snippyoutfiles 
snippy-clean_full_aln core.full.aln > clean.full.aln
```

## Output

File | Description
-----|------------
`.csv`   | 

...

## Options

Flag &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Short flag | Description | Required | Default val
--------------|------------|-------------|----------|--------------
`--alignment` |  `-a`     |  Provide path and name of alignment file          | ✅
`--cutoff ` | `-c` |  Per-site percent core (integer)|    | 95
`--step ` | `-s` |  Step for random population size sampling |    | 10
`--minpop ` | `-mp` |  Minimum (starting) random population size |    | 20
`--iterations ` | `-itr` |  Number of iterations per population size |    | 100
`--keepref`  |           |  Remove reference sequence from the alignment              |    | False

