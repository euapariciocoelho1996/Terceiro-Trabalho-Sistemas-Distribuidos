from PIL import Image

# Função para aplicar um filtro de pixelização e converter para preto e branco
def apply_filter(image_path):
    img = Image.open(image_path)
    
    # Reduz a imagem para um tamanho menor, mas com uma redução menos agressiva
    smaller_size = (img.width // 5, img.height // 5)  # Redução suave
    img = img.resize(smaller_size, Image.NEAREST)  # Aplicando o filtro de pixelização

    # Aumenta de volta ao tamanho original
    img = img.resize((img.width * 5, img.height * 5), Image.NEAREST)  # Aumentando sem suavizar
    
    # Converte para preto e branco
    img = img.convert("L")  # "L" significa escala de cinza (grayscale)
    
    return img