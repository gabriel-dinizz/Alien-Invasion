from PIL import Image

#abrir arquivo png

image_1 = Image.open("ship.png")

bmp__image__path = "ship.bmp"

image_1.save(bmp__image__path)
