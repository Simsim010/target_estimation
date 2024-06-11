import pandas as pd
import numpy as np

excel_dosyası = "/home/simge/Downloads/soru3_data.xlsx" 

df = pd.read_excel(excel_dosyası)

image = df.values

def gaussian(x, sigma):
    return 1 / (2 * np.pi * (sigma ** 2)) * np.exp(-(x ** 2) / (2 * sigma ** 2))


def gaussian_kernel(kernel_size, sigma):
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size // 2
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i - center, j - center
            
            kernel[i, j] = gaussian(np.sqrt(x ** 2 + y ** 2), sigma)
    return kernel / np.sum(kernel)

def apply_gaussian_filter(image, kernel_size, sigma):
    rows, cols = image.shape
    output_image = np.zeros((rows - kernel_size + 1, cols - kernel_size + 1))
    kernel = gaussian_kernel(kernel_size, sigma)
    for i in range(rows - kernel_size + 1):
        for j in range(cols - kernel_size + 1):
            output_image[i, j] = int(np.sum(image[i:i+kernel_size, j:j+kernel_size] * kernel))  # Tam sayıya dönüştürme
    return output_image

output_image = apply_gaussian_filter(image, kernel_size=3, sigma=1)

for row in output_image:
    print(*row)