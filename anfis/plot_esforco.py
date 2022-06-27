import matplotlib.pyplot as plt 
import numpy as np 


pid = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/esforco_pid.txt", usecols=[0,1])
nf = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/esforco_neuro.txt", usecols=[0,1])



# x1 = pid[:,0]
y1 = pid[:,1]
# x2 = nf[:,0]
y2 = nf[:,1]

x1 = np.arange(0,61)
x2 = np.arange(0,52)
plt.plot(x1, y1, color='r', label = "Esforço de controle PID") 
plt.plot(x2, y2, color='c', label = "Esforço de controle Neuro-Fuzzy")



plt.xlabel("Tempo (s)", fontsize = 13) 
plt.ylabel("PWM", fontsize = 13) 
plt.title("Esforço de controle") 
plt.legend(fontsize = 20) 
plt.grid()
plt.show() 
