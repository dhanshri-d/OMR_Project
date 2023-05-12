from PIL import Image

# Open the PNG image
png_image = Image.open("/home/dhanshri/Desktop/MajorProjectWork_2023/studentAns_Plot.png")

# Convert PNG image to JPEG image
jpeg_image = png_image.convert("RGB")

# Save the JPEG image
jpeg_image.save("StudentPlot.jpg", "JPEG")

