def purge():
    counter = open("raw.txt", "r")
    text = counter.read()
    counter.close()

    rawFile = open("raw.txt", "r")
    outFile = open("out.txt", "w")

    for i in range(len(text)):
        char = rawFile.read(1)
        if i >= 280 and i < len(text) - 314:
            outFile.write(char)

    rawFile.close()
    outFile.close()

def split():
    outFile = open("out.txt", "r")    
    splitFile = open("split.txt", "w")

    for line in outFile:
        for word in line.split():
            splitFile.write(word)
            splitFile.write("\n")

    outFile.close()
    splitFile.close()

def scanner():
    splitFile = open("split.txt", "r")
    matches = []
    for word in splitFile:
        word = word[:-1]
        if word[-1] == ',': word = word[:-1]
        
        for keyWord in ["Cancer", "Precision", "Medicine", "Pediatrics", "Neurology", "Glymphatic", "Brain",  "Tumors", "Quiescent", "Cells", "Genetics", "Genomics", "Epigenetics", "Sequencing", "Multiphoton", "MRI", "PET", "CT", "Computational", "Biology", "Bioinformatics", "Machine", "Learning", "Tumor", "Microenvironments"]:
            if word == keyWord:
                matches.append(keyWord)
    
    if len(matches) == 0:
        print("\nNo matches found\n")
    else:
        matches.sort()
        if len(matches) > 1:
            for i in range(len(matches) - 1):
                for j in range(len(matches) - 1, i, -1):
                    if matches[i] == matches[j]:
                        matches.pop(j)
        result = "\nMatches: "
        for match in matches:
            result += match + ", "
        print(result[:-2] + "\n")

    splitFile.close()

def main():
    purge()
    split()
    scanner()

if __name__ == '__main__':
    main()