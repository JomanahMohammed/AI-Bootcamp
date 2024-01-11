#استدعاء مكتبه OpenCv 
import cv2 as cv 
#استددعاء مكتبه للرسوم البيانيه 
from matplotlib import pyplot as plt 
img = cv.imread('img1.jpg')

cv.imshow('window' , img )
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('window')
plt.axis('off')

plt.show()
