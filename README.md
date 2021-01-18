# Realtime nesne tespiti
Merhaba bu uygulamada Template Matching tekniği kullanılarak Python dilinde nesne tespiti anlatılmaya çalışılmıştır.

### Template Matching

 - Template Matching (Şablon Eşleştirme) yöntemi ile nesne tanıma daha çok kaynak bir görüntü üzerinde bir şablonu aramak için kullanılır.

- Template Matching yöntemi ile kaynak görsel üzerinde aranan şablon Sliding window (Kayan,sürgülü pencere) yöntemi ile aranır.

- Kaynak üzerinde şablon (1,1) koordinatlarına oturtulur ve tüm pikseller üzerinde dönülür, kullandığınız benzerlik yöntemine göre bir benzerlik oranı oluşturulur ve şablonunuz ile o anki dönülen şablon benzer ise sonuç olarak size o pikselleri döndürür.


##### Simule edilmesi
![image](https://user-images.githubusercontent.com/77530565/104892990-ec997580-5983-11eb-855c-2cf2f535eef1.png)

- uTemplate Matching yönteminde kaynak ile şablonu eşleştirirken kullanılan farklı yöntemler vardır. Bu yöntemler aşağıdaki gibidir.

		•  TM_CCOEFF

		•  TM_CCOEFF_NORMED

		•  TM_CCORR

		•  TM_CCORR_NORMED

		•  TM_SQDIFF

		•  TM_SQDIFF_NORMED

		*Bu yöntemlerin her birinin farklı bir matematiksel formül olduğunu unutulmamalıdır.





