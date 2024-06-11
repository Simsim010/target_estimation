# Verilen histogram verileri
yoğunluk_değerleri = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
piksel_sayıları = [12, 18, 32, 48, 52, 65, 55, 42, 32, 16, 10, 5, 18, 25, 32, 40, 65, 43, 32, 20, 10, 4]

# Başlangıç eşik değeri T0 ve eşikleme sabiti
T0 = 100
eşikleme_sabiti = 1

# Global eşikleme fonksiyonu
def global_esikleme(yoğunluk_değerleri, piksel_sayıları, T0, eşikleme_sabiti):
    while True:
        # G1 ve G2 gruplarının toplam yoğunluk ve piksel sayıları
        g1_toplam_yoğunluk = 0
        g1_toplam_piksel = 0
        g2_toplam_yoğunluk = 0
        g2_toplam_piksel = 0

        # Görüntüyü iki gruba ayırma
        for i in range(len(yoğunluk_değerleri)):
            if yoğunluk_değerleri[i] > T0:
                g1_toplam_yoğunluk += yoğunluk_değerleri[i] * piksel_sayıları[i]
                g1_toplam_piksel += piksel_sayıları[i]
            else:
                g2_toplam_yoğunluk += yoğunluk_değerleri[i] * piksel_sayıları[i]
                g2_toplam_piksel += piksel_sayıları[i]

        # Ortalama yoğunluk değerlerini hesaplama
        m1 = g1_toplam_yoğunluk / g1_toplam_piksel if g1_toplam_piksel != 0 else 0
        m2 = g2_toplam_yoğunluk / g2_toplam_piksel if g2_toplam_piksel != 0 else 0

        # Yeni eşik değeri T1'i hesaplama
        T1 = (m1 + m2) / 2

        # Eşik değeri değişiminin eşikleme sabitinden küçük olup olmadığını kontrol etme
        if abs(T1 - T0) < eşikleme_sabiti:
            return T1
        else:
            T0 = T1

# Optimum eşik değerini hesaplama
optimum_esik_değeri = global_esikleme(yoğunluk_değerleri, piksel_sayıları, T0, eşikleme_sabiti)
print(f"Optimum eşik değeri: {optimum_esik_değeri}")