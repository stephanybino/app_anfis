#define T1_A 8 //Solenoide - Alto - Tanque 1
#define T1_B 7 //Solenoide - Baixo - Tanque 1

#define T2_A 4 //Solenoide - Alto - Tanque 2
#define T2_B 5 //Solenoide - Baixo - Tanque 2

#define T3_A 3 //Solenoide - Alto - Tanque 3
#define T3_B 2 //Solenoide - Baixo - Tanque 3

#define M_S 6 //Solenoide da saida do motor

#define BOMBA 9 //PWM da BOMBA
#define COMANDO_BOMBA 10 //Direção da Bomba

#define NIVEL A0   //Sensor de Pressão diferencial para medir nível do Tanque 2
#define T1_MIN 15  //Sensor Nivel Mínimo Tanque 1
#define T1_MAX 16  //Sensor Nivel Mínimo Tanque 1
#define T2_MIN 17  //Sensor Nivel Mínimo Tanque 2
#define T2_MAX 18  //Sensor Nivel Mínimo Tanque 2
#define T3_MIN 11  //Sensor Nivel Mínimo Tanque 3
#define T3_MAX 12  //Sensor Nivel Mínimo Tanque 3

int POT = 255,
    modo = 0,
    pressao = 0;

bool T1_NIVEL_MIN = 0,
     T1_NIVEL_MAX = 0,
     T2_NIVEL_MIN = 0,
     T2_NIVEL_MAX = 0,
     T3_NIVEL_MIN = 0,
     T3_NIVEL_MAX = 0;
     
float  nivel = 0;

//modos
// 0 - Desligado  
// 1 - Encher o tanque 2 com o tanque 1
// 2 - Encher o tanque 2 com o tanque 3
// 3 - Encher o tanque 1 com o tanque 2
// 4 - Encher o tanque 3 com o tanque 2


void setup() {
  pinMode(T1_A, OUTPUT);
  pinMode(T1_B, OUTPUT);
  pinMode(T2_A, OUTPUT);
  pinMode(T2_B, OUTPUT);
  pinMode(T3_A, OUTPUT);
  pinMode(T3_B, OUTPUT);
  pinMode(M_S, OUTPUT);
  pinMode(BOMBA, OUTPUT);
  pinMode(COMANDO_BOMBA, OUTPUT);

  pinMode(NIVEL, INPUT);
  pinMode(T1_MIN, INPUT);
  pinMode(T1_MAX, INPUT);
  pinMode(T2_MIN, INPUT);
  pinMode(T2_MAX, INPUT);
  pinMode(T3_MIN, INPUT);
  pinMode(T3_MAX, INPUT);

  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    // read the incoming byte:
           modo = Serial.read() - 48;
  }
  switch (modo) {
    case 0:   
      {
        solenoides(1, 1, 1, 1, 1, 1, 1);
        analogWrite(BOMBA, 0);
        break;
      }
    case 1:
      {
        encher_T2_com_T1();
        break;
      }
    case 2:
      {
        encher_T2_com_T3();
        break;
      }
    case 3:
      {
        encher_T1_com_T2();
        break;
      }
    case 4:
      {
        encher_T3_com_T2();
        break;
      }
    default:
      {
        modo = 0;
      }

  }
  
  pressao = analogRead(NIVEL);
  T1_NIVEL_MIN = digitalRead(T1_MIN);
  T1_NIVEL_MAX = digitalRead(T1_MAX);
  T2_NIVEL_MIN = digitalRead(T2_MIN);
  T2_NIVEL_MAX = digitalRead(T2_MAX);
  T3_NIVEL_MIN = digitalRead(T3_MIN);
  T3_NIVEL_MAX = digitalRead(T3_MAX);
  
  nivel = 0.25*pressao + 79.89;

  
Serial.print("Nivel T2 = ");
  Serial.print(nivel);
  Serial.print(" ");
  
  Serial.print("MIN T1 = ");
  Serial.print(T1_NIVEL_MIN);
  Serial.print("  ");

  Serial.print("MAX T1 = ");
  Serial.print(T1_NIVEL_MAX);
  Serial.print("  ");

  Serial.print("MIN T2 = ");
  Serial.print(T2_NIVEL_MIN);
  Serial.print("  ");

  Serial.print("MAX T2 = ");
  Serial.print(T2_NIVEL_MAX);
  Serial.print("  ");

  Serial.print("MIN T3 = ");
  Serial.print(T3_NIVEL_MIN);
  Serial.print("  ");

  Serial.print("MAX T3 = ");
  Serial.print(T3_NIVEL_MAX);
  Serial.println("  ");
  
  
  delay(100);
}


void solenoides(int Tanque_1_A,  int Tanque_1_B, int Tanque_2_A, int Tanque_2_B, int Tanque_3_A, int Tanque_3_B, int Saida_Bomba) {
  digitalWrite(T1_A, Tanque_1_A);
  digitalWrite(T1_B, Tanque_1_B);
  digitalWrite(T2_A, Tanque_2_A);
  digitalWrite(T2_B, Tanque_2_B);
  digitalWrite(T3_A, Tanque_3_A);
  digitalWrite(T3_B, Tanque_3_B);
  digitalWrite(M_S, Saida_Bomba);
}

void encher_T2_com_T1() {
  solenoides(1, 0, 0, 1, 1, 1, 0);
  analogWrite(BOMBA, POT);
}

void encher_T2_com_T3() {
  solenoides(1, 1, 0, 1, 1, 0, 0);
  analogWrite(BOMBA, POT);
}

void encher_T1_com_T2() {
  solenoides(0, 1, 1, 0, 1, 1, 0);
  analogWrite(BOMBA, POT);
}

void encher_T3_com_T2() {
  solenoides(1, 1, 1, 0, 0, 1, 0);
  analogWrite(BOMBA, POT);
}
