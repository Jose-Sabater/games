import cv2

im = cv2.imread("./static/icons/unnamed.png")

print("original dimensions: ", im.shape)

# preserving aspect ratio
scale_percent = 40  # percent of original size
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)


# not preserving aspect ration
width = 800
height = 600
dim = (width, height)
resized = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)

cv2.imwrite("alien2.png", resized)
print("Resized Dimensions : ", resized.shape)
