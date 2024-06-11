# target_estimation - birinci.py
top atışı hedefi tespiti ve hedef vuran atışın grafiği


# manhattan distance - ikinci.py
    2. Bir web sitesini ziyaret eden 19 kişinin yaşları aşağıdaki gibidir. (Tek boyutlu uzay)
[15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
Başlangıç küme merkez değerlerini  c1=16 ve c2=22  alarak  ve mesafe için manhattan uzaklık ölçütü Distance1=|xi-c1| ve Distance2=|xi-c2| kullanarak 
Her  iterasyonda tabloyu güncelleyerek ve örneklerin hangi kümeye olduğunu belirleyerek 4 iterasyon sonucunda ortaya çıkacak küme merkezlerini ve her iterasyonda elde edilecek sonuçları yazdıran program

# final1:
Ekte verilen soru1_2_data.csv dosyasındaki 32x32 lik görüntü parçacığına contrast strecthing yöntemini iç içe döngüler kullanarak  uygulayınız. Elde ettiğiniz matrisi çıktı olarak veriniz (L=256) 

# final2
Ekte verilen soru1_2_data.csv dosyasındaki 32x32 lik görüntü parçacığına aşağıda örneği verilmiş şekilde ara tabloları da çıktı olarak göstererek contrast equalisation yöntemini uygulayınız. Elde ettiğiniz matrisi çıktı olarak veriniz

# final3
Ekte soru3_data.csv dosyasında verilen 32x32 lik görüntü parçacığına aşağıda Gauss yumuşatma filtresini iç içe döngüler kullanarak  uygulayınız. Elde ettiğiniz matrisi çıktı olarak veriniz. (çıktı görüntü boyutu 30x30 olacak)

# final4
    4. Aşağıda histogramı verilen görüntünün histogramı için aşağıda adımları verilmiş şekilde global eşikleme yöntemini uygulayınız. Başlangıç eşik değeri  T0= 100 olarak alınız ve thresholdu=1 olarak seçiniz. (while döngüsü kullanılacak). Optimum eşik değerini yazdırın. 

1. Başlangıçta, bir T0 global eşik tahmini seçin.
2. Döngü başlatın:
    3.1 T0 kullanarak görünüyü iki gruba ayırın: G1 ve G2.
        G1: T'den büyük yoğunluk değerlerine sahip pikseller.
        G2: T değerine sahip pikseller.
    3.2 G1 ve G2'deki piksellerin ortalama yoğunluk değerlerini hesaplayın ve m1 ve m2'ye atayın.
    3.3 Yeni bir eşik değeri T1 hesaplayın: (m1 + m2) / 2
    3.4 Eğer |T1 - T0| < threshold ise:
        3.4.1 Algoritmayı sonlandırın.
    3.5 Aksi takdirde, T0'ı T1'e eşitleyin ve döngüyü devam ettirin.


# final5

Aşağıda histogramı verilen görüntünün histogramı için Otsu eşikleme yöntemini aşağıda açıklamalarda verilen şekilde uygulayarak en uygun eşik değerini belirleyerek yazdırın
