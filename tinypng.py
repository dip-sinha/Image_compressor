import os
from PIL import Image
from PIL import ImageFile
from io import BytesIO
ImageFile.LOAD_TRUNCATED_IMAGES = True
print("||||||||||||||||||||Starting Compression Process||||||||||||||||||||")
for root, dirs, files in os.walk(".", topdown=False):
   for file in files:
        if file.endswith(".jpg"):
            #After compression compress files
            im = Image.open(os.path.join(root,file))
            im.save(os.path.join(root, file), format="JPEG", quality=70)
            print(root+"\ "+file+"-- jpeg --compression done")
        if file.endswith(".png"):
            im = Image.open(os.path.join(root,file))
            im.save(os.path.join(root,file), optizime= False, compress_level=9)
            print(root+"\ "+ file +"-- png --compression done")

print("||||||||||||||||||||done||||||||||||||||||||")
