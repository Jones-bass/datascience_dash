import imaplib
import email
import os
from datetime import datetime
from email.header import decode_header

username = "jonesbass.tb@gmail.com"
host = "imap.gmail.com"

base_dir = r"C:\Users\Jones_2\Documents\Search\datascience_dash\03_Automatizando Tarefas com Python\Onboarding\E-mail"

password_folder = os.path.join(base_dir, "passwords")
token_path = os.path.join(password_folder, "token")
download_folder = os.path.join(base_dir, "attachments")

os.makedirs(password_folder, exist_ok=True)
os.makedirs(download_folder, exist_ok=True)


def carregar_senha():
    with open(token_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def limpar_nome_arquivo(nome):
    caracteres_invalidos = '<>:"/\\|?*\r\n\t'
    for char in caracteres_invalidos:
        nome = nome.replace(char, " ")

    while "  " in nome:
        nome = nome.replace("  ", " ")

    nome = nome.strip()
    return nome or "arquivo_sem_nome.pdf"


def decodificar_nome(nome):
    if not nome:
        return "arquivo_sem_nome.pdf"

    partes = decode_header(nome)
    resultado = ""

    for texto, encoding in partes:
        if isinstance(texto, bytes):
            resultado += texto.decode(encoding or "utf-8", errors="ignore")
        else:
            resultado += texto

    return limpar_nome_arquivo(resultado)


def gerar_nome_unico(pasta, nome_arquivo):
    caminho = os.path.join(pasta, nome_arquivo)

    if not os.path.exists(caminho):
        return caminho

    base, ext = os.path.splitext(nome_arquivo)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return os.path.join(pasta, f"{base}_{timestamp}{ext}")


def baixar_pdfs():
    password = carregar_senha()

    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)

    # INBOX pega só caixa de entrada.
    # Para Gmail, tente também: "[Gmail]/Todos os e-mails" ou "[Gmail]/All Mail"
    mail.select("INBOX")

    status, mensagens = mail.search(None, "ALL")

    if status != "OK":
        print("Nenhum e-mail encontrado.")
        return

    ids_emails = mensagens[0].split()

    total_emails = len(ids_emails)
    total_anexos = 0
    total_pdfs = 0

    print(f"E-mails encontrados: {total_emails}")

    for id_email in ids_emails:
        status, dados = mail.fetch(id_email, "(RFC822)")

        if status != "OK":
            continue

        mensagem = email.message_from_bytes(dados[0][1])

        for parte in mensagem.walk():
            nome_arquivo = parte.get_filename()

            if not nome_arquivo:
                continue

            total_anexos += 1

            nome_arquivo = decodificar_nome(nome_arquivo)

            if not nome_arquivo.lower().endswith(".pdf"):
                continue

            conteudo = parte.get_payload(decode=True)

            if not conteudo:
                continue

            caminho_arquivo = gerar_nome_unico(download_folder, nome_arquivo)

            with open(caminho_arquivo, "wb") as arquivo:
                arquivo.write(conteudo)

            total_pdfs += 1
            print(f"PDF salvo: {caminho_arquivo}")

    mail.logout()

    print("\nResumo:")
    print(f"E-mails lidos: {total_emails}")
    print(f"Anexos encontrados: {total_anexos}")
    print(f"PDFs baixados: {total_pdfs}")


if __name__ == "__main__":
    baixar_pdfs()