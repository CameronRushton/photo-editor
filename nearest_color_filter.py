# SYSC 1005 Fall 2015 Lab 11, Extra Practice Exercise #5

from Cimpl import *

# Do not modify or delete any of the statements in this section.

black = create_color(0, 0, 0)
white = create_color(255, 255, 255)

red = create_color(255, 0, 0)
green = create_color(0, 255, 0)
blue = create_color(0, 0, 255)

cyan = create_color(0, 255, 255)
magenta = create_color(255, 0, 255)
yellow = create_color(255, 255, 0)

gray = create_color(128, 128, 128)

teal = create_color(0, 128, 128)
purple = create_color(128, 0, 128)
olive = create_color(128, 128, 0)

maroon = create_color(128, 0, 0)
navy = create_color(0, 0, 128)
other_green = create_color(0, 128, 0)
# Note: W3C names (0, 128, 0) as "green", but other organizations
# define green to be the primary colour (0, 255, 0), and don't name (0, 128, 0).
# To compound the confusion, W3C names (0, 255, 0) as "lime"...

# palette 1 - black and white and gray
palette_1 = [black, white, gray]

# palette 2 - the 8 RGB triplets composed of 0 and 255
palette_2 = [black, white, red, green, blue, cyan, magenta, yellow]

# palette 3 - the 8 RGB triplets composed of 0 and 128
palette_3 = [black, gray, teal, purple, olive, maroon, other_green, navy]

# palette 4 - a union of palettes 1 and 2 (15 colours).
palette_4 = [black, white, gray, red, green, blue, cyan, magenta, yellow,
             teal, purple, olive, maroon, other_green, navy]

# palette 5 - the 3 RGB triplets composed of two 0's and one 255
palette_5 = [red, green, blue]

# palette 6 - the 3 RGB triplets composed of one 0 and two 255's
palette_6 = [cyan, magenta, yellow]

        
# Write the definition of find_nearest_color here.
        
# Write the definition of nearest_color here.        

def test_nearest_color():
    original = load_image(choose_file())
     
    img = copy(original)
    nearest_color(img, palette_1)
    show(img)
    # save_as(img, "nearest_color_palette_1.jpg")    

    img = copy(original)
    nearest_color(img, palette_2)
    show(img)
    # save_as(img, "nearest_color_palette_2.jpg")    

    img = copy(original)
    nearest_color(img, palette_3)
    show(img)
    # save_as(img, "nearest_color_palette_3.jpg")

    img = copy(original)
    nearest_color(img, palette_4)
    show(img)
    # save_as(img, "nearest_color_palette_4.jpg")    

    img = copy(original)
    nearest_color(img, palette_5)
    show(img)
    # save_as(img, "nearest_color_palette_5.jpg")    

    img = copy(original)
    nearest_color(img, palette_6)
    show(img)
    # save_as(img, "nearest_color_palette_6.jpg")