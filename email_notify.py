import os
import smtplib
from email.mime.text import MIMEText

# Read environment variables
email_destino = os.getenv("EMAIL_DESTINO")
smtp_user = os.getenv("SMTP_USER")
smtp_pass = os.getenv("SMTP_PASS")
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Corpo do e-mail
msg = MIMEText("🚀 Pipeline executado com sucesso (ou não)! Confira o GitHub Actions para mais detalhes.")
msg["Subject"] = "📣 Notificação de Pipeline"
msg["From"] = smtp_user
msg["To"] = email_destino

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        print("✅ Email enviado com sucesso.")
except Exception as e:
    print("❌ Falha ao enviar email:", e)
    exit(1)
