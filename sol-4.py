# Ex-4
# Extract filenames that has txt as extension
# filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']

# sol:
def getFileNames(fileNames, extention):
    return [fileName for fileName in fileNames if fileName.endswith(extention)]

if __name__ == "__main__":
    filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']
    print (getFileNames(filenames, 'txt'))