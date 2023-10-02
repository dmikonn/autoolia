from gui import mainGUI
from frameextract import FrameContainer, videoProcessor

VIDEO_SOURCE, IMG_SOURCE = mainGUI()

def frontEnd():
    return True

def findFramesByImg(MOVIE, IMG, TIMEFRAME=False):
    pass

def findFramesByMode(MOVIE, MODE=False, TIMEFRAME=False):
    pass

if __name__ == "__main__":
    if frontEnd():
        fc1 = FrameContainer(VIDEO_SOURCE, IMG_SOURCE)
        print(fc1)
        videoProcessor(VIDEO_SOURCE, fc1.imgFileHash())
    else:
        findFramesByMode(VIDEO_SOURCE)