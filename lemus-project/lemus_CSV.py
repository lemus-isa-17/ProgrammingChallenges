# Created by Isabella Lemus
# CSV Combiner project for PMG Programming Challenge
# 10/22/2022
#
# This class contains methods to read CSV files passed through the command 
# line and combine them into one file to be printed.
# The new file will contain a column identifying the name of the origin file
# of each element.
#
# This will be fun :)
import csv
import sys

class CSVCombiner:

    def __init__(self) -> None:
        # First make sure that file(s) have been given as arguments
        if ((len(sys.argv)) > 1):
            self.numArgs = len(sys.argv)
        else:
            # If there are no arguments, quit program
            self.numArgs = 0
            print("File not valid or does not exist. Try again.")
            exit()
        # Set up to create the new file, check the order of the existing files
        self.header = ["email_hash", "category", "filename"]
        self.contents = []

    def displayCSV(self):
        import pandas as pan
        toDisplay = pan.read_csv("newCSV.csv")
        print(toDisplay.to_string())
        #with open("newCSV.csv", 'r') as file:
        #    csvRead = csv.reader(file)
        #    for row in csvRead:
        #        print(row)

    # Method to construct a new CSV file with a new column
    def constructCSV(self):
        with open('newCSV.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
            writer.writerows(self.contents)

    # Method to check order of file
    # Returns True or False
    def checkOrder(self, one):
        if (one == "category"):
            return False
        else:
            return True
    
    # Method to extract file name
    # Returns file name
    def getFileName(self, filePath):
        fSplit = filePath.split("/")
        fName = fSplit[-1]
        return fName

    # Method to open the files from the cmd line arguments, combine them into one
    # file, and print contents of new file.
    def main(self):
        for i in range(1, self.numArgs):
            # Extract the file name
            fName = self.getFileName(sys.argv[i])
            # Print file contents
            with open(sys.argv[i], 'r') as file:
                csvRead = csv.reader(file)
                inOrder = True
                for row in csvRead:
                    # Order the file contents
                    if(csvRead.line_num == 1):
                        inOrder = self.checkOrder(row[0])
                    else:
                        if (inOrder):
                            self.contents.append([row[0], row[1], fName])
                        else:
                            self.contents.append([row[1], row[0], fName])
            # Make new CSV file
            self.constructCSV()
            # Read the new file to stdout
            self.displayCSV()

# Create CSVCombiner object
# Run program
csvC = CSVCombiner()
csvC.main()