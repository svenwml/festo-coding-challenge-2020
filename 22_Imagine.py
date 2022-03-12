import cv2
import numpy
import matplotlib.pyplot

# A "page that does not exist" is e.g. this one: https://coding-challenge.festo.com/404
# The background image is: https://coding-challenge.festo.com/images/cybersecurity.png

# Note: Before running the script, please download the image manually.

original = cv2.imread("cybersecurity.png", 0)
spectrum = numpy.fft.fft2(original)

matplotlib.pyplot.imshow(numpy.log(numpy.abs(spectrum)), "gray")
matplotlib.pyplot.show()