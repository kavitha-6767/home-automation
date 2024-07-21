import pyfirmata
comport='COM4'
board=pyfirmata.Arduino(comport)
led_2=board.get_pin('d:12:o') # led 1 
led_3=board.get_pin('d:11:o') # led 2 
led_4=board.get_pin('d:8:o') # fan
led_5=board.get_pin('d:7:o') # fan
led_2.write(0)
led_3.write(0)
led_4.write(0)
led_5.write(0)
def led(total):
 if total==0: # FAN OFF
 led_4.write(0)
 led_5.write(0)
 elif total==1: # LED1 ON
 led_2.write(1)
 elif total==2: # LED2 ON
 led_3.write(1)
 elif total==3: # LED1 OFF
 led_2.write(0)
 elif total==4: # LED2 OFF
 
 led_3.write(0)
 elif total==5: # FAN ON
 
 led_4.write(1)
 led_5.write(0)