def on_button_pressed_a():
    global num
    num = num * 2
    num += 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global num
    num = num * 2
    num += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

num = 0
num = 0

def on_forever():
    basic.show_string("" + str((num)))
basic.forever(on_forever)
