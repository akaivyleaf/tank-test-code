distance = 0
obstacle = 0
"""

Switch to code that uses ultrasonic sensor extension... ?

"""
def checkDistance():
    global distance
    pins.digital_write_pin(DigitalPin.P0, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P0, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P0, 0)
    distance = Math.idiv(pins.pulse_in(DigitalPin.P1, PulseValue.HIGH), 58)
    basic.pause(100)
    return distance
def turnLeft(theDelay: number):
    pins.servo_set_pulse(AnalogPin.P13, 1200)
    pins.servo_set_pulse(AnalogPin.P14, 1200)
    basic.pause(theDelay)
def goBackward(theDelay: number):
    pins.servo_set_pulse(AnalogPin.P13, 1200)
    pins.servo_set_pulse(AnalogPin.P14, 2000)
    basic.pause(theDelay)
def goForward(theDelay: number):
    pins.servo_set_pulse(AnalogPin.P13, 2000)
    pins.servo_set_pulse(AnalogPin.P14, 1200)
    basic.pause(theDelay)
def turnRight(theDelay: number):
    pins.servo_set_pulse(AnalogPin.P13, 2000)
    pins.servo_set_pulse(AnalogPin.P14, 2000)
    basic.pause(theDelay)

def on_forever():
    global obstacle
    obstacle = checkDistance()
    if obstacle < 8:
        goBackward(1000)
        turnRight(1000)
    else:
        goForward(100)
basic.forever(on_forever)
