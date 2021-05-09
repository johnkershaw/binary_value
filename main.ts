input.onButtonPressed(Button.A, function () {
    num = num * 2
    num += 0
})
input.onButtonPressed(Button.B, function () {
    num = num * 2
    num += 1
})
let num = 0
num = 0
basic.forever(function () {
    basic.showString("" + (num))
})
