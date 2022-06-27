import matplotlib.pyplot as plt 
import numpy as np 


neuro1 = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/planta_neuro/planta_neuro1.txt", usecols=[0,1])
neuro2 = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/planta_neuro/planta_neuro2.txt", usecols=[0,1])
neuro3 = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/planta_neuro/planta_neuro3.txt", usecols=[0,1])
neuro4 = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/planta_neuro/planta_neuro4.txt", usecols=[0,1])
neuro5 = np.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/planta_neuro/planta_neuro5.txt", usecols=[0,1])


x1 = neuro1[:,0]
y1 = neuro1[:,1]
x2 = neuro2[:,0]
y2 = neuro2[:,1]
x3 = neuro3[:,0]
y3 = neuro3[:,1]
x4 = neuro4[:,0]
y4 = neuro4[:,1]
x5 = neuro5[:,0]
y5 = neuro5[:,1]
xdeg = np.arange(0,81)
deg = (xdeg>=0)*150


xmean = []
ymean = []

for i in range (len(x1)):
    xmean.append((x1[i] + x2[i] + x3[i] +x4[i] + x5[i])/5)
    ymean.append((y1[i] + y2[i] + y3[i] +y4[i] + y5[i])/5)

plt.plot(x1, y1, color='r',alpha = 0.3, label = "Resultados medidos") 
plt.plot(x2, y2, color='r',alpha = 0.3) 
plt.plot(x3, y3, color='r',alpha = 0.3) 
plt.plot(x4, y4, color='r',alpha = 0.3) 
plt.plot(x5, y5, color='r',alpha = 0.3) 
plt.plot(xmean, ymean, color='c', linewidth = 2.5, label = "Média dos valores medidos")
plt.plot(xdeg, deg, color='g', label = "Setpoint 150mm") 

plt.xlabel("Tempo (s)", fontsize = 13) 
plt.ylabel("Altura (mm)", fontsize = 13) 
plt.title("Resposta do controlador Neuro-Fuzzy") 
plt.legend(fontsize = 20) 
plt.grid()
plt.show() 

# for i in range (len(xmean)):
#  with open('arquivonf.txt','a') as arquivo:
#          arquivo.write(str(xmean[i]) + " " + str(ymean[i]) + "\n")

