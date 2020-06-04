# Using Python’s Exception Handling and Picking Capabilities

*Thivanka, June02 2020*

## Introduction
This assignment delves into error handling and pickling of data. Error handling involves the use of try-exception blocks to catch errors that the user might run into as they proceed through the program. Data pickling involves the creation of a binary file to add and read data from it. These two concepts were tested using simple programs in this module. 

## Benefits of Built In Python Commands
Python has many built in commands that can be used in functions. They provide ways of building in logic or getting additional information to a program. For example, the len() command returns the length of an object. This enables the user to easily call the length of an object—an important piece of information—into a function.

## Benefits of Structured Error Handling
Structured error handling provides a way to fix issues that are caused by the user of the program. These types of errors can be anticipated ahead of time to allow for the code to run smoothly. Structured error handling allows the programmer to customize how the program handles errors as opposed to letting Python handle them. There are several ways that errors can be managed within a program. One method is through try-except blocks. Another method is through the Exception class.

## Text File vs Binary File
Data can be saved in binary format in Python. Unlike a text file where information can be read by a human, a binary file saves data with a series of bits where some parts of the file can be read as a text file. However, overall a binary file can only be read by the computer. Pickling is one method of storing data in this way. Pickling involves the serialization of data to be extracted (unpickled) later. Serialization of data reduces the amount of memory needed to save the data. In figure 1, text data is pickeled and unpickled using the pickling commands in Python.

```
import pickle # This imports code from another code file!

example_data = {"Key": "1", "Name": "Frodo", "Title": "Ring Bearer", "Importance": "High"} # Set of data to be pickled

pickle_out = open("dict.pickle", "wb") # creating a binary file to pickle data
pickle.dump(example_data, pickle_out) # pickling data
pickle_out.close() # closing binary file

pickle_in = open("dict.pickle", "rb") # opening binary filed with pickled data
list_of_dic = pickle.load(pickle_in) # unpickling data from binary file

print(example_data) # printing pickled data
print(example_data["Key"]+","+example_data["Name"]) # Still acting like a dictionary
```
![Figure01--Pickling Data](https://github.com/THIVASAM/IntroToProg-Python-Mod07/blob/master/docs/Figure1.png "Figure01--Pickling Data")
### Figure01--Pickling Data

## Exception Class
Exception class is a built in class within Python that can be programmed to handle errors. Python automatically creates an Exception object when an error occurs with information about the error. This information can be captured and stored in a try-except block to read out the error message. Custom exception classes can be created in Python as well. The Exception class is a base class that can be used to create a derived class where the inherit data in the function can be replaced with a customized message. You derive a new class from the Exception class by replacing the def__str__(self) with a custom message. These types of custom classes are created when there is a specific error in the program that you want to capture that is not built into Python.

## Markdown Language and GitHub
Markdown languages allow you to take information and convert into code through the use of special syntax. In the case of GitHub markdown language, the code is converted into static HTML page using a conversion processing application called Jekyll. The advantage of a markdown language is its ability to easily read and write it using plain text. GitHub has custom functionality to create webpages using a GitHub flavored markdown language. It is created by using markdown commands in an index file. More information about this can be found in this website:
https://help.github.com/en/github/writing-on-github/about-writing-and-formatting-on-github

## Assignment07
The code shown in the following figures demonstrates pickling data and error handling.

![Figure02--Pickling and Un-Pickling Data in a Dictionary](https://github.com/THIVASAM/IntroToProg-Python-Mod07/blob/master/docs/Figure2.png "Figure02--Pickling and Un-Pickling Data in a Dictionary")
### Figure02--Pickling and Un-Pickling Data in a Dictionary

![Figure03--Example of Custom Error With Capitalization of Document Name](https://github.com/THIVASAM/IntroToProg-Python-Mod07/blob/master/docs/Figure3.png "Example of Custom Error With Capitalization of Document Name")
### Figure03--Example of Custom Error With Capitalization of Document Name

## Conclusion
This module was learning about pickling and error handling. I learned about the difference between a text file and a binary file and how pickling helps “flatten” out a file to conserve space. I also learned about the benefits of putting built in Python commands into function and the benefits of structured error handling. Finally, this module also focused on building a more complex GitHub webpage for presentation purposes.
