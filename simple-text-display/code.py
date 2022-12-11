# SPDX-FileCopyrightText: 2020 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# This example implements a simple two line scroller using
# Adafruit_CircuitPython_Display_Text. Each line has its own color
# and it is possible to modify the example to use other fonts and non-standard
# characters.

import adafruit_display_text.label
from adafruit_bitmap_font import bitmap_font
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio

# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()

# Load custom font
BIG_FONT = bitmap_font.load_font("LibreBodoniv2002-Bold-27.bdf")

# This next call creates the RGB Matrix object itself. It has the given width
# and height. bit_depth can range from 1 to 6; higher numbers allow more color
# shades to be displayed, but increase memory usage and slow down your Python
# code. If you just want to show primary colors plus black and white, use 1.
# Otherwise, try 3, 4 and 5 to see which effect you like best.
#
# These lines are for the Matrix Portal M4. If you're using a different board,
# check the guide to find the pins and wiring diagrams for your board.
# If you have a matrix with a different width or height, change that too.
# If you have a 16x32 display, try with just a single line of text.
matrix = rgbmatrix.RGBMatrix(
    width=192, height=32, bit_depth=6, tile=1, serpentine=True,
    rgb_pins=[board.MTX_R1,
              board.MTX_G1,
              board.MTX_B1,
              board.MTX_R2,
              board.MTX_G2,
              board.MTX_B2],
    addr_pins=[board.MTX_ADDRA,
               board.MTX_ADDRB,
               board.MTX_ADDRC,
               board.MTX_ADDRD],
    clock_pin=board.MTX_CLK, latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE)

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

text = "Hello world!"
text_area = adafruit_display_text.label.Label(BIG_FONT,color=0x0080ff, text=text)
text_area.x = 14
text_area.y = 15
g = displayio.Group()
g.append(text_area)
display.show(g)


# You can add more effects in this loop. For instance, maybe you want to set the
# color of each label to a different value.
while True:
    display.refresh(minimum_frames_per_second=0)
