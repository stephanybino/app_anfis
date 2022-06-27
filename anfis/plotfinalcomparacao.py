import matplotlib.pyplot as plt 
import numpy as np 
from pylab import *


pid = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/arquivopid.txt", usecols=[0,1])
nf = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/arquivonf.txt", usecols=[0,1])



x1 = pid[:,0]
y1 = pid[:,1]
x2 = nf[:,0]
y2 = nf[:,1]
xdeg = np.arange(0,81)
deg = (xdeg>=0)*150



plt.plot(xdeg, deg, color='g', label = "Setpoint 150mm") 
plt.plot(x1, y1, color='r', label = "Controlador PID") 
plt.plot(x2, y2, color='c', label = "Controlador Neuro-Fuzzy")




plt.xlabel("Tempo (s)", fontsize = 13) 
plt.ylabel("Altura (mm)", fontsize = 13) 
plt.title("Comparação dos controladores") 
plt.legend(fontsize = 20) 
plt.grid()
plt.show() 
