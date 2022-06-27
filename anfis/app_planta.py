import pickle
import numpy
import anfis

#teste do ANFISObj fora da planta

sets = []
sets = numpy.array([[0,0]])

with open ('funcao_treinada.pkl', 'rb') as inp:
     anf = pickle.load(inp)



while True:

     setpoint = (float(input('Setpoint:')))/225
     erro = (float(input('erro: ')))/140
     sets = numpy.array([[setpoint, erro]])
     y_saida = (anfis.predict(anf, sets))*255
     print(y_saida)



