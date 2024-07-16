
import numpy as np
import matplotlib.pyplot as plt

hight = 300
width = 400
img= np.ones((hight, width, 3), dtype = "uint8")*255

img[:,150:250] = [0,0,255]
img[100:200,:] = [255,0,0]

plt.imshow(img)

plt.show()



