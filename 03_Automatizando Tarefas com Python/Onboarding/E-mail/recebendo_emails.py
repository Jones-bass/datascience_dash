from imbox import Imbox
from datetime import datetime
import os

username = 'jonesbass.tb@gmail.com'
host = "imap.gmail.com"

base_dir = r'D:\Search\dashboard_python\03_Automatizando Tarefas com Python\Onboarding\E-mail'
download_folder = os.path.join(base_dir, 'attachments')
os.makedirs(download_folder, exist_ok=True)

# Lê a senha do arquivo
with open(os.path.join(base_dir, 'passwords', 'token'), 'r') as file:
    password = file.read().strip()

# Conecta ao e-mail
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)

# Pega todos os e-mails (sem filtros)
messages = mail.messages()

for (uid, message) in messages:
    if not message.attachments:
        continue  # pula se não tiver anexo

    for attach in message.attachments:
        file_name = attach.get('filename')
        content = attach.get('content')

        if file_name and file_name.lower().endswith('.pdf'):
            file_path = os.path.join(download_folder, file_name)

            # Se o arquivo já existe, cria um nome único
            if os.path.exists(file_path):
                base, ext = os.path.splitext(file_name)
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                file_path = os.path.join(download_folder, f"{base}_{timestamp}{ext}")
            
            with open(file_path, "wb") as fp:
                fp.write(content.read())
            
            print(f"✅ PDF salvo: {file_path}")

mail.logout()
