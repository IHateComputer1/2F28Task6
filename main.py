def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(32 + 1.8 * input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)
