import os

types = ['jpeg']

# Usa 'Documents', não 'Documentos'
base_path = os.path.expanduser('~')
path = os.path.join(base_path, 'Downloads')

# Garante que o diretório existe
if not os.path.exists(path):
    raise FileNotFoundError(f"Diretório não encontrado: {path}")

# Muda o diretório de trabalho
os.chdir(path)

# Lista de arquivos no diretório atual
full_list = os.listdir()

# Cria as pastas se não existirem
for type_ in types:
    if not os.path.exists(type_):
        os.mkdir(type_)

# Move os arquivos para as respectivas pastas
for file in full_list:
    for type_ in types:
        if file.lower().endswith('.' + type_):
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type_, file)
            os.replace(old_path, new_path)
