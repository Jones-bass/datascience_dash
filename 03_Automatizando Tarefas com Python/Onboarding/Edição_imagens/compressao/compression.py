from PIL import Image
import os

# Parâmetros
reduct_fact = 0.5          # fator de redução (0.5 = 50%)
quality = 95               # qualidade JPEG de saída (0-100)
base_dir = r'D:\Search\dashboard_python\03_Automatizando Tarefas com Python\Onboarding\Edição_imagens'
files_path = os.path.join(base_dir, 'fotos')
compressed_path = os.path.join(base_dir, 'compressed_images')

# --- Verificações e criação de pastas ---
if not os.path.exists(files_path):
    raise FileNotFoundError(f"A pasta de entrada não existe: '{files_path}'. Crie-a ou ajuste o caminho.")

os.makedirs(compressed_path, exist_ok=True)

# --- Coleta de arquivos (case-insensitive) ---
valid_exts = ('.jpg', '.jpeg', '.png', '.webp')
files = [f for f in os.listdir(files_path)
         if os.path.isfile(os.path.join(files_path, f)) and f.lower().endswith(valid_exts)]

if not files:
    print("Nenhuma imagem encontrada na pasta de entrada.")
    raise SystemExit

# --- Estatísticas ---
size_antes = 0
size_depois = 0

for file in files:
    src = os.path.join(files_path, file)
    dst = os.path.join(compressed_path, os.path.splitext(file)[0] + '.jpg')  # salvar tudo como jpg

    size_antes += os.path.getsize(src)

    # Abrir imagem com Pillow
    with Image.open(src) as img:
        # Convertendo para RGB antes de salvar em JPEG (para imagens com alpha)
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            img = img.convert("RGB")

        new_w = max(1, int(reduct_fact * img.width))
        new_h = max(1, int(reduct_fact * img.height))

        # LANCZOS é a opção recomendada para downsampling (ANTIALIAS é alias antigo)
        img_resized = img.resize((new_w, new_h), Image.LANCZOS)

        # Salvar com otimização
        img_resized.save(dst, 'JPEG', optimize=True, quality=quality)

    size_depois += os.path.getsize(dst)

# --- Resultados ---
size_antes_mb = size_antes / (1024 * 1024)
size_depois_mb = size_depois / (1024 * 1024)
diferenca_mb = size_antes_mb - size_depois_mb

if size_antes > 0:
    percent = 100.0 * (size_antes - size_depois) / size_antes
else:
    percent = 0.0

print(f"Tamanho Anterior (MB): {size_antes_mb:.2f}")
print(f"Tamanho Comprimido (MB): {size_depois_mb:.2f}")
print(f"Diferença: {diferenca_mb:.2f} MB")
print(f"Redução total: {percent:.2f}%")
