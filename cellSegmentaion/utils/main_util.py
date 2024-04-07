import os.path
import sys
import base64

from cellSegmentaion.exception import AppException
from cellSegmentaion.logger import logging

def decodeImage(imgdata, fileName): #write imgstring to filename
    logging.info("enter decodeImage")
    # imgdata = base64.b64decode(imgstring)
    with open("./static/"+fileName, 'wb') as f:
        f.write(imgdata)
        f.close()



def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())