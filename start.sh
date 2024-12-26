#!/bin/bash

python3 -m venv .muscle_venv
wait

source ./.muscle_venv/bin/activate

pip install biopython
wait

python3 fasta_parser.py

cat muscle-proteins.genbank
