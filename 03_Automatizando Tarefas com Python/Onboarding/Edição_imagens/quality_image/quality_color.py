import cv2
from PIL import Image, ImageEnhance
import os
import numpy as np

# --- Caminhos ---
base_dir = r'D:\Search\dashboard_python\03_Automatizando Tarefas com Python\Onboarding\Edição_imagens\quality_image'
files_path = os.path.join(base_dir, 'fotos')
image_path = os.path.join(base_dir, 'enhanced_images')

os.makedirs(image_path, exist_ok=True)

print(f"Pasta destino: {image_path}")
print("Existe a pasta?", os.path.exists(image_path))

files = [f for f in os.listdir(files_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(image_path, file)

    print(f"📷 Processando: {file}")
    print(f"Caminho para salvar: {new_path}")

    # Abrir imagem usando imdecode para suportar unicode no path
    try:
        with open(file_path, 'rb') as f:
            file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
            img_cv = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    except Exception as e:
        print(f"⚠ Erro ao abrir {file}: {e}")
        continue

    if img_cv is None:
        print(f"⚠ Não foi possível ler: {file}")
        continue

    if img_cv.shape[2] == 4:
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGRA2BGR)

    img_cv = cv2.fastNlMeansDenoisingColored(img_cv, None, 2, 2, 1, 12)

    h, w = img_cv.shape[:2]
    upscale_factor = 2 if max(h, w) < 1500 else 1.5
    new_size = (int(w * upscale_factor), int(h * upscale_factor))
    img_cv = cv2.resize(img_cv, new_size, interpolation=cv2.INTER_CUBIC)

    img = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    img = ImageEnhance.Brightness(img).enhance(1.1)
    img = ImageEnhance.Contrast(img).enhance(1.1)
    img = ImageEnhance.Color(img).enhance(1.1)
    img = ImageEnhance.Sharpness(img).enhance(2.0)

    try:
        img.save(new_path, "JPEG", quality=95)
        print(f"Imagem salva com sucesso: {new_path}")
    except Exception as e:
        print(f"Erro ao salvar a imagem {file}: {e}")

print("✅ Processo finalizado! Imagens salvas em:", image_path)
