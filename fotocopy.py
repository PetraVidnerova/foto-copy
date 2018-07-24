import sys
import os 
import shutil
import PIL.Image

source = sys.argv[1]
dest = sys.argv[2]


source_dict = os.fsencode(source)

for file in os.listdir(source_dict):
    filename = os.fsdecode(file)

    img = PIL.Image.open(source + filename)
    exif_data = img._getexif()
    print(exif_data)
    
    
    print(f'copying {filename} to {dest}')
    shutil.copy(source + filename, dest + filename)

    
