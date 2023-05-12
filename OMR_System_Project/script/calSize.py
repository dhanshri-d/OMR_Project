from PIL import Image

# Open the image
image_path = "/home/dhanshri/Desktop/MajorProjectWork_2023/MyProject/Imges/ans.jpeg" # Replace with the actual path to your image file
image = Image.open(image_path)

# Get the size of the image
image_size = image.size

# Extract width and height
width, height = image_size

# Print the size of the image
print("Image Width: {} pixels".format(width))
print("Image Height: {} pixels".format(height))

desired_height = 609
desired_width = 708

# Resize the image
resized_image = image.resize((desired_width, desired_height))

image_size = resized_image.size

# Extract width and height
width, height = image_size

# Print the size of the image
print("Image Width: {} pixels".format(width))
print("Image Height: {} pixels".format(height))


resized_image.save("example_resized.jpeg")