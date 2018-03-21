import os
import sys
import glob
from PIL import Image

args = sys.argv
imagepath = os.path.abspath(args[1])
outpath = os.path.abspath(args[2])
imageList = []

if os.path.exists(os.path.abspath(outpath)) == False:
    os.makedirs(os.path.abspath(outpath))

class Resize:
    def __init__(self, width=256, height=256):
        self.width = width
        self.height = height
        self.picture_size = (self.width, self.height)

    def load_imagefile(self):
        extlist = ["*.jpg", "*.jpeg", "*.JPEG", "*.jpe"]
        for e in extlist:
            filelist = glob.glob(os.path.join(imagepath, e))
            imageList.extend(filelist)

    def resize_imagefile(self):
        for img in imageList:
            resized_img = Image.open(img)
            image = resized_img.resize(self.picture_size)
            basename = os.path.basename(img)
            name, ext = os.path.splitext(basename)
            
            if ext is not ".JPEG":
                ext = ".JPEG"

            imgname = name + ext
            image.save(os.path.join(outpath, imgname))


if __name__=='__main__':
    resize = Resize(416, 416)
    resize.load_imagefile()
    resize.resize_imagefile()
