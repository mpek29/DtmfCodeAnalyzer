def function_u(i,t):
    return np.sin(t*w[(i)%7]*2*np.pi+(i//7)*np.pi/2)

def createOrthonormalBasis(sample_rate,signal_freq):
    u = []
    t_ech=np.linspace(0.0,1.0,fs) # intervalle d'echantillonnage
    for i in range(14):
        u.append(np.array(function_u(i,t_ech)))
    return u