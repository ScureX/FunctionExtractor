import os
import re
from fnmatch import fnmatch

root = ''
pattern = "*"

scriptPaths = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            scriptPaths.append(os.path.join(path, name))

print(str(len(scriptPaths)) + " Files found")

#####

def filter(method, filMeth):
    method = str(method)[2:]
    parIndex = method.find('(')

    dots = []
    currDotIndex = None
    while (currDotIndex == None or currDotIndex > 0):
        shortenedMethod = method[sum(dots):]
        currDotIndex = str(shortenedMethod).find('.')
        if(currDotIndex != 0):
            dots.append(currDotIndex)
        else:
            break

    remove = sum(dots)
    if(remove != -1):
        a = str(method)[sum(dots) : - (len(method) - parIndex)]
    else:
        a = str(method)[:-(len(method) - parIndex)]
    
    if not any(a in s for s in filMeth):
        return a
    else:
        return None

#####

count = 1
allMethodsFiltered = []
for path in scriptPaths:
    print("file: " + str(count))
    f = open(path, 'r')
    # check each line 
    lines = f.readlines()
    methods = []
    for line in lines:
        methods.append(re.findall("([a-zA-Z_.0-9]+\((\)|[ a-zA-Z_0-9.,\"\'/\\<>${=}!()\[\]+\-*]+\)))", line)) # ([a-zA-Z_.0-9]+\((\)|[ a-zA-Z_0-9.,"'/\\<>${}=!()\[\]+\-*]+\)))
    
    methods = [ele for ele in methods if ele != []] # remove empty
    # sort alphabetically

    filteredMethods = []

    # filter
    for method in methods:
        x = filter(method, allMethodsFiltered)
        if(x != None):
            filteredMethods.append(x)
    
    allMethodsFiltered.extend(filteredMethods)
    count += 1

#####
print("append")
allMethodsFiltered = list(sorted(allMethodsFiltered))
# appending
for e in allMethodsFiltered:
    outfile = open("outFiltered.txt", 'a')
    outfile.writelines(str(e)[1:]+ "\n")



  
