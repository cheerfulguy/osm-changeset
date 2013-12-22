import csv
import sys


def chooserows(key, val, inputfile, outputfile):
    outrows = []

    with open(inputfile) as infileh:
        csvreader = csv.DictReader(infileh, delimiter = "\t")
        fields = csvreader.fieldnames
        for row in csvreader:
            if row[key] == val:
                outrows.append(row)

    with open(outputfile, "w") as outfileh:
        writer = csv.DictWriter(outfileh, fields)
        writer.writerows(outrows)

if __name__ == "__main__":

    inputfile = sys.argv[1].strip()
    outputfile = sys.argv[2].strip()
    key = "@oname"
    val = "node"
    
    chooserows(key, val, "map.csv", "mapfilter.csv")
    chooserows(key, val, inputfile, outputfile)
    
