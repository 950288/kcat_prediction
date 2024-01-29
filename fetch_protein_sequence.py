# fetch the protein sequence from BRENDA or Uniprot

import requests
import tqdm

fileName = "test.tsv"

def get_sequence_from_UniPort(UniprotID, ECNumber, Organism):
    if UniprotID != "":
        url = "https://www.uniprot.org/uniprot/" + UniprotID + ".fasta"
    elif Organism != "":
        url = "https://rest.uniprot.org/uniprotkb/search?format=fasta&query=(ec:" + ECNumber + ")%20AND%20(organism_name:" + Organism + ")"
    else:
        url = "https://rest.uniprot.org/uniprotkb/search?format=fasta&query=ec:" + ECNumber
    response = requests.get(url)

    if response.status_code == 200:
        # convert fasta to sequence
        sequence = ""
        for line in response.text.split("\n"):
            if not line.startswith(">"):
                sequence += line
        print(sequence)
        print("\n")
        return sequence
    print(response)
    return "unavailable"

with open(fileName, "r") as file:
    lines = file.readlines()
    # length = len(lines)

with open(fileName, "w") as file:   
    file.seek(0)
    file.writelines(lines)  
    index = 0
    for i , line in tqdm.tqdm(enumerate(lines)):
        if not line:
            break
        if line.startswith("ECNumber"):
            header = line.split("\t")
            if len(header) == 8:
                lines[i] = line.replace("\n", "") + "\tSequence\n"
            continue
        else:
            sequence = ""
            line = line.split("\t")
            print(line)
            ECNumber = line[0]
            EnzymeType = line[1]
            Organism = line[2]
            Smiles = line[3]
            Substrate = line[4]
            UniprotID = line[5]
            Value = line[6]
            Unit = line[7].replace("\n", "")
            if (len(line) == 9) and (line[8] != ""):
                continue

            sequence = get_sequence_from_UniPort(UniprotID.replace("\t", ""), ECNumber.replace("\t", ""), Organism.replace("\t", ""))
            index += 1

            # write the sequence into the file
            lines[i] = ECNumber + "\t" + EnzymeType + "\t" + Organism + "\t" + Smiles + "\t" + Substrate + "\t" + UniprotID + "\t" + Value + "\t" + Unit + "\t" + sequence + "\n"

        if index % 10 == 0:
            file.seek(0)
            file.writelines(lines)

    file.writelines(lines)  
    file.seek(0)      