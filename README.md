# Postscript Interpreter in Python <br>

There are two files for this interpreter:
- **the 'test_psip.py' that contains 47 test functions for the application in regards to most of the operation functions implemented and can be run with pytest using 'pytest test_psip.py'**
- **The 'psip.py' that contains the logic and function implementations for the entire interpreter**

The program is run by simply running the 'psip.py' file with 'python psip.py'. It was developed and tested by running the file(s) in the VSCode IDE and the Windows terminal. It uses the python 'math' and 'logging' libraries for dependencies, if necessary. From here, enter input one at a time (ie 1, 2, add). It supports commands from the 7 major command groups (Stack Manipulation, Arithmetic, Boolean, Dictionary, String, Flow Control, IO). All default operations implemented are displayed in the 'psip.py' file and the Canvas assignment page for default Postscript commands. 

Switching between Dynamic and Lexical scoping is done by entering 'dynamic' or 'lexical' when the interpreter is running. It will print the switch to console when entered. The interpreter uses Dynamic Scoping by default and has mostly implemented the Lexical scoping logic with working subfunctions.  

The following is a [Demonstration Video](https://www.youtube.com/watch?v=PmjZfmeQtyM) that demonstrates most of the function capability, how to run the interpreter (and test cases), and how to switch between Dynamic and Lexical scoping. 
