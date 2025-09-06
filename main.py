import cv2
import numpy as np
import requests
from io import BytesIO
from matplotlib import pyplot as plt

# URL da imagem
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Museu_Hist%C3%B3rico_Nacional_%286342998263%29.jpg/640px-Museu_Hist%C3%B3rico_Nacional_%286342998263%29.jpg"

# Cabeçalho com User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Baixar a imagem
response = requests.get(url, headers=headers)
if response.status_code == 200:
    image_bytes = BytesIO(response.content)
    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
else:
    raise Exception(f"Erro ao baixar imagem: {response.status_code}")

# Converter para escala de cinza (para alguns filtros)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Filtros
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
mean = cv2.blur(img, (5, 5))  # média móvel
median = cv2.medianBlur(img, 5)
canny = cv2.Canny(img, 100, 200)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
sobel = cv2.magnitude(sobelx, sobely)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Organizar para exibição
images = [
    ("Original", cv2.cvtColor(img, cv2.COLOR_BGR2RGB)),
    ("Gray", gray),
    ("Gaussian Blur", gaussian),
    ("Média Móvel", mean),
    ("Mediana", median),
    ("Canny", canny),
    ("Sobel", sobel),
    ("Threshold", thresh)
]

# Exibir
plt.figure(figsize=(15, 10))
for i, (title, image) in enumerate(images):
    plt.subplot(2, 4, i + 1)
    cmap = "gray" if len(image.shape) == 2 else None
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
