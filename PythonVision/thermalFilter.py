import sys
import numpy as np
import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm
from matplotlib import pyplot

def applyThermal(image_source):
    img = cv2.imread(image_source)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    colormap = mpl.cm.jet
    cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
    scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_inverted = cv2.bitwise_not(gray)
    colors = scalarMap.to_rgba(gray_inverted, bytes=False)

    pyplot.imsave(image_source, colors)
    