import numpy as np
import matplotlib.pyplot as plt

img = np.ones((300,300), dtype = "uint8") * 255
print(img)

img2 = img[ : , 150:250] = (255,0,0)
img2 = img[ : , 150:250] = (0,255,0)



plt.imshow(img)