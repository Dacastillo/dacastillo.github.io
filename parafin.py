# -*- coding: utf-8 -*- Librerías de Python
#Pendientes punto del Newport, temperatura del Lakeshore, tiempo, val
import sys
import os
from time import time
import visa
rm = visa.ResourceManager('@py')
rm.list_resources()
('GPIB::16::INSTR','GPIB::12::INSTR','GPIB::8::INSTR','GPIB::10::INSTR')
k2 = rm.open_resource('GPIB::16::INSTR') #keithley
dev12 = rm.open_resource('GPIB::12::INSTR',) #lakeshore
dev8 = rm.open_resource('GPIB::8::INSTR') #lockin
dev10 = rm.open_resource('GPIB::10::INSTR')#newport
k2.read_termination='\r\n'
k2.write_termination='\r\n'
file = open('dat.csv', mode='w')

def val(data):
    y=0
    nst=""
    dlist = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in data:
        for i in dlist:
            if x == i:
                nst=nst+x
    n=len(nst)
    dcont=n
    acum=0
    for z in range(n):
        y=0
        for i in dlist:
            if nst[z] == i:
                d=y
                mult=1
                dcont=dcont-1
                for j in range(dcont):
                    mult=mult*10
                acum=acum+(d*mult)
            y=y+1

    return acum

def NewPort()
PolarizatorNew = val(Polarizator) + L12 
PolarizatorNew = str(PolarizatorNew) 
PolarizatorNew = str(PolarizatorNew).strip('') 
dev10.query("*wai" + "\n")
dev10.query("move1" + " " + PolarizatorNew + "\n")
dev10.query(dev10%, "*wai" + "\n")
Polarizator = PolarizatorNew

def KeithleyChannel1()
K1.query(":SENS:VOLT:DC:AVER:TCON MOV")
K1.query(":SENS:VOLT:DC:AVER:STAT ON")
K1.query(":SENS:VOLT:DC:AVER:COUN 20")
K1.query(":ROUT:CLOS (@1)") 
K1.query(":SENS:VOLT:DC:AVER:STAT OFF")
K1.query("*wai")

def Keithley()
Ch3$ = "                       "	
K2.query("FETCh?")
K2.read(Ch3$)

def Display()
#keithley
Text1 = str(LCh1 * 1000)
Text2 = str(LCh2)
Text3 = str(LCh3)
Text4 = str(LCh4)
Text5 = str(LCh5 * 1000)
Text6 = str(LCh6 * 1000)
Text7 = str(LCh7)
Text8 = str(LCh8)
Text9 = str(LCh9)
Text10 = str(LCh10)
#lakeshore
Text11 = str(LTempControl)
Text12 = str(LTempSample)
#faraday en grados
Text15 = str(Aux1LCh1)
#faraday en grados, acumulado
Text18 = str(Aux2LCh1)
#tiempo
Tiempo = time()
Label56Caption = str(Tiempo)
#numero de datos
Label58Caption = str(NumDat)



def Keithley2()
Ch1$ = "                       "# asignado a faraday
#Ch2$ = "                       " #vector asignado a baratron 1
#Ch3$ = "                       " #vector asignado a baratron 2
Ch4$ = "                       " #vector asignado a Cañon de Alkanes
#Ch5$ = "                       " #vector asignado a stray light
Ch6$ = "                       " #(reservado para uso futuro)
#Ch7$ = "                       " #(reservado para uso futuro)
#Ch8$ = "                       " #(reservado para uso futuro)
#Ch9$ = "                       " #vector asignado a piranni 1
#Ch10$ = "                       " #vector asignado a piranni 2
K2.query(":SENS:VOLT:DC:AVER:TCON MOV")
K2.query(":SENS:VOLT:DC:AVER:STAT ON")
K2.query(":SENS:VOLT:DC:AVER:COUN 20")
K2.query(":ROUT:CLOS (@2)") #Faraday K2.query(":TRIG:COUN 1")
K2.read("FETCh?")
K2.read(Ch1$)
K2.query(":SENS:VOLT:DC:AVER:STAT OFF")
K2.query("*wai")
K2.query(":ROUT:CLOS (@4)")	#Cañon de Alkanes
K2.query(":TRIG:COUN 1")
K2.query("FETCh?")
K2.read(Ch4$)
K2.query(":ROUT:CLOS (@6)") 
K2.query("FETCh?")
K2.read(Ch6$)

def LockIn()
Ch1 = "                       "
#	vector asignado a faraday
dev8.query("OUTP? 1" + "\n")
dev8.read( Ch1)
C = val(Ch1)
Ch1 =str(C).strip('')
if(C <= 0.0000000001 and C >= -0.0000000001):	#filtro para valores muy pequenos
  SearchChar = "E"	#Search for "E"
  #A binary comparison starting at position 1. Returns 9.
  PosExp = Ch1.find("SearchChar")
  num=Ch1[:11]
  Ch1 = Ch1.strip(num)

def CurrentPos()
#if(GPIB.value = 1):
Pos1$ = "                       "
Pos2$ = "                       "
dev10.query("Pos1?" + "\n")
dev10.read(Pos1)
dev10.query("*wai" + "\n")
dev10.query("Pos2?" + "\n")
dev10.read(Pos2)
Label31Caption = Pos1
Label32Caption = Pos2
PosPol = val(Pos1)
PosAnA = val(Pos2)

def Form_Load()
dev10.query("*wai" + "\n")
dev10.query("VEL1 10.0" + "\n")
dev10.query("*wai" + "\n")
dev10.query("VEL2 10.0" + "\n")
dev10.query("*wai" + "\n")
dev10.query("BACKLASH 0.000,0.000" + "\n")
dev10.query("*wai" + "\n")
K2.query("*CLS")
K2.query("*wai")
K2.query(":CONF:VOLT:DC")
K2.query("*wai")
K2.query(":SENS:VOLT:DC:RANG:UPP 1")
K2.query(":INIT:CONT ON")
#Keithley
K2.query("*wai")
K2.query(":ROUT:MULT:OPEN (@2,4,6)")
#K2.query(":ROUT:MULT:OPEN (@6)")
K2.query("*wai")
K2.query(":SENS:VOLT:DC:AVER:TCON MOV")
K2.query(":SENS:VOLT:DC:AVER:COUN 20")
K2.query(":SENS:VOLT:DC:AVER:STAT ON")
K2.query(":ROUT:CLOS (@2)")
term$ = "\r" + "\n"
BeginEnabled = 0
FinEnabled = 0
opt1 = 2
opt2 = 3
n = 1
kk = 1



def MainLoop()
Start = time.time
FinishAux = time.time()
Keithley2	
LakeShore
Finish = time.time()
if(Finish < Start):
   Start = 86400 - Start
   Finish = Finish + Start
if(FinishAux < StartAux):
   StartAux = 86400 - StartAux
   FinishAux = FinishAux + StartAux
TiempoAux = FinishAux - StartAux
Tiempo = Tiempo + Finish - Start + TiempoAux 
StartAux = time.time()
Conversiones
CurrentPos
NumDat = NumDat + 1
LTempControl = str(LTempControl).strip('')
LimitEnd = str(val(SetPointDown) * 1.033).strip('')
LimitUp = str(val(SetPointUp) * 0.997).strip('')
if(SetPointUp != 290):
  if(LTempControl >= LimitUp):#aqui
    if(ControlFlujo = 1):
      TimeIni = Tiempo.strip('')
      TimeIni = TimeIni.strip('')
    ControlFlujo = 0
  TimeOnPlateau=(Tiempo - TimeIni) / 60 # Returns "334.90".
  Label52Caption = TimeOnPlateau
else if(LTempControl <= LimitEnd and Up == 0): 
       TurnHeaterOff = 1
       SetLakeShore
       EndRun = 1
TimeOnPlateau = TimeOnPlateau.strip('')
TimePlateau = val(TimePlateau.strip(''))
if(TimeOnPlateau >= TimePlateau and Down == 0):
  Up = 0
  Down = 1
  SetLakeShore
if(EndRun == 1):
  EndData = 0
file.writelines('%f,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (t,text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text18))  


def LakeShore()
TempControl$ = "                       "
TempSample$ = "                       "
CmdTempControl$ = "CDAT?"
CmdTempControl$ = CmdTempControl$.upper()
CmdTempControl$ = CmdTempControl$ + term$
CmdTempSample$ = "SDAT?"
CmdTempSample$ = CmdTempSample$.upper()
CmdTempSample$ = CmdTempSample$ + term$
dev12.query(CmdTempControl$)
dev12.read(TempControl$)
dev12.query(CmdTempSample$)
dev12.read(TempSample$)


def Conversiones()
LCh1 = -val(Ch1$) # Faraday Voltaje
LCh2 = val(Ch2$) # baratron 1
LCh3 = val(Ch3$)# baratron 2
LCh4 = val(Ch4$) # Voltaje del Cañon de Alkanes
LCh6 = -val(Ch6$) # stray light
LCh6 = val(Ch6$) # voltaje del heater reservado para uso futuro)
LCh7 = val(Ch7$) # reservado para uso futuro)
LCh8 = val(Ch8$) # reservado para uso futuro)
LCh9 = val(Ch9$) # piranni 1
LCh10 = val(Ch10$) # piranni 2
LTempControl = val(TempControl$)
LTempSample = val(TempSample$) #faraday en grados
Aux1LCh1 = LCh1 * 8.31784 #8.08184 8.46454 8.31784
#faraday en grados, acumulado
Aux2LCh1 = Aux1LCh1


def Timer1_Timer()
if(EndData == 0):
   Timer1Enabled = 0
else:
   MainLoop

def SetLakeShore()
#SPU$ = "                       "
#SPD$ = "                       "
cmdSPU$ = "SETP " + SetPointUp + term
cmdSHeaterOn$ = "RANG 3" + term$
cmdSHeaterOff$ = "RANG 0" + term$
cmdSPD$ = "SETP " + SetPointDown + term
if(Up == 1):
  dev12.query(cmdSPU)
  dev12.query(cmdSHeaterOn)
if(Down == 1):
  dev12.query(cmdSPD)
if(TurnHeaterOff == 1):
  dev12.query cmdSHeaterOff)
  TurnHeaterOff = 0



def Begin()
BeginEnabled = 0
NumDat = 0
Tiempo = 0
Up = 1
Down = 0
SetLakeShore	#estaba comentariado
CurrentPos_Click
ControlFlujo = 1
TimeOnPlateau = 0
TimeIni = 0
TurnHeaterOff = 0
EndRun = 0
EndLoop = 1
EndData = 1
Timer1Interval = 2*1000 #val(Stime) * 1000 Timer1.Enabled = 1
StartAux = Timer
FinEnabled = 1
#para el grafico
#k = 1
#Release = 0



def Fin()
EndData = 0
SaveFileAsEnabled = 1
#cmdEndEnabled = 1
K2.query(":ROUT:CLOS (@2)")
dev12.query(cmdSHeaterOff$)
dev12.query(cmdSPD$)
FinEnabled = 0
K2.query(":ROUT:CLOS (@2)")
dev12.query(cmdSHeaterOff$)
dev12.query(cmdSPD$)
FinEnabled = 0










begin()
fin()

