import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kontrast_genişletme(görüntü):
    # Orijinal görüntünün minimum ve maksimum piksel değerlerini bul
    min_değer = np.min(görüntü)
    max_değer = np.max(görüntü)
    
    # Yeni Min ve Max değerlerini belirle (genellikle 0-255 arası)
    yeni_min = 0
    yeni_max = 255
    
    # Yeni görüntü matrisi oluştur
    genişletilmiş_görüntü = np.zeros_like(görüntü)
    
    # Kontrast genişletme işlemini uygula
    for i in range(görüntü.shape[0]):
        for j in range(görüntü.shape[1]):
            genişletilmiş_görüntü[i, j] = (görüntü[i, j] - min_değer) * ((yeni_max - yeni_min) / (max_değer - min_değer)) + yeni_min
            
    return genişletilmiş_görüntü

# Excel dosyasının tam yolunu belirle
excel_dosyası = "/home/simge/Downloads/soru1_2_data.xlsx"  # Linux'ta örnek bir yol

# Excel dosyasını oku
df = pd.read_excel(excel_dosyası)

# Veriyi NumPy dizisine dönüştür
veri = df.values

# Kontrast genişletme işlemini uygula
genişletilmiş_veri = kontrast_genişletme(veri)

# Sonuçları çıktı olarak göster
print("Orijinal Veri:")
for row in veri:
    for val in row:
        print(f"{val:3}", end=' ')
    print()

print("\nKontrast Genişletilmiş Veri:")
for row in genişletilmiş_veri:
    for val in row:
        print(f"{val:3}", end=' ')
    print()

# Sonuçları görselleştir
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Orijinal Veri")
plt.imshow(veri, cmap='viridis')  # Renkli bir harita kullan

plt.subplot(1, 2, 2)
plt.title("Kontrast Genişletilmiş Veri")
plt.imshow(genişletilmiş_veri, cmap='viridis')  # Renkli bir harita kullan

plt.show()