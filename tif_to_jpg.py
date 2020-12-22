import os
from PIL import Image

path = os.getcwd()
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        # Находим все .tif в папке проекта и конвентируем в jpg
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print("A jpeg file already exists")
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    print("Generating jpeg")
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                except Exception as e:
                    print(e)
