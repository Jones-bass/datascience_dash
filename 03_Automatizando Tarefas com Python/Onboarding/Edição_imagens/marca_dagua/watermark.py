from PIL import Image
import os

# --- Caminhos ---
base_dir = r'D:\Search\dashboard_python\03_Automatizando Tarefas com Python\Onboarding\Edição_imagens\marca_dagua'
files_path = os.path.join(base_dir, 'fotos')       # Pasta das fotos
image_open = os.path.join(base_dir, 'open')        # Pasta onde está a marca d'água
image_path = os.path.join(base_dir, 'watermark_ok')# Pasta de saída

# Caminho completo da marca d’água
watermark_path = os.path.join(image_open, 'images.png')
watermark = Image.open(watermark_path).convert("RGBA")
width_w, height_w = watermark.size

# Criar pasta de saída se não existir
os.makedirs(image_path, exist_ok=True)

# Coletar as fotos (jpg/jpeg/png)
files = [f for f in os.listdir(files_path) if f.lower().endswith(('jpg', 'jpeg', 'png'))]

# Margem em pixels
margin = 100

# Iterar sobre as fotos e inserir a marca d'água
for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(image_path, file)

    image = Image.open(file_path).convert("RGBA")
    width, height = image.size

    # Redimensionar a marca d'água proporcionalmente
    base_width = int(width * 0.2)
    wpercent = base_width / float(width_w)
    hsize = int(float(height_w) * wpercent)

    watermark_resized = watermark.resize((base_width, hsize), Image.LANCZOS)

    # Posição com margem
    position = (width - base_width - margin, height - hsize - margin)

    # Criar cópia da imagem e colar a marca d'água
    image_with_watermark = image.copy()
    image_with_watermark.paste(watermark_resized, position, watermark_resized)

    # Salvar como JPEG
    image_with_watermark.convert("RGB").save(new_path, "JPEG", quality=95)

print("Marca d'água aplicada com sucesso!")
