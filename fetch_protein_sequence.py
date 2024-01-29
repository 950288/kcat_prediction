import tqdm


fileName = "test.tsv"

with open(fileName, "r") as file:
    lines = file.readlines()
    length = len(lines)


with open(fileName, "w") as file:
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
            if len(line) == 9:
                continue
            if UniprotID == "":
                # fetch the sequence from NCBI
                sequence = "unavailable"
                
            else:
                # fetch the sequence from Uniprot
                sequence = "..."

            index += 1

            # write the sequence into the file
            lines[i] = ECNumber + "\t" + EnzymeType + "\t" + Organism + "\t" + Smiles + "\t" + Substrate + "\t" + UniprotID + "\t" + Value + "\t" + Unit + "\t" + sequence + "\n"

        if index % 10 == 0:
            file.writelines(lines)

    file.writelines(lines)           
                    

