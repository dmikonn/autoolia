import cv2
import imagehash

from PIL import Image

vidFile = '/home/user/Downloads/Константин Заслонов.mkv'
# IMG_SOURCE = "example_frame.jpg"
# hash0 = imagehash.average_hash(Image.open('example_frame.jpg'))

def videoProcessor(vidFile):

  count = 0
  cutoff = 25
  vidcap = cv2.VideoCapture(vidFile)
  success,image = vidcap.read()
  hash0 = imagehash.average_hash(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))

  while success:
    hash1 = imagehash.average_hash(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
    if hash0 - hash1 > cutoff:
      cv2.imwrite("output/frame%d.png" % count, image)
      print('frame contents are definitely different')
      hash0 = hash1
    else:
      print('frame contents are not different enough')
    success,image = vidcap.read()
    count += 1

"""
class FrameContainer:
  def __init__(self, movieFile, imgFile):
    self.movieFile = movieFile
    self.imgFile = imgFile
    self.cutoff = 2  # maximum bits that could be different between the hashes.

  def __str__(self):
    return f"Обрабатываемый файл фильма: {self.movieFile}; образец кадра: {self.imgFile}; макскимальное отличие: {self.cutoff}"

  def imgFileHash(self):
    return imagehash.average_hash(Image.open(self.imgFile))
"""

if __name__ == "__main__":

    videoProcessor(vidFile)
