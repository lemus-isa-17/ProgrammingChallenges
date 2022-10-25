# CSV Project Notes

## Initial Thoughts, Planning  

Review my tools. Which language/software should I use?  
- I am most familiar with Java, which would cut down on prep work and issues due to gaps in knowledge. Using Python is easier to read/write the CSVs, which would allow more time to focus on the later intricacies of the project.
- Review GitHub basics.
- VSCode or Eclipse?       

*Keep in mind* :
Program should be able to handle **more than two inputs**, inputs with **different columns**, and **very large (> 2GB) files** gracefully.

## Breaking down the project  

Approaching the problem in manageable steps.   
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
- Creation and construction of a class and methods in python
- Method vs Function
    - Method cannot be called independently, must operate on an object, an instance of the class.
    - Function can be called independently.
- Debugging from the command line (pdb).
- Installing pandas for a clean user result.
- Best practices and available libraries as well as minor variance (from Java) in implementation and utilization of methods.   

Links used:   
- https://www.w3schools.com/python/default.asp
- https://www.geeksforgeeks.org/difference-method-function-python/
- https://www.w3schools.com/python/pandas/default.asp
- https://realpython.com/python-return-statement/#using-the-python-return-statement-best-practices   

## Testing and Debugging
I was not able to complete unit testing due to problems with command line arguments. 
- Minor testing of the program was performed with print statements and debugging to create a working final program.

Links used:   
- https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/   

## Successes and Improvements

- I was successfully able to:
    - Learn more about python, a language with which I had very little prior experience.
    - Read, write and combine CSV files.
    - Use command line arguments.
    - Refactor my program to the best of my ability. Although I had to sacrifice some good coding practices due to my lack of familiarity, I was still able to write clean code. I felt my use of classes and methods allowed my code to be reusable as well.
- In the future, I would like to improve:
    - The ability of the program to handle large files. Of all the criteria, this is the one I felt most short of acieving. While it can process large files in a relatively quick amount of time, the resulting CSV is not always fully visible in the terminal.
        - I would further research the processing of input CSV files. This could have an effect on the storage and processing speed of the program. 
    - Testing. I was unable to complete the unit test requirements of this project. While I did simple tests along the way to create a working project, I was not able to create working unit tests. Passing command line arguments to the CSVCombiner objects I initiated in the testing class proved to be a challenge I was not able to overcome given the timeframe of the project.


#### Links used for documentation file :

[Markdown Guide](https://www.markdownguide.org/basic-syntax/)