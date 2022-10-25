# Lemus CSV Combiner  

This project is created by Isabella Lemus to fulfill the CSV Combiner Programming Challenge designed by PMG.  

The contents of the project include the CSVCombiner (lemus_CSV.py), the fixtures folder (CSV files to input), the testing class (test.py), and a document detailing my thought process and approach to the challenge for personal use (lemus_doc.md).  

## Function   

The program takes CSV files as input from the command line and outputs a new CSV file containing the information from the original file inputs in addition to a new column that includes the filename from which the row originated.    

The new column is titled 'filename'.  

The program is able to handle more than two inputs, inputs with different columns, and large files.   

## Running the program    

The program runs from the command line, where the CSV files to combine are included as arguments. For example, to run the code, one could write:  

'python3 lemus_CSV.py ./fixtures/clothing.csv ./fixtures/accessories.csv'

The code then outputs the rows from the original files with the new 'filename' column included.

## Testing

Unfortunately, full testing is not complete for this project.   

Due to my lack of experience with python, and given the timeframe of the challenge, I was not able to overcome some challenges in the unit testing section.   

*If applicable, I explain my reasons for choosing python despite its setbacks in the lemus_doc.md file. I would also love the chance to explain them further in an interview :)*

In the future, I would hope to improve my understanding of the use of command line arguments in unit tests in order to perform thorough testing.

