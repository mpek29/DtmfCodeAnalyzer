def integrale(w):
    dt = (1/(len(w)-1))
    sum_w = 0
    for i in range(len(w)-1):
        sum_w += w[i]

    return sum_w*dt