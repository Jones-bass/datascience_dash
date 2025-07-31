import smtplib
import ssl
from email.message import EmailMessage
import os
import mimetypes

# --- Caminhos base ---
base_dir = r'D:\Search\dashboard_python\03 Automatizando Tarefas com Python\0. Onboarding\E-mail'
caminho_token = os.path.join(base_dir, 'passwords', 'token')
caminho_corpo = os.path.join(base_dir, 'corpo_email.txt')
caminho_imagem = os.path.join(base_dir, 'imagem.jpg')

# --- Dados de acesso dos emails ---
with open(caminho_token, 'r') as f:
    email_senha = f.read().strip()

email_origem = 'jonesbass.tb@gmail.com'
email_destino = 'jonesbass.tb@gmail.com'

# --- Textos do email ---
with open(caminho_corpo, 'r', encoding='utf-8') as f:
    body = f.read()

assunto = 'Orçamento de produtos'

# --- Mensagem ---
mensagem = EmailMessage()
mensagem['From'] = email_origem
mensagem['To'] = email_destino
mensagem['Subject'] = assunto
mensagem.set_content(body)

# --- Anexo ---
mime_type, _ = mimetypes.guess_type(caminho_imagem)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(caminho_imagem, 'rb') as ap:
    mensagem.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                            filename=os.path.basename(caminho_imagem))

# --- Envio seguro ---
safe = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
    print("✅ Email enviado com sucesso!")