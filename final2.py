import numpy as np
import pandas as pd

# Excel dosyasının tam yolunu belirle
excel_dosyası = "/home/simge/Downloads/soru1_2_data.xlsx"  # Linux'ta örnek bir yol

# Excel dosyasını oku
df = pd.read_excel(excel_dosyası)

# Veriyi NumPy dizisine dönüştür
veri = df.values

# Calculate the histogram
histogram = np.zeros(256, dtype=int)
for row in veri:
    for pixel in row:
        histogram[pixel] += 1

# Calculate the cumulative distribution function (CDF)
cdf = np.zeros(256, dtype=float)
for i in range(256):
    cdf[i] = np.sum(histogram[:i+1]) / np.sum(histogram)

# Transform the CDF to a uniform distribution
uniform_cdf = np.linspace(0, 1, 256)

# Map the transformed CDF to the original histogram values
transformed_histogram = np.zeros(256, dtype=int)
for i in range(256):
    transformed_histogram[i] = np.argmin(np.abs(cdf[i] - uniform_cdf))

# Apply contrast equalization
equalized_image = np.zeros_like(veri)
for row in range(veri.shape[0]):
    for col in range(veri.shape[1]):
        equalized_image[row, col] = transformed_histogram[veri[row, col]]

# Display the intermediate tables
print("Orijinal Pixel Değerleri:")
print(veri)

print("\nFrekans Değerleri:")
frequency_data = np.zeros_like(veri)
for row in range(veri.shape[0]):
    for col in range(veri.shape[1]):
        frequency_data[row, col] = histogram[veri[row, col]]
print(frequency_data)

print("\nEşitlenmiş Pixel Değerleri:")
print(equalized_image)

print("\nEşitlenmiş Pixel Değerlerinin Frekans Değerleri:")
equalized_frequency_data = np.zeros_like(veri)
for row in range(equalized_image.shape[0]):
    for col in range(equalized_image.shape[1]):
        equalized_frequency_data[row, col] = histogram[equalized_image[row, col]]
print(equalized_frequency_data)

print("\nEşitlenmiş Pixel Değerlerinin CDF Değerleri:")
equalized_cdf = np.zeros_like(veri)
for row in range(equalized_image.shape[0]):
    for col in range(equalized_image.shape[1]):
        equalized_cdf[row, col] = cdf[equalized_image[row, col]]
print(equalized_cdf)