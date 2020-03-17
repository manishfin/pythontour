# Ex-5
# Extract filenames that has txt as extension
# filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']

# sol:
def getFileNames(fileNames, extention):
    files = []
    for fileName in fileNames:
        fileExt = fileName.split(".")[-1]
        if fileExt == extention:
            files.append(fileName)
    return files

if __name__ == "__main__":
    filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']
    print (getFileNames(filenames, 'txt'))