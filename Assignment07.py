#---------------------------------------------------------------
# Title: Assignment07
# Developer: Thivanka Samaranayake
# Date June01  2020
# Changelog:
#   Thivanka, June01 2020, Created Pickling Script
#   Thivanka, June02 2020, Created Exception Handling Script
#---------------------------------------------------------------

# How Pickling Works
# https://www.youtube.com/watch?v=2Tw39kZIbhs
import pickle # This imports code from another code file!

example_data = {"Key": "1", "Name": "Frodo", "Title": "Ring Bearer", "Importance": "High"} # Set of data to be pickled

pickle_out = open("dict.pickle", "wb") # creating a binary file to pickle data
pickle.dump(example_data, pickle_out) # pickling data
pickle_out.close() # closing binary file

pickle_in = open("dict.pickle", "rb") # opening binary filed with pickled data
list_of_dic = pickle.load(pickle_in) # unpickling data from binary file

print(example_data) # printing pickled data
print(example_data["Key"]+","+example_data["Name"]) # Still acting like a dictionary

# How Exceptions Work
# https://www.youtube.com/watch?v=NIWwJbo-9_8
class CapitalizationError(Exception):
    """The first letter not capitalized in file name error"""
    def __str__(self):
        return "Please capitalize the t in test"

try:
    docfile = input("Please provide the name of the file you want to open: ")
    file = open(docfile)
    if file.name == "test.txt":
        raise CapitalizationError
except FileNotFoundError as e:
    print("This file does not exist")
    #print(e)
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()
finally:
    pass
