# CSV Project Notes

## Initial Thoughts, Planning  

Reviewing my tools. Which language/software to use?  
- Using Java is most comfortable and cuts down on prep work. Use Python is easier to read/write the CSVs, allows more time to focus on the details of the project.
- Review GitHub basics.
- VSCode or Eclipse   
*Keep in mind* :
Program should be able to handle **more than two inputs**, inputs with **different columns**, and **very large (> 2GB) files** gracefully.

## Breaking down the project  

1. Read a CSV file  
2. Create/Write to a CSV file  
3. Read/utilize command line arguments  
4. Create new CSV file, combine new info with input file info  
    - Extract file names
    - Create headers
    - Order original info
    - Pass on original info with added column
5. Put it all together   

Links used :   
- https://earthly.dev/blog/csv-python/
- https://www.pythontutorial.net/python-basics/python-write-csv-file/
- https://www.codingem.com/python-write-to-csv-file/
- https://www.geeksforgeeks.org/command-line-arguments-in-python/?id=discuss     

*Test along the way!*

## Learning curves

Since I am fairly new to python, there were some things I had to learn as they arose.  
- A class will help with reusability and encapsulation, a focus for the project
    - Learning how to construct a class and call methods in python 
- Method vs Function
    - Method cannot be called independently, must operate on an object, an instance of the class.
    - Function can be called independently.
    - Debugging from the command line (pdb).
    - Installing pandas for a clean user result.
- Best practices for return statements

Links used:   
- https://www.w3schools.com/python/default.asp
- https://www.geeksforgeeks.org/difference-method-function-python/
- https://www.w3schools.com/python/pandas/default.asp
- https://realpython.com/python-return-statement/#using-the-python-return-statement-best-practices   

## Testing and Debugging

- I was not able to complete testing due to problems with command line arguments. 
- Testing of the program was completed along the way with print statements and debugging to create a working final program, though unit tests were not achievable.  

Links used:   
- https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/   

## Successes and Challenges

- I am proud that I was able to:
    - Read, write and combine the CSV files.
    - Learn more about python, a language with which I had little prior experience.
    - Use command line arguments in my program.
    - Refactor my program as best I could along the way. Although I had to sacrifice some good coding practices due to my lack of familiarity, I was still able to write clean code. I felt my use of classes and methods allowed my code to be reusable as well.
- In the future, I would like to improve:
    - The ability of the program to handle large files. Of all the criteria, this is the one I felt most short of. While it can process the files in a relatively quick amount of time, the resulting CSV is not always fully visible in the terminal.
        - I would further research the processing of input CSV files. This could have an effect on the storage and processing speed of the program. 
    - Testing. I was unable to complete the unit test requirements of this project. While I did simple tests along the way to create a working project, I was not able to create working unit tests. Passing command line arguments to the CSVCombiner objects I initiated in the testing class proved to be a challenge I was not able to overcome given the timeframe of the project.


#### Links used for documentation file :

[Markdown Guide](https://www.markdownguide.org/basic-syntax/)