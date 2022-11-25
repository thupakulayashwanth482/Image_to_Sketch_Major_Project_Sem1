import cv2
image = cv2.imread(r"C:\Users\nukan\Desktop\job\pass_photo.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"C:\Users\nukan\Desktop\job\pass_photo_gray.jpg",gray_image)

inverted_image = 255 - gray_image
cv2.imwrite(r"C:\Users\nukan\Desktop\job\pass_photo_inverted.jpg",inverted_image)

blurred_image = cv2.GaussianBlur(inverted_image, (21,21),0)
cv2.imwrite(r"C:\Users\nukan\Desktop\job\pass_photo_blurred.jpg",blurred_image)

inverted_blurred = 255 - blurred_image
pencil_sketch = cv2.divide(gray_image,inverted_blurred,scale= 256.0)
cv2.imwrite(r"C:\Users\nukan\Desktop\job\pass_photo_sketch.jpg",pencil_sketch)
