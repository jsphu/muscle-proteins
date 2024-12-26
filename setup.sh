#!/bin/bash
echo -ne "script-started.(0/3)\r"

python3 -m venv .muscle_venv
wait
echo -ne "python3-venv-created.(1/3)\r"

source ./.muscle_venv/bin/activate

pip install biopython > /dev/null
wait
echo -ne "biopython-installed.(2/3)\r"
sleep 1

OUT=$(python3 parse.py) 

echo -ne "fastas-parsed-successfully.(3/3)\r"
sleep 1

cat ./output/muscle-proteins.gb
echo "$OUT"
