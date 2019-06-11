# SYSC 1005 A Fall 2015 Lab 7
# Revised: November 4, 2015.

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """
    # Pop up a dialogue box to select a file
    file = choose_file()
        
    # Exit the program if the Cancel button is clicked.
    if file == "":
                
        sys.exit("File Open cancelled, exiting program")
                
    # Open the file containing the image and load it
    img = load_image(file)
        
    return img    

# A bit of code to demonstrate how to use get_image().
if __name__ == "__main__":
    
    answer = "z" #init. answer and imgLoaded
    imgLoaded = False
    error = False
    
    while answer != "Q":
        
        answer = input ("L)oad image \nN)egative G)rayscale P)osterize S)epia tint E)dge detect\nQ)uit \n:")       
        
        if imgLoaded == False:
            
            if answer == "L":
                                
                img = get_image()
                imgLoaded = True             
            
            elif answer in ["N", "G", "P", "S", "E"]:
                        
                print("Image has not been loaded") 
            
            elif answer == "Q":
                        
                print("Done") #Quit        
            
            else:
            
                print("No such command")
            
        else:
            
            if answer == "L":
                                            
                img = get_image()            
            
            elif answer == "N":
    
                negative(img)
            
            elif answer == "G":
            
                weighted_grayscale(img)
            
            elif answer == "P":
            
                posterize(img)
            
            elif answer == "S":
            
                sepia_tint(img)
            
            elif answer == "E":
            
                threshold = float(input("Enter the threshold: "))
                detect_edges_better(img, threshold)
                
            elif answer == "Q":
                
                print("Done")
                
            else:
                            
                print("No such command")
                error = True
            
        
        if answer != "Q" and imgLoaded == True and error == False:
            
            show(img)
            
        error = False