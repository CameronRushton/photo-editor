""" SYSC 1005 A Fall 2015
Image processing examples - two filters that create a grayscale image
from a colour image.

To run all the filters, load this module into Python, then call test_all
from the shell:

>>> test_all()
"""
from Cimpl import *

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

def grayscale_copy(img):
    """ (Cimpl.Image) -> Image
    
    Return a grayscale copy of the image bound to img.
    The original image is not altered.
    
    >>> image = load_image(choose_file()) 
    >>> modified = grayscale_copy(image)
    >>> show(modified)
    >>> show(image)
    """
    gray_image = copy(img)
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        col = create_color(brightness, brightness, brightness)
        
        # Modify the pixel @ (x, y) in the copy, not the original image.
        
        set_color(gray_image, x, y, col)
        
    return gray_image

def test_all():
    file = choose_file()
    original = load_image(file) 
    show(original)
    
    image = copy(original)
    grayscale(image)
    
    # Show the image that was passed to grayscale, so that we can verify
    # that the filter modified the image.
    show(image)    
    
    image = copy(original)    
    modified = grayscale_copy(image)
    
    # Show the image returned by grayscale_copy, so that we can verify that
    # it is a modified image.
    show(modified)  
    
    # Show the image that was passed to grayscale_copy, so that we can
    # verify that it was not changed by the filter.
    show(image) 
