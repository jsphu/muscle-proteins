import Bio.SeqIO
import os
# Opening all fasta files.
directory = os.getcwd()
fastas = []
for r,d,f in os.walk(directory):
    fastas_dir = "{}/fastas".format(directory)
    if fastas_dir == r:
        for faa in f:
            if faa.endswith(".faa"):
                fastas.append(faa)
# For Debugging
"""
print(fastas)
exit()
"""
muscle_pro = "./output/muscle-proteins.faa"
with open(muscle_pro,"w") as w:
    all_fastas = []
    for file in fastas:
        with open(f"../fastas/{file}","r") as r:
            r = r.read()
            all_fastas.append(r)
    w.write("".join(all_fastas))

records = Bio.SeqIO.parse(muscle_pro, "fasta")
count = Bio.SeqIO.write(records, "./output/muscle-proteins.genbank","genbank")

print(f"Converted {count} records")
