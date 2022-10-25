# Created by Isabella Lemus
# CSV Combiner project for PMG Programming Challenge
# 10/20/2022
#
# This class contains methods to read CSV files passed through the command 
# line and combine them into one file to be printed.
# The new file will contain a column identifying the name of the origin file
# of each element.
#
import csv
import sys

class CSVCombiner:

    def __init__(self) -> None:

        # Created a method instead for testing purposes
        #
        # First make sure that file(s) have been given as arguments
        # if ((len(sys.argv)) > 1):
        #     self.numArgs = len(sys.argv)
        # else:
            # If there are no arguments, quit program
        #     self.numArgs = 0
            
        # Set up to store given arguments, create the new file, check 
        # the order of the existing files
        self.args = []
        self.header = ["email_hash","category","filename"]
        self.contents = []
        self.storeArgs()        

    def storeArgs(self):
        for i in range(1, len(sys.argv)):
            self.args.append(sys.argv[i])
        if (len(self.args) == 0):
            print("Enter a valid file in command line. Try again.")
            exit()

    # Method to display new CSV file using pandas
    # for user clarity
    def displayCSV(self, fileName):
        import pandas as pan
        toDisplay = pan.read_csv(fileName)
        print(toDisplay.to_string())

    # Method to construct a new CSV file with a new column
    def constructCSV(self, fileName):
        with open(fileName, 'w') as file:
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
        for i in range(0, len(self.args)):
            # Extract the file name
            fName = self.getFileName(self.args[i])
            # Print file contents
            with open(self.args[i], 'r') as file:
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
        self.constructCSV("newCSV.csv")
        # Read the new file to stdout
        self.displayCSV("newCSV.csv")

# Create CSVCombiner object
# Run program
csvC = CSVCombiner()
csvC.main()