def findingMainFrequencies(c):
    c_processing = c.copy()
    m1 = max(c_processing, key=abs)
    i1 = c.index(m1)

    #remove the largest number using its index
    c_processing.pop(i1)

    m2 = max(c_processing, key=abs)
    i2 = c.index(m2)
    return [i1,i2,m1,m2]