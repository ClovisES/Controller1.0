# Import all libraries 
# step 0
# step 1
# step 2
# step 3
# step 4


import os
import pdb
import datetime
import SystemTime
import Relays
import RPi.GPIO as GPIO
import time


# Pin definitions (updated 7-26-2017)
rel1 = 5 # Relay 1 Q_XV_007 dosifier injector acid (C)
rel2 = 6 # Relay 2 Q_XV_006 dosifier injector B
rel3 = 13 # Relay 3 Q_XV_005 dosifier injector A
rel4 = 19 # Relay 4 Q_XV_004 irrigation zone D
rel5 = 26 # Relay 5 Q_XV_003 irrigation zone C
rel6 = 21 # Relay 6 Q_XV_002 irrigation zone B
rel7 = 20 # Relay 7 Q_XV_001 irrigation zone A
rel8 = 16 # Relay 8 Q_PP001 pump water supply
rel9 = 12 # Relay 9 Q_PP002 pump dosifier
rel10 = 25 # Relay 10 Q_PP003 pump irrigarion



# GPIO definition

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#RTC definition 




#Relay class definition 
# Relays.DisplayRelayStates(1)
	


# Read characters to active relays, off = kill all relays 
# each character actives a relay, just one relay is activated at a time 

list1 = [rel1,rel2,rel3,rel4,rel5,rel6,rel7,rel8,rel9,rel10]

# Tito
# GPIO setup outputs and Start up all off
GPIO.setup(list1,GPIO.OUT, initial=GPIO.HIGH)

# end Tito



while 1 : 
	var= raw_input('Enter relay # or kill entering off: ')
	if var == '1' :
		
		 GPIO.output(rel1, GPIO.LOW)
		 print('relay 1 = ON') 
	     
        else: 
	     GPIO.output(rel1, GPIO.HIGH)
	     print('relay 1 = OFF')
	
	if var == '2' :
		
		 GPIO.output(rel2, GPIO.LOW)
		 print('relay 2 = ON') 
	     
        else: 
	     GPIO.output(rel2, GPIO.HIGH)
	     print('relay 2 = OFF')
	     
	
	if var == '3' :
		
		 GPIO.output(rel3, GPIO.LOW)
		 print('relay 3 = ON') 
	     
        else: 
	     GPIO.output(rel3, GPIO.HIGH)
	     print('relay 3 = OFF')
	
	
	if var == '4' :
		
		 GPIO.output(rel4, GPIO.LOW)
		 print('relay 4 = ON') 
	     
        else: 
	     GPIO.output(rel4, GPIO.HIGH)
	     print('relay 4 = OFF')
	
	if var == '5' :
		
		 GPIO.output(rel5, GPIO.LOW)
		 print('relay 5 = ON') 
	     
        else: 
	     GPIO.output(rel5, GPIO.HIGH)
	     print('relay 5 = OFF')
	
	
	
	if var == '6' :
		
		 GPIO.output(rel6, GPIO.LOW)
		 print('relay 6 = ON') 
	     
        else: 
	     GPIO.output(rel6, GPIO.HIGH)
	     print('relay 6 = OFF')
	
	if var == '7' :
		
		 GPIO.output(rel7, GPIO.LOW)
		 print('relay 7 = ON') 
	     
        else: 
	     GPIO.output(rel7, GPIO.HIGH)
	     print('relay 7 = OFF')
	     
	     
	     
	if var == '8' :
		
		 GPIO.output(rel8, GPIO.LOW)
		 print('relay 8 = ON') 
	     
        else: 
	     GPIO.output(rel8, GPIO.HIGH)
	     print('relay 8 = OFF')
	
	if var == '9' :
		
		 GPIO.output(rel9, GPIO.LOW)
		 print('relay 9 = ON') 
	     
        else: 
	     GPIO.output(rel9, GPIO.HIGH)
	     print('relay 9 = OFF')
	
	
	if var == '10' :
		
		 GPIO.output(rel10, GPIO.LOW)
		 print('relay 10 = ON') 
	     
        else: 
	     GPIO.output(rel10, GPIO.HIGH)
	     print('relay 10 = OFF')
	
	if var == 'off' :
		for word in list1:
		 GPIO.output(word, GPIO.HIGH)
		 print ('relays off ' + str(word)) 
		 
	
	
	 
	if var == 'quit' : break 







