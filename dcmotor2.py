# -*- coding: utf-8 -*-
'''
Created on Sat Apr 22 2017
@author: jsha

'''

import RPi.GPIO as GPIO
import sys, termios, time

def init_set():
    GPIO.setmode(GPIO.BCM)

	# GPIO Pins Motor_A: 17(PWM_sig12), 27(in1), 22(in2)
	# GPIO Pins Motor_B: 13(PWM_sig34), 5(in3), 6(in4)
	# Motor_A is located in Left
	# Motor_B is located in Right

    global Pin_pwm_sig12, Pin_in1, Pin_in2, Pin_pwm_sig34, Pin_in3, Pin_in4
	
    Pin_pwm_sig12 = 17
    Pin_in1 = 22
    Pin_in2 = 27
    Pin_pwm_sig34 = 5 
    Pin_in3 = 13
    Pin_in4 = 6

    GPIO.setup(Pin_pwm_sig12, GPIO.OUT)
    GPIO.setup(Pin_in1, GPIO.OUT)
    GPIO.setup(Pin_in2, GPIO.OUT)
    GPIO.setup(Pin_pwm_sig34, GPIO.OUT)
    GPIO.setup(Pin_in3, GPIO.OUT)
    GPIO.setup(Pin_in4, GPIO.OUT)

    global init_freq, pwm_12, pwm_34
    
    init_freq = 500
    pwm_12 = GPIO.PWM(Pin_pwm_sig12, init_freq)	# GPIO.PWM(channel, frequency)
    pwm_34 = GPIO.PWM(Pin_pwm_sig34, init_freq)

    global sleep_time, sp_high, sp_low, sp_rot 
    sleep_time = [2.3, 4.6, 6.9, 9.2, 11.5]
    sp_high = 18
    sp_low = 12
    sp_rot = 13

    print("Initializing Completed")

def cleanup():
    GPIO.cleanup()
    print("System Cleanup!!")


# speed(20, 30, 40) :  DutyCycle
# angle(10, 20, 40) : degree
# direct('L', 'R') : ('Left', 'Right')
# move('F', 'B')  : ('Forward', 'Backward')
def direction(direct, angle):
    pwm_12.start(0)
    pwm_34.start(0)

    if direct == 'Left':
        GPIO.output(Pin_in1, False)
        GPIO.output(Pin_in2, True)
        GPIO.output(Pin_in3, False)
        GPIO.output(Pin_in4, True)
        
    elif direct == 'Right':
        GPIO.output(Pin_in1, True)
        GPIO.output(Pin_in2, False)
        GPIO.output(Pin_in3, True)
        GPIO.output(Pin_in4, False)
    
    if angle == '10':
        pwm_12.ChangeDutyCycle(sp_rot)
        pwm_34.ChangeDutyCycle(sp_rot)
        time.sleep(sleep_time[0])
        print("direction = %s, angle = %s, sleeptime = %i" %(direct, angle, sleep_time[0]))

    elif angle == '30':
        pwm_12.ChangeDutyCycle(sp_rot)
        pwm_34.ChangeDutyCycle(sp_rot)
        time.sleep(sleep_time[1])
        print("direction = %s, angle = %s, sleeptime = %i" %(direct, angle, sleep_time[1]))

    elif angle == '50':
        pwm_12.ChangeDutyCycle(sp_rot)
        pwm_34.ChangeDutyCycle(sp_rot)
        time.sleep(sleep_time[2])
        print("direction = %s, angle = %s, sleeptime = %i" %(direct, angle, sleep_time[2]))
    
    elif angle == '70':
        pwm_12.ChangeDutyCycle(sp_rot)
        pwm_34.ChangeDutyCycle(sp_rot)
        time.sleep(sleep_time[3])
        print("direction = %s, angle = %s, sleeptime = %i" %(direct, angle, sleep_time[2]))
    
    elif angle == '90':
        pwm_12.ChangeDutyCycle(sp_rot)
        pwm_34.ChangeDutyCycle(sp_rot)
        time.sleep(sleep_time[4])
        print("direction = %s, angle = %s, sleeptime = %i" %(direct, angle, sleep_time[2]))
    print("Goto the direction")

#    print("direction = %s, angle = %i, sleeptime = %i" %(direction, angle, sleeptime[2]))
    pwm_12.ChangeDutyCycle(0)
    pwm_34.ChangeDutyCycle(0)

def forward(speed):
    pwm_12.start(0)
    pwm_34.start(0)
    
    GPIO.output(Pin_in1, True)
    GPIO.output(Pin_in2, False)
    GPIO.output(Pin_in3, False)
    GPIO.output(Pin_in4, True)
                
    if speed == 'Low':
        pwm_12.ChangeDutyCycle(sp_low)
        pwm_34.ChangeDutyCycle(sp_low)

    elif speed == 'High':
        pwm_12.ChangeDutyCycle(sp_high)
        pwm_34.ChangeDutyCycle(sp_high)

    print("Go forward")
    print("speed = %s" %(speed))


def backward(speed):
    pwm_12.start(0)
    pwm_34.start(0)

    GPIO.output(Pin_in1, False)
    GPIO.output(Pin_in2, True)
    GPIO.output(Pin_in3, True)
    GPIO.output(Pin_in4, False)

    if speed == 'Low':
        pwm_12.ChangeDutyCycle(sp_low)
        pwm_34.ChangeDutyCycle(sp_low)

    elif speed == 'High':
        pwm_12.ChangeDutyCycle(sp_high)
        pwm_34.ChangeDutyCycle(sp_high)
    
    print("Go backward")
    print("speed = %s" %(speed))

def stop():
    pwm_12.stop()
    pwm_34.stop()
    print("Stop")

#if __name__ == '__main__ :
#GPIO.cleanup 

