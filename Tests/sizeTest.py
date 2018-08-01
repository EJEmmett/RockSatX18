import  picamera
from __future__ import division

width = 100
height = 100
stream = open('image.data', 'w+b')
# Capture the image in RGB format
with picamera.PiCamera() as camera:
    camera.resolution = (width, height)
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, 'rgb')
# Rewind the stream for reading
stream.seek(0)
# Calculate the actual image size in the stream (accounting for rounding
# of the resolution)
fwidth = (width + 31) // 32 * 32
fheight = (height + 15) // 16 * 16
# Load the data in a three-dimensional array and crop it to the requested
# resolution
image = np.fromfile(stream, dtype=np.uint8).\
        reshape((fheight, fwidth, 3))[:height, :width, :]
# If you wish, the following code will convert the image's bytes into
# floating point values in the range 0 to 1 (a typical format for some
# sorts of analysis)
image = image.astype(np.float, copy=False)
image = image / 255.0