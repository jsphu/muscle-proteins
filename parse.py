""" converts individual amino acid fastas to genbank format """

if __name__ == "__main__":

    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    from Bio.SeqFeature import SeqFeature, FeatureLocation
    from Bio import SeqIO

    from os import getcwd, walk, path, mkdir 
    
    # Opening all fasta files.
    directory = getcwd()

    fastas = []
    for r,d,f in walk(directory):

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

    if not path.isdir("./output"):
        mkdir("./output")

    with open(muscle_pro,"w") as w:
    
        all_fastas = []
        for file in fastas:
    
            with open(f"./fastas/{file}","r") as r:
                r = r.read()
                all_fastas.append(r)
    
        w.write("".join(all_fastas))

    records = []
    for record in SeqIO.parse(muscle_pro,"fasta"):

        record.annotations["molecule_type"]="protein"
    
        feature=SeqFeature(FeatureLocation(0, len(record.seq)), type="region")
    
        record.features.append(feature)
    
        records.append(record)

    with open(f"{muscle_pro[:-3]}gb","w") as gb:
        SeqIO.write(records, gb, "genbank")

    print(f"Converted to {muscle_pro[:-3]}gb")

""" Y. Unal 2024 """
