from PIL import Image

# Open the first PNG image
image_1 = Image.open("ship.png")

# Save the first image as BMP
bmp_image_path_1 = "ship.bmp"
image_1.save(bmp_image_path_1)

# Open the second PNG image
image_2 = Image.open("alien.png")

# Save the second image as BMP
bmp_image_path_2 = "alien.bmp"
image_2.save(bmp_image_path_2)
