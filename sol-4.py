# Ex-4
# Extract filenames that has txt as extension
# filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']

# sol:
def getFileNames(fileNames, extention):
    outputFileNames = []
    for fileName in fileNames:
        fileExt = fileName.split(".")[-1]
        if fileExt == extention:
            outputFileNames.append(fileName)
    return outputFileNames

if __name__ == "__main__":
    filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']
    print (getFileNames(filenames, 'txt'))