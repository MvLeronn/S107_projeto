import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email):
    subject = "Pipeline Executado"
    body = "Pipeline executado com sucesso"
    from_email = os.getenv('FROM_EMAIL', '').replace('\xa0', '').strip()
    password = os.getenv('EMAIL_PASSWORD', '').replace('\xa0', '').strip()

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Alterar para 'utf-8' ao invés de 'plain'
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

if __name__ == "__main__":
    commit_author_email = os.getenv('COMMIT_AUTHOR_EMAIL')
    
    # Remover espaços não separáveis e outros caracteres não ASCII
    commit_author_email = commit_author_email.replace('\xa0', ' ').strip()

    print(f"Commit Author Email (sanitizado): {commit_author_email}")
    send_email(commit_author_email)

