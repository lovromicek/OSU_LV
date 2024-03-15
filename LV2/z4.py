import numpy as np
import matplotlib.pyplot as plt    

black_square = np.zeros((50, 50))
white_square = np.ones((50, 50)) * 255

top_left = black_square
top_right = white_square
bottom_left = white_square
bottom_right = black_square

top_row = np.hstack((top_left, top_right))
bottom_row = np.hstack((bottom_left, bottom_right))
final_image = np.vstack((top_row, bottom_row))

plt.figure()
plt.imshow(final_image, cmap = "gray")
plt.show()