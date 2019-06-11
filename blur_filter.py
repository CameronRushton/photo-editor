# SYSC 1005 Fall 2015

from Cimpl import *

def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of the image bound to source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(source)):
    #     for x in range(0, get_width(source)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    #
    # We have to adjust the arguments passed to range to ensure that (x, y)
    # never specifies the location of pixel on the top, bottom, left or right 
    # edge of the image, because those pixels don't have four neighbours.
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @(x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red ) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green ) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue ) // 5

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target


def test_blur():
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)
    # save_as(blurred, "blurred.jpg")
    
    
def make_very_blurry(number_of_blurs):
    img = load_image(choose_file())
    
    for i in range(number_of_blurs):
        img = blur(img)  # Blur the image repeatedly

    show(img)
    # save_as(img, "very_blurred.jpg")   
    

# Exercise - modify the filter so that the pixels at the image's edges are
# blurred. Hint: the number of neighbours of these pixels will vary, depending 
# on the pixel's coordinates.