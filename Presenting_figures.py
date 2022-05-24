import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import cv2
import numpy as np
import os

plt.rcParams["figure.figsize"] = (220,100)
plt.rcParams["figure.autolayout"] = True

samples = ['A', 'B', 'C', 'D', 'E']

# 2D 3D

for i in range(5):
    os.chdir('put your directory for initial images')
    red = "red"+str(i+1)+".tif"
    image_red = plt.imread(red)
    plt.subplot(3, 5, 1+i)
    plt.imshow(image_red)
    plt.title(samples[i],
            fontsize=200)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('Histone', fontsize=200)
    # plt.axis('off')
    
#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
#plt.gca().add_artist(scalebar)

    green = "GFP"+str(i+1)+".tif"
    image_green = plt.imread(green)
    plt.subplot(3, 5, 6+i)
    plt.imshow(image_green)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('GFP', fontsize=200)
    # plt.axis('off')
#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
#plt.gca().add_artist(scalebar)

# Here the red and green combined to achieve similar result to composite
    os.chdir('put your directory for composites')
    combined = str(i+1)+".png"
    image = plt.imread(combined)
    plt.subplot(3, 5, 11+i)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('Combined', fontsize=200)
    plt.imshow(image)
    #scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
    #plt.gca().add_artist(scalebar)

    # plt.axis('off')
plt.savefig('combined_2D3D')
plt.show()

# 4D 2D

plt.rcParams["figure.figsize"] = (220,100)
plt.rcParams["figure.autolayout"] = True

samples = ['A', 'B', 'C', 'D', 'E']

for i in range(5):
    os.chdir('put your directory for initial images')
    red = "red"+str(i+1)+".tif"
    image_red = plt.imread(red)
    plt.subplot(3, 5, 1+i)
    plt.imshow(image_red)
    plt.title(samples[i],
            fontsize=200)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('Histone', fontsize=200)
        
#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
#plt.gca().add_artist(scalebar)

    green = "GFP"+str(i+1)+".tif"
    image_green = plt.imread(green)
    plt.subplot(3, 5, 6+i)
    plt.imshow(image_green)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('GFP', fontsize=200)
#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
#plt.gca().add_artist(scalebar)

# Here the red and green combined to achieve similar result to composite
    os.chdir('put your directory for composites')
    combined = str(i+1)+".png"
    image = plt.imread(combined)
    plt.subplot(3, 5, 11+i)
    plt.imshow(image)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('Combined', fontsize=200)
    
    #scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
    #plt.gca().add_artist(scalebar)
plt.savefig('combined_4D2D')
plt.show()

# control

plt.rcParams["figure.figsize"] = (220,100)
plt.rcParams["figure.autolayout"] = True

samples = ['A', 'B', 'C', 'D', 'E']

for i in range(5):
    os.chdir('put your directory for initial images')
    red = "red"+str(i+1)+".tif"
    image_red = plt.imread(red)
    plt.subplot(3, 5, 1+i)
    plt.imshow(image_red)
    plt.title(samples[i],
            fontsize=200)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('Histone', fontsize=200)
        
#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
#plt.gca().add_artist(scalebar)

    green = "GFP"+str(i+1)+".tif"
    image_green = plt.imread(green)
    plt.subplot(3, 5, 6+i)
    plt.imshow(image_green)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('GFP', fontsize=200)
        
#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
#plt.gca().add_artist(scalebar)

# Here the red and green combined to achieve similar result to composite
    os.chdir('put your directory for composites')
    combined = str(i+1)+".png"
    image = plt.imread(combined)
    plt.subplot(3, 5, 11+i)
    if i == 0:
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.tick_params(left = False, bottom = False)
        plt.ylabel('Combined', fontsize=200)
    plt.imshow(image)
    #scalebar = ScaleBar(scale,units="um",length_fraction=0.125)
    #plt.gca().add_artist(scalebar)
    
plt.savefig('combined_control')
plt.show()

# Presenting figure 

plt.rcParams["figure.figsize"] = (100,80)
plt.rcParams["figure.autolayout"] = True

os.chdir('put your directory for tumour condition')
image_red = plt.imread('red3.tif')
plt.subplot(3, 3, 3)
fig = plt.imshow(image_red)
plt.title("2 days 3 days",
          fontsize=200)
plt.axis('off')

image_green = plt.imread('GFP3.tif')
plt.subplot(3, 3, 6)
plt.imshow(image_green)
plt.axis('off')

os.chdir('put your directory for tumour composite')
image = plt.imread('3.png')
plt.subplot(3, 3, 9)
plt.imshow(image)
plt.axis('off')

os.chdir('put your directory for mid-tumour')
image_red = plt.imread('red1.tif')
plt.subplot(3, 3, 2)
plt.imshow(image_red)
plt.title("4 days 2 days",
          fontsize=200)
plt.axis('off')

image_green = plt.imread('GFP1.tif')
plt.subplot(3, 3, 5)
plt.imshow(image_green)
plt.axis('off')

os.chdir('put your directory for mid-tumour composite')
image = plt.imread('1.png')
plt.subplot(3, 3, 8)
plt.imshow(image)
plt.axis('off')

os.chdir('put your directory for control')
image_red = plt.imread('red4.tif')
plt.subplot(3, 3, 1)
plt.imshow(image_red)
plt.title("Control",
          fontsize=200)
plt.xticks(color='w')
plt.yticks(color='w')
plt.tick_params(left = False, bottom = False)
plt.ylabel('Histone',fontsize=200)

image_green = plt.imread('GFP4.tif')
plt.subplot(3, 3, 4)
plt.imshow(image_green)
plt.xticks(color='w')
plt.yticks(color='w')
plt.tick_params(left = False, bottom = False)
plt.ylabel('GFP',fontsize=200)

os.chdir('put your directory for control composite')
image = plt.imread('4.png')
plt.subplot(3, 3, 7)
plt.imshow(image)
plt.xticks(color='w')
plt.yticks(color='w')
plt.tick_params(left = False, bottom = False)
plt.ylabel('Combined',fontsize=200)

os.chdir('put your directory for final presenting figure')
plt.savefig('combined_presenting')
plt.show()
