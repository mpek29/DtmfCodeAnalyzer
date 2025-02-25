def scalarProduct(u,v):
    return 2*integrale(np.multiply(u,v))

def coordonnees(u,v):
    c = []
    for i in range(len(u)):
        c.append(scalarProduct(u[i],v))
    return c

def projectionOrt(u,v):
    c = coordonnees(u,v)
    p = np.zeros_like(v)
    for i in range(len(u)):
        p += c[i]*u[i]
    return [c,p]