import cv2
import numpy as np

from PIL import Image

vidFile = 'input/movie_source.mp4'

def meanSuaredError(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

def videoProcessor(vidFile):

  count = 0
  vidcap = cv2.VideoCapture(vidFile)
  success,image = vidcap.read()

  while success:
    img1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2GRAY)

    mse, diff = meanSuaredError(img1, img2)

    print("Image matching Error between the two images:", mse)
    cv2.imshow("Difference", diff)
    cv2.waitKey(600)
    cv2.destroyAllWindows()

    success,image = vidcap.read()
    count += 1

if __name__ == "__main__":

    videoProcessor(vidFile)