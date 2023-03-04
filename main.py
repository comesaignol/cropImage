import os
from PIL import Image
import param


def crop_image():

    i = 0
    for file in param.inputFiles:

        image = Image.open(file)
        width, height = image.size
        new_width = width // 2

        # First half
        cropped_image = image.crop((0, 0, new_width, height))
        i += 1
        myIteration = "{:0{}}".format(i, 3)
        myPath = os.path.join(param.pathOutput, param.fileId + "_" + myIteration + "." + param.inputExtension)
        cropped_image.save(myPath)
        print("Save file:", myPath)

        # Second half
        cropped_image = image.crop((new_width, 0, width, height))
        i += 1
        myIteration = "{:0{}}".format(i,3)
        myPath = os.path.join(param.pathOutput, param.fileId + "_" + myIteration + "." + param.inputExtension)
        cropped_image.save(myPath)
        print("Save file:", myPath)

if __name__ == '__main__':
    crop_image()
