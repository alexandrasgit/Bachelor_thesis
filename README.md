# Bachelor_thesis
The code for Fiji macro plugin and the python code for creating the presenting figures are described. 

## Macro.jm
The macro plugin allows the batch merging of GFP and red channels, as well as the addition of scale bar. Start with choosing Plugins -> Macros -> Run... 
The code starts with the assigning the folder with the initial images. They should be in the form of GFP*samplenumber*.tiff and same for red - red*samplenumber*.tiff. Next, the user chooses the folder for the merged images. 

#### The setup
The code worked on the Fiji (ImageJ2) in version of 2.3.0 installed on macOS.

## Presenting_figures.py
The code employs [matplotlib](https://matplotlib.org) to create the final presenting figures for tumour, mid-tumour, control and presenting figure. The scale bar can be also added to images. See commented: 
<p>#scalebar = ScaleBar(scale,units="um",length_fraction=0.125)<br>
#plt.gca().add_artist(scalebar)</p>
