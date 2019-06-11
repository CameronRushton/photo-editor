""" SYSC 1005 A Fall 2015 Lab 4 - Part 3.
"""

from Cimpl import *

#--------------------------------------
# This function was presented in class:

def grayscale(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified picture into a grayscale image.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)        
    """
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)

# Exercise 7

def weighted_grayscale(img):
    
    """ (Cimpl.Image) -> None
    
    Convert the specified picture into a weighted grayscale image.
    
    >>> image = load_image(choose_file()) 
    >>> weighted_grayscale(image)
    >>> show(image)        
    """
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r * 0.299 + g * 0.587 + b * 0.114)
        gray = create_color(brightness, brightness, brightness)
        set_color(img, x, y, gray)


# Exercise 6

def negative(img):
    
    """ (Cimpl.Image) -> None
        
        Convert the specified picture into a negative image.
        
        >>> image = load_image(choose_file()) 
        >>> negative(image)
        >>> show(image)        
        """    
    
    for pixel in img:
                
        x, y, col = pixel
        r, g, b = col
                
        r = 255 - r
        g = 255 - g
        b = 255 - b
             
        col = create_color(r, g, b)
        set_color(img, x, y, col)

#---------------------------------------------------------------
# A filter that uses three if statements to check every pixel's
# red, green and blue components, individually.

def solarize(img):
    """ (Cimpl.Image) -> None
    
    Solarize the specified image, modifying all RGB components with intesities
    that are less than the specified threshold.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image)
    >>> show(image)
    """

    for x, y, col in img:
        red, green, blue = col

        # Invert the values of all RGB components that are less than the
        # threshold, leaving components with higher values unchanged.

        if red < 128:
            red = 255 - red

        if green < 128:
            green = 255 - green

        if blue < 128:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)


#--------------------------------------
# A filter that uses an if-else statement.

def black_and_white(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on whether
    # its brightness is in the lower or upper half of this range.

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3
        
        if brightness < 128:
            set_color(img, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(img, x, y, white)


#--------------------------------------
# A filter that uses an if-elif-else statement.

def black_and_white_and_gray(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, col in img:
        red, green, blue = col
        
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

# Exercise 2
# Extreme contrast Filter

def extreme_contrast(img):
    
    """ (Cimpl.Image) -> None
    
    Modify img, maximizing the contrast between the light and dark pixels.
    
    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    >>> show(image)
    """
    
    for x, y, col in img:
        
        r, g, b = col
        
        if r <= 127:
            
            r = 0
        
        else:
            
            r = 255
        
        if g <= 127:
            
            g = 0
            
        else:
            
            g = 255
            
        if b <= 127:
            
            b = 0
            
        else:
            
            b = 255
            
        col = create_color(r, g, b)
        set_color(img, x, y, col)
        
# Exercise 3
# Sepia Tint

def sepia_tint(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified image to sepia tones.
    
    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """
    
    grayscale(img)
    
    for x, y, col in img:
        
        r, g, b = col
        
        if r < 63:
            
            b *= 0.9
            r *= 1.1
            
        elif r <= 191:
            
            b *= 0.85
            r *= 1.15
            
        else:
            
            b *= 0.93
            r *= 1.08
            
        col = create_color(r, g, b)
        set_color(img, x, y, col)
        
# Exercise 4

def _adjust_component(amount):
    
    """ (int) -> int
    
    Divide the range 0..255 into 4 equal size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.
    
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    
    if amount <= 63:
        
        return 31
    
    elif amount <= 127:
        
        return 95
    
    elif amount <= 191:
        
        return 159
    
    else:
        
        return 223
    
# Exercise 5
# Posterize an image

def posterize(img):
    """ (Cimpl.Image) -> None
    
    "Posterize" the specified image.
    
    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)
    """
    
    for x, y, col in img:
        
        r, g, b = col
        
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        
        col = create_color(r, g, b)
        set_color(img, x, y, col)
        
# Exercise 6

def simplify(img):
    """ (Cimpl.Image) -> None
    
    Modify img so that each pixel is white, black, red, green or
    blue. Very bright pixels are changed to white. Very dark
    pixels are changed to black. All other pixels are changed to
    red, green or blue, depending on which component is the
    largest.
    
    >>> image = load_image(choose_file())
    >>> simplify(image)
    >>> show(image)
    """
    
    for x, y, col in img:
        
        r, g, b = col
        
        if r > 200 and g > 200 and b > 200:
            
            r = 255
            g = 255
            b = 255
            
        elif r < 50 and g < 50 and b < 50:
            
            r = 0
            g = 0
            b = 0
            
        elif r > g and r > b:
            
            r = 255
            
        elif g > r and g > b:
            
            g = 255
            
        else:
            
            b = 255
    
        col = create_color(r, g, b)
        set_color(img, x, y, col)

# Exercise 3
   
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
        
            total_red = 0
            total_green = 0
            total_blue = 0
    
            # Grab the pixel @(x, y) and its four neighbours
            for j in range(-1, 2):
                for i in range(-1, 2):
                    
                    red, green, blue = get_color(source, x + j, y + i)
                    
                    total_red += red
                    total_green += green
                    total_blue += blue
                    
                    average_red = total_red // 9
                    average_green = total_green // 9
                    average_blue = total_blue // 9
            
            new_color = create_color(average_red, average_green, average_blue)
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

# Exercise 1 - Lab 6

def detect_edges (img, threshold):
    """ (Cimpl.Image, float) -> None
    
    Modify the specified image using edge detection.
    An edge is detected when a pixel's brightness differs
    from that of its neighbour by an amount that is greater
    then the specified threshold.
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image)
    >>> show(image)
    """
    black = create_color(255, 255, 255)
    white = create_color(0, 0, 0)
    
    for y in range(1, get_height(img) - 1):
        for x in range(1, get_width(img) - 1):
            
            #top_red, top_green, top_blue = get_color(img, x, y - 1)
            center_red, center_green, center_blue = get_color(img, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
            
            contrast = ((center_red + center_blue + center_green) // 3) - ((bottom_red + bottom_blue + bottom_green) // 3)
            
            if contrast < 0:
                
                contrast *= -1
                
            if contrast > threshold: # High contrast - change top to black
                
                set_color(img, x, y, white)
                
            else: # Low contrast - change top to white
                
                set_color(img, x, y, black)
                
# Exercise 2 - L6

def detect_edges_better (img, threshold):
    """ (Cimpl.Image, float) -> None
    
    Modify the specified image using edge detection.
    An edge is detected when a pixel's brightness differs
    from that of its neighbour by an amount that is greater
    then the specified threshold.
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image)
    >>> show(image)
    """
    black = create_color(255, 255, 255)
    white = create_color(0, 0, 0)
    
    for y in range(1, get_height(img) - 1):
        for x in range(1, get_width(img) - 1):
            
            #top_red, top_green, top_blue = get_color(img, x, y - 1)
            center_red, center_green, center_blue = get_color(img, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
            right_red, right_green, right_blue = get_color(img, x + 1, y)
            
            contrastBottom = ((center_red + center_blue + center_green) // 3) - ((bottom_red + bottom_blue + bottom_green) // 3)
            
            contrastRight = ((center_red + center_blue + center_green) // 3) - ((right_red + right_blue + right_green) // 3)
            
            if contrastBottom < 0:
                
                contrastBottom *= -1
                
            if contrastRight < 0:
                
                contrastRight *= -1
                
            if contrastBottom > threshold or contrastRight > threshold: # High contrast - change top to black
                
                set_color(img, x, y, white)
                
            else: # Low contrast - change top to white
                
                set_color(img, x, y, black)
                
            
def flip(img):
                
    """ (Cimpl.Image) -> None
                
    Flip the specified image around an imaginary vertical
    line drawn through the midpoint of the image
                
    >>> image = load_image(choose_file())
    >>> flip(image)
    >>> show(image)
    """
    width = get_width(img)
    
    for y in range(0, get_height(img)):
        for x in range(0, get_width(img)//2):
            
            col = get_color(img, x, y)
            
            newX = width - x - 1
            
            set_color(img, x, y, get_color(img, newX, y))
            set_color(img, newX, y, col)
            
            
        