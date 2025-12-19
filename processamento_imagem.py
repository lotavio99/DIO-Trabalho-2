from PIL import Image
import os
import numpy as np

relative_path = os.path.dirname(os.path.abspath(__file__))

# Carregar a imagem colorida
imagem_colorida = Image.open(os.path.join(relative_path, "imagens", "a processar", "lena.png"))

# Converter imagem para array NumPy
img_array = np.array(imagem_colorida)

# Separar os canais RGB
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

# Converter para tons de cinza (0 a 255)
imagem_cinza = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

# Converter para imagem PIL (cinza)
img_cinza_pil = Image.fromarray(imagem_cinza)
img_cinza_pil.save(os.path.join(relative_path, "imagens", "processado", "lena_cinza.png"))

# Definir limiar para binarização
limiar = 127

# Binarização (0 ou 255)
imagem_binaria = np.where(imagem_cinza >= limiar, 255, 0).astype(np.uint8)

# Converter para imagem PIL (binária)
img_binaria_pil = Image.fromarray(imagem_binaria)
img_binaria_pil.save(os.path.join(relative_path, "imagens", "processado", "lena_binaria.png"))

print("Processo concluído com sucesso!")
