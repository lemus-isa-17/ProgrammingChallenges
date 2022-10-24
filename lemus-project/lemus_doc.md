#CSV Project Notes
###*Because I'm tired of using Google Docs*

##Initial Thoughts, Planning
Reviewing my tools. Which language and software to use.
- Use Java, most comfortable and cuts down on prep work. Use Python, easier for the barebones, allows more time to for details
- Review GitHub basics
- VSCode, Eclipse...
*Keep in mind*
Program should be able to handle **more than two inputs**, inputs with **different columns**, and **very large (> 2GB) files** gracefully.

##Breaking down the project
    1. Read a CSV file
        - https://earthly.dev/blog/csv-python/
    2. Create/Write to a CSV file
        - https://www.pythontutorial.net/python-basics/python-write-csv-file/
        - https://www.codingem.com/python-write-to-csv-file/
    3. Command line arguments
        - https://www.geeksforgeeks.org/command-line-arguments-in-python/?id=discuss  
    4. Read files from command line
    5. Create new CSV file, combine new info with input file info
        - Extract file names
        - Create headers
        - Store? or Pass on original info
    6. Put it all together
*Testing along the way!*

##Learning along the way
Drawback of python is that I'm sacrificing some good coding practice for functionality.
- A class will help with reusability and encapsulation, a focus for the project
    - Learning how to construct a class, call methods
- Method vs Function
    - Method cannot be called independently, must operate on an object, an instance of the class
    - Function can be called independently
        - https://www.geeksforgeeks.org/difference-method-function-python/ 
    - Debugging from the command line (pdb)
    - Installing pandas for a clean user result
        - https://www.w3schools.com/python/pandas/default.asp

##Handling data, creating combined CSV
Storing data from each file or creating new file as it is read.
    - Speed/Functionality
    - Storage

##Best Practices
https://www.w3schools.com/python/default.asp 
https://realpython.com/python-return-statement/#using-the-python-return-statement-best-practices 
Deciding how to refactor as I went.
Worked in main method, made new methods out of processes I used in main.
Discerning where best to have variables, local or global.

##Testing and Debugging
- https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/ 


###Links used
[Markdown Guide](https://www.markdownguide.org/basic-syntax/)

**Do your best. You decide your best.**