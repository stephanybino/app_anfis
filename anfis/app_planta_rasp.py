import pickle
import numpy
import anfis
import matplotlib.pyplot as plt
import serial
import time


#inicia e limpa serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.flush()

#instanciando as listas de variaveis 

dados_enviar = []
y = []
tempo = []
plot_final = False
sets = []
sets = numpy.array([[0,0]])

with open ('funcao_treinada.pkl', 'rb') as inp:
    anf = pickle.load(inp)

#loop q espera o nivel ser enviado e seta reset e parada
while(setpoint == 0):
        msg_recebida = ser.readline().decode('utf-8').rstrip()
        if msg_recebida != '':
                nivel_recebido =float(msg_recebida)
                print(nivel_recebido)
        escrito = input("setpoint: ")
        try:
                setpoint = (int(escrito))/225  #sempre um valor entre 90 e 225
        except:
                if escrito == 'r':
                        ser.write([7,255,3])
                elif escrito == 'p':
                        ser.write([7,0,0])


nivel_recebido = setpoint + 0
#loop do controlador
while True:
        msg_recebida = ser.readline().decode('utf-8').rstrip()
        if msg_recebida != '':
                nivel_recebido =float(msg_recebida)
                y += [nivel_recebido]
                if tempo == []:
                        start_time = time.time()
                        tempo = [0.0]
                else:
                        tempo += [(time.time()-start_time)]

 #calculo do erro       
        erro = (float(setpoint-nivel_recebido))/150

#def vetor a ser inserido no treinamento
        sets = numpy.array([[setpoint, erro]])

#def resposta e limites de resposta
        pwm = (anfis.predict(anf, sets))*255
        if  pwm > 40:
                modo = 1
                plot_final = False

        elif pwm <-40:
                pwm = -pwm
                modo = 2
                plot_final = False
        else:
                modo = 0
                pwm = 0
                if plot_final == False:
                        plot_final = True
                        tempo_plot = time.time()
        
        if pwm > 255:
                        pwm = 255

#prepara vetor para ser enviado e envia via serial
        dados_enviar = [[7,pwm,modo]]
        # print(dados_enviar)
        # print(erro)
        ser.write(dados_enviar)

        #plot da resposta da planta
        if (plot_final == True):
                if (time.time() - tempo_plot)>20.0:
                        break
        
        time.sleep(0.1)

plt.plot(tempo,y)
plt.grid()
plt.show()





