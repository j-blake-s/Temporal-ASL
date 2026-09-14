
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse

def events_to_color(
    spikes, 
    on_color=[0,0,255], # RED 
    off_color=[255,0,0] # BLUE
): 
    spikes = np.transpose(spikes, axes=(0,1,3,2))

    H, W, T, _ = spikes.shape
    colored_events = np.zeros((H, W, T, 3), dtype=np.uint8)

    on_events = np.where(spikes[:,:,:,0] > 0)
    off_events = np.where(spikes[:,:,:,1] > 0)

    colored_events[on_events] = on_color
    colored_events[off_events] = off_color
    return np.transpose(colored_events, axes=(0,1,3,2))


def plot_sample(file):

        print("Reading...",file)
        with np.load(file) as data:
            x = data['x'].astype(np.uint8)
            y = data['y'][0]

        # Grab class label
        label = ["Tuesday", "Bathroom", "Name", "Weight", "Brown", "Beer", "Favorite", "Colors", "Hamburger", "Marriage"][y]

        # Auto-Detect if sample is event or rgb
        img = events_to_color(x) if np.max(x) <= 1 else x
        for i in range(img.shape[-1]):
            cv2.imshow(label, img[:,:,:,i])
            cv2.waitKey(33)
        cv2.destroyAllWindows()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, required=True, help="file to plot")
args = parser.parse_args()

plot_sample(args.file)

