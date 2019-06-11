from Cimpl import *

#Exercise 2
def build_hot_metal_lookup_table():
    """ None --> (List)
    Returns a list of color RGB values for the hot_metal filter.
    """
    lookup = []
    
    #build color table
    for b in range (256): #For brightness 0 -> 255

        if b < 170:
            green = 0
            
        else:
            green = 3 * (b - 170)
            
        if b > 170:
            red = 255
                        
        else:
            red = 1.5 * b
    
        lookup.append(create_color(red, green, 0))
        
    return lookup

hot_metal_table = build_hot_metal_lookup_table()

def hot_metal(img, table):
    
    """(img, list) --> none 
    Sets each pixel in an image to a combination of red and green based on a weighted brightness.
    """
    
    for x, y, col in img:
        
        red, green, blue = col
        wB = int(0.3*red + 0.59 * green + 0.11 * blue)
        set_color(img, x, y, table[wB])
        
