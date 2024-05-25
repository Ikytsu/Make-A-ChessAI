import os
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cairosvg
import io
import matplotlib
import time
import threading
import sys
from matplotlib.widgets import Button

actual_move = 0

with open("output/0", "rb") as svg_file:
    svg_data = svg_file.read()

png_board = cairosvg.svg2png(bytestring=svg_data)
svg_file.close()
image_data = io.BytesIO(png_board)
fig, ax = plt.subplots()
image_box = OffsetImage(plt.imread(image_data), zoom=0.8)
ABb = AnnotationBbox(image_box, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
ax.add_artist(ABb)

def next_clicked(event):
    global actual_move
    actual_move += 1
    with open("output/" + str(actual_move), "rb") as svg_file:
        svg_data = svg_file.read()

    png_board = cairosvg.svg2png(bytestring=svg_data)
    svg_file.close()
    image_data = io.BytesIO(png_board)
    ax.clear()
    image_box = OffsetImage(plt.imread(image_data), zoom=0.8)
    ABb = AnnotationBbox(image_box, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
    ax.add_artist(ABb)

    plt.draw()

next_button_ax = plt.axes([0.7, 0.05, 0.2, 0.075])


next_button = Button(next_button_ax, 'next move')

next_button.on_clicked(next_clicked)

def precedent_clicked(event):
    global actual_move
    actual_move -= 1
    with open("output/" + str(actual_move), "rb") as svg_file:
        svg_data = svg_file.read()

    png_board = cairosvg.svg2png(bytestring=svg_data)
    svg_file.close()
    image_data = io.BytesIO(png_board)
    ax.clear()
    image_box = OffsetImage(plt.imread(image_data), zoom=0.8)
    ABb = AnnotationBbox(image_box, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
    ax.add_artist(ABb)

    plt.draw()

precedent_button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])


precedent_button = Button(precedent_button_ax, 'precedent move')

precedent_button.on_clicked(precedent_clicked)
plt.show()
