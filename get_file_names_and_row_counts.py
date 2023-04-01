import os
#import pandas as pd
import sys
import re

path ="XX"
#we will store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
  for file in files:
    path = os.path.join(root, file)
    #size = (os.stat(path).st_size) # in bytes
    filelist.append(path)
        #append the file name to the list
    # filelist.append(os.path.join(root,file))
print(filelist)
# #print all the file names
# for name in filelist:
#     print(name)

#get count of file if xlsx - modify list to print that out
#get index of all items in filelist based on key substrings (for now not checking counts for each file)
xlsxlist = []
needs_count = ['DATA', 'xlsx', 'final']

for file in filelist:
  if all(substring.lower() in file.lower() for substring in needs_count):
    xlsxlist.append(file)

print(xlsxlist)

original_stdout = sys.stdout # Save a reference to the original standard output

#create file, modify output, and save modified output.
with open('XX', 'w') as f:
  sys.stdout =f
  for name in filelist:
    if name in xlsxlist:
      number_records =(len(pd.read_excel(name))-1)
      print(f"{name}, number of records: {number_records}")
    else:
      print(name)
  sys.stdout = original_stdout
