# rankwatch17_py_csvbreakdown
read a csv file from one directory and write the text to anther csv file in another director
### requirements libraries
* import csv
it is used to perform differet operation in csv files
* import glob
If you need a list of filenames that all have a certain extension, prefix, or any common string in the middle, use glob instead of writing code to scan the directory contents yourself.
* import os 
The OS module in Python provides a way of using operating system dependent
functionality. 

The functions that the OS module provides allows you to interface with the
underlying operating system that Python is running on – be that Windows, Mac or
Linux. 

first it reads to csv file using glob from current directory. to get the path of current directory:
* current_directory_path = os.getcwd()
it returns current directory path

To run the program file go to the cmd and change the directory according to directory of file. 
#### command to change the directory
* cd <directory_path>
#### command to run the file
* python <file_name.py> 

