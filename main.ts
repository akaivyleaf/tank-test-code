function turnLeft (theDelay: number) {
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P13, speed)
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P14, speed)
    basic.pause(theDelay)
}
function goBackward (theDelay: number) {
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P13, speed)
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P14, speed)
    basic.pause(theDelay)
}
function goForward (theDelay: number) {
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P13, speed)
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P14, speed)
    basic.pause(theDelay)
}
function stopMoving (theDelay: number) {
    ContinuousServo.turn_off_motor(DigitalPin.P13)
    ContinuousServo.turn_off_motor(DigitalPin.P14)
    basic.pause(theDelay)
}
function turnRight (theDelay: number) {
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P13, speed)
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P14, speed)
    basic.pause(theDelay)
}
let speed = 0
speed = 50
basic.pause(3000)
basic.forever(function () {
    goForward(2000)
    turnRight(1800)
    goBackward(2000)
    turnLeft(1800)
    stopMoving(4000)
})
