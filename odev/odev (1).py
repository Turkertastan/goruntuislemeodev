from PIL import Image
import numpy as np 


# Image dosyasını açalım
img = Image.open("resim.jpg")

#NOT: RESİM DOSYASI "RGB" MODUNDA OLMAK ZORUNDADIR 
#BUNUN KONTROLÜ İÇİN..
if img.mode != "RGB":
    print("Lütfen RGB modunda bir resim seçin")

# Görüntü dosyasından bir dizi oluşturalım
img_dizi = np.array(img)
print(img.mode)

# RGB modunun alabileceği en yüksek sayı
I_max = 255
 
#Önemli nokta burası: Bir rengin tersini bulmak için o rengin sahip olduğu RGB değerini 
# en yüksek RGB değeriyle(255) çıkarmaktır. 
img_dizi = I_max - img_dizi # Bu satır bize resmin ters renklerinin Rgb değerini verir
 
# Yeni oluşan dizimizi fromarray fonksiyonuyla bir resime dönüştürelim
img_negatif = Image.fromarray(img_dizi)

# Yeni oluşan resmi kaydet 
img_negatif.save("Image_negatif.jpg")