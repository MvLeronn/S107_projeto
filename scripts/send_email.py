import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email):
    subject = "Pipeline Executado"
    body = "Pipeline executado com sucesso"
    from_email = os.getenv('FROM_EMAIL', '').strip()
    password = os.getenv('EMAIL_PASSWORD', '').strip()

    if not from_email or not password:
        raise ValueError("As variáveis de ambiente FROM_EMAIL ou EMAIL_PASSWORD não estão configuradas.")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Usar 'utf-8' na codificação do corpo do e-mail
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print(f"E-mail enviado com sucesso para {to_email}")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {str(e)}")
        raise

if __name__ == "__main__":
    commit_author_email = os.getenv('COMMIT_AUTHOR_EMAIL', '').strip()

    if not commit_author_email or 'noreply' in commit_author_email:
        raise ValueError(f"E-mail do autor do commit é inválido: {commit_author_email}")

    print(f"E-mail do autor do commit: {commit_author_email}")
    send_email(commit_author_email)
