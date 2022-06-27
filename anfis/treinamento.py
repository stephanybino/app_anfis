import anfis
import membership.mfDerivs
import membership.membershipfunction
import numpy
import pickle

#importa dados 
ts = numpy.loadtxt("/home/labsea9/Documents/tcc_stephany/anfis-master/anfis/dataset_novo.txt", usecols=[0,1,2])
X = ts[:,0:2]

# normalização dos valores
X[:,0] = X[:,0]/225. 
X[:,1] = X[:,1]/150.
Y = ts[:,2]/255.

#definição dos universos de discurso
mf = [[['sigmf',{'b':0.2,'c':-40.}],['gaussmf',{'mean':0.35,'sigma':0.12}],['gaussmf',{'mean':0.65,'sigma':0.12}],['sigmf',{'b':0.8,'c':40.}]],
            [['sigmf',{'b':0.2,'c':-40.}],['gaussmf',{'mean':0.35,'sigma':0.12}],['gaussmf',{'mean':0.65,'sigma':0.12}],['sigmf',{'b':0.8,'c':40.}]]]


#criação do ANFISObj
mfc = membership.membershipfunction.MemFuncs(mf)
anf = anfis.ANFIS(X, Y, mfc)

#método de treinamento
anf.trainHybridJangOffLine(epochs=70)

#salvando o ANFISObj para aplicação
with open ('funcao_treinada.pkl','wb') as outp:
    pickle.dump(anf, outp, pickle.HIGHEST_PROTOCOL)

#plot dos erros, da comparação treinadaxoriginal e funções de pertinência
print("Plotting errors")
anf.plotErrors()
print("Plotting results")
anf.plotResults()
print("Plotting members functions")
anf.plotMF(X[:,0],0) 
anf.plotMF(numpy.unique(X[:,1]),1)

