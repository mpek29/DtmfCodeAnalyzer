def getCodeFromFile(filename):
    file = open(filename, "rb")
    code_recover=np.load(file)
    file.close()
    return code_recover