import os
import glob

# Param to customize
fileId = "Test"
pathInput = os.path.abspath("input")
pathOutput = os.path.abspath("output")
inputExtension = "jpg"

# Param to script
inputFiles = glob.glob(os.path.join(pathInput+"/*."+inputExtension))