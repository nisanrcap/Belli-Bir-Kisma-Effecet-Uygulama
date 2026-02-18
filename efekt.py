import cv2
import numpy

resim=cv2.imread("kemalSunal.jpeg")
#resim[:,:,2]=0     RGB = 210 sona ne yazarsak diğer renklere sıfır son renge sağ taraftakini yazmış oluruz
#resim[:,:,1]=200
#resim[:,:,0]=50
resim[150:230,380:580,0]=50 #resim[Y,X,RGB] belirlediğimiz kısıma bilirlediğimiz efekti uyguladık
resim[150:230,380:580,1]=150

cv2.imshow("Kemal Sunal",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()