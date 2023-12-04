import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sys

class ImageSegmentation:

    # tab10 colors used for marking
    colors = [tuple(np.array(cm.tab10(i)[:3]) * 255) for i in range(10)]

    def __init__(self, imagePath) -> None:

        # read the image
        try:
            self.image = cv2.imread(imagePath)
            if self.image is None:
                raise FileNotFoundError(f"Failed to read image: {imagePath}")
        except FileNotFoundError as e:
            print("image not found at the path provided...")
            sys.exit()

        self.image_copy = self.image.copy()

        # to keep track of the marker
        self.current_marker = 1
        
        # to display the segmented image
        self.segments = np.zeros(self.image.shape, np.uint8)

        # marker image for watershed algorithm
        self.marker_image = np.zeros(self.image.shape[:2], np.int32)

        self.marks_updated = False

    def _mouse_callback(self, event, x, y, flags, param):
        # use left mouse button to put a marker
        if event == cv2.EVENT_LBUTTONDOWN:

            # for marker image
            cv2.circle(self.marker_image, (x,y), 10, self.current_marker, -1)
        
            # for users
            cv2.circle(self.image_copy, (x,y), 10, self.colors[self.current_marker], -1)
        
            self.marks_updated = True

    # main process
    def runProcess(self):

        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.namedWindow('Watershed Segmentation', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('Image', self._mouse_callback)

        while True:
            cv2.imshow('Watershed Segmentation', self.segments)
            cv2.imshow('Image', self.image_copy)
            
            k = cv2.waitKey(1)
    
            # using esc key to halt
            if k == 27:
                break
    
            # c to undo all changes
            elif k == ord('c'):
                self.image_copy = self.image.copy()
                self.marker_image = np.zeros(self.image.shape[:2], np.int32)
                self.segments = np.zeros(self.image.shape, np.uint8)
    
            # using keyboard numbers to choose a color
            elif k > 0 and chr(k).isdigit():
                self.current_marker = int(chr(k))
        
            if self.marks_updated:
                marker_image_copy = self.marker_image.copy()
                cv2.watershed(self.image, marker_image_copy)
                self.segments = np.zeros(self.image.shape, np.uint8)
        
                for color_ind in range(10):
                    self.segments[marker_image_copy == (color_ind)] = self.colors[color_ind]

        cv2.destroyAllWindows()


        



