def on_button_pressed_a():
    record.start_recording(record.BlockingState.BLOCKING)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_long_pressed():
    record.play_audio(record.BlockingState.BLOCKING)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_b():
    if Math.random_boolean():
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)
