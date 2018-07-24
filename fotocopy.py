import sys
import os 
import shutil
import PIL.Image
import datetime

def get_date(filename):
    """Return string year-month-date for the filename. Ideally 
    it is foto creation from exif, if no exif is available, its 
    modification time of the file. """

    img = PIL.Image.open(filename)
    exif_data = img._getexif()
    if exif_data and 36867 in exif_data:
        date = exif_data[36867]
        date = date.replace(':','-')
        return date.split()[0]
    else:
        timestamp = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

    
source = sys.argv[1]
dest = sys.argv[2]

source_dict = os.fsencode(source)

for file in os.listdir(source_dict):
    filename = os.fsdecode(file)

    date = get_date(source + filename)
    print(date)

    if not os.path.isdir(dest + "/" + date): 
        os.makedirs(dest + "/" + date)
    
    dest_name = dest + date + "/" + filename
    if not os.path.exists(dest_name):
        print(f'copying {filename} to {dest}')
        shutil.copy(source + filename, dest_name)

    
