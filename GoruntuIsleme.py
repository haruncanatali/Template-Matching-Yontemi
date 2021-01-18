#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 # Kütüphanelerimizi dahil ediyoruz
import numpy as np

baglanti = cv2.VideoCapture(0) # Bilgisayarımdaki kameraya bağlanıyorum (0 => bilgisayarımdaki kamera)
aranan_nesne = cv2.imread('kaynak.jpeg',0) # gri formatta aranan resmi alıyoruz

if not baglanti.isOpened(): # bağlantı açılmaz ise
    print('Kamera Bağlantısı Başarısız Oldu')
else:
    while True: # aslında sürekli anlık görüntü alıyor
        ret,goruntu = baglanti.read() # Görüntüyü alıyoruz (return değeri True/False)
        
        if ret == False:
            print('Bağlantıdan Görüntü Alınamadı')
            break
            
        okunan = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY) # gelen görütüyü gri formata çeviriyoruz
        
        w,h = aranan_nesne.shape # aranan görüntünün satır sütn bilgisini w ve h değişkenlerine atıyoruz
        
        sonuc = cv2.matchTemplate(okunan,aranan_nesne,cv2.TM_CCOEFF_NORMED) # nesne tespitini başlatalım
        
        threshold = 0.8 # eşik değeri 
        
        eslesen_alan = np.where(sonuc>=threshold) # eşleşen alanı numpy dizisinde saklıyalım
        print(eslesen_alan)
        
        for x in zip(*eslesen_alan[::-1]): # eşleşen alanı dikdörtgen içine alalım
            cv2.rectangle(goruntu,x,(x[0]+h,x[1]+w),(0,255,0),2)
        
        cv2.imshow('Görüntü-I',goruntu) # görüntüyü ekrana aktaralım
         
        if(cv2.waitKey(25) & 0xFF == ord('q')):
            break
            
            
baglanti.release()
cv2.destroyAllWindows()

