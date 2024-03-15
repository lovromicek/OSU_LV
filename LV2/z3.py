import numpy as np
import matplotlib.pyplot as plt
img = plt.imread ("road.jpg")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.show()

lighten_factor = 100
lightened_image = np.clip(img.astype(int) + lighten_factor, 0, 255).astype(np.uint8)
plt.figure()
plt.imshow(lightened_image, cmap = "gray")
plt.show()

height, width = img.shape

start_col = width // 4
end_col = width // 2

second_quarter = img[:, start_col:end_col]

plt.figure()
plt.imshow(second_quarter, cmap = "gray")
plt.show()

rotated_image_array = np.rot90(img, k=-1)

plt.figure()
plt.imshow(rotated_image_array, cmap = "gray")
plt.show()

mirrored_image_array = np.fliplr(img)

plt.figure()
plt.imshow(mirrored_image_array, cmap = "gray")
plt.show()