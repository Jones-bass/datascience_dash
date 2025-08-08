from PIL import Image
import os

base_dir = r'D:\Search\dashboard_python\03_Automatizando Tarefas com Python\Onboarding\Edição_imagens\greyscale'
files_path = os.path.join(base_dir, 'fotos')
image_path = os.path.join(base_dir, 'greyscale_images')

if image_path not in os.listdir():
    os.mkdir(image_path)

# Coletando as files
files = [i for i in os.listdir(files_path) if 'jpg' in i]

for file in files:
    # Abrindo a file e convertendo para GreyScale diretamente
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(image_path, file)
    image = Image.open(file_path).convert('L')

    # Direcionando para o folder criado (ou existente)
    image.save(new_path, 'JPEG')