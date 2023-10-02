import cv2
import imagehash

from PIL import Image

# hash0 = imagehash.average_hash(Image.open('example_frame.jpg'))

def videoProcessor(VIDEO_SOURCE, hash0):

  count = 0
  cutoff = 2
  vidcap = cv2.VideoCapture(VIDEO_SOURCE)
  success,image = vidcap.read()

  while success:
    hash1 = imagehash.average_hash(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
    if hash0 - hash1 < cutoff:
      cv2.imwrite("output/frame%d.png" % count, image)

      print('images are similar')
    else:
      print('images are not similar')
    success,image = vidcap.read()
    count += 1

class FrameContainer:
  def __init__(self, movieFile, imgFile):
    self.movieFile = movieFile
    self.imgFile = imgFile
    self.cutoff = 2  # maximum bits that could be different between the hashes.

  def __str__(self):
    return f"Обрабатываемый файл фильма: {self.movieFile}; образец кадра: {self.imgFile}; макскимальное отличие: {self.cutoff}"

  def imgFileHash(self):
    return imagehash.average_hash(Image.open(self.imgFile))