nombre = 0
def dé_qui_roule():
    global nombre
    nombre = 0
    basic.show_leds("""
        # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """)
    nombre += randint(1, 6)

def on_button_pressed_a():
    dé_qui_roule()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    if nombre == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif nombre == 2:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . . . .
            . # . . .
            . . . . .
            """)
    elif nombre == 3:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """)
    elif nombre == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif nombre == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    elif nombre == 6:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
basic.forever(on_forever)
