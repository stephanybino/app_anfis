import serial
import time
import matplotlib.pyplot as mp
#inicia e limpa serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.flush()
#constantes pid
kp = 5
ki = 0.1
kd = 0.01
integral = 0
deriv = 0
last_erro = 0
#inicialização das listas 
dados_enviar = []
y = []
tempo = []
plot_final = False

setpoint = 0
#loop q espera o nivel ser enviado e seta reset e parada
while(setpoint == 0):
        msg_recebida = ser.readline().decode('utf-8').rstrip()
        if msg_recebida != '':
                nivel_recebido =float(msg_recebida)
                print(nivel_recebido)
        escrito = input("setpoint: ")
        try:
                setpoint = int(escrito)
        except:
                if escrito == 'r':
                        ser.write([7,255,3])
                elif escrito == 'p':
                        ser.write([7,0,0])
        ser.flush()

nivel_recebido = setpoint + 0
#loop do controlador
while(1):
        msg_recebida = ser.readline().decode('utf-8').rstrip()
        if msg_recebida != '':
                nivel_recebido =float(msg_recebida)
                y += [nivel_recebido]
                if tempo == []:
                        start_time = time.time()
                        tempo = [0.0]
                else:
                        tempo += [(time.time()-start_time)]
        else:
                print('Ação iniciada')
        print(nivel_recebido)
 #calculo dos erros       
        erro = float(setpoint-nivel_recebido)
        last_erro = erro
        integral += erro
        deriv = last_erro-erro
        
        if integral > 255:
                integral = 255
        if deriv > 255:
                deriv = 255
      #controlador          
        pwm = int(erro*kp+integral*ki+deriv*kd)
        #limites e defs
        if  pwm > 35:
            modo = 1
            plot_final = False
        elif pwm <-35:
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
        #def envio         
        dados_enviar = [7,pwm,modo]
        print(dados_enviar)
        print(erro)
        ser.write(dados_enviar)
        #plot da planta
        if (plot_final == True):
                if (time.time() - tempo_plot)>30.0:
                        break
        
        time.sleep(0.1)
#for i in range(len(tempo)):
 #      with open('planta_pid5.txt','a') as arquivo:
  #             arquivo.write(str(tempo[i])+"  "+str(y[i])+"\n")
               
mp.plot(tempo,y)
mp.grid()
mp.show()

	

