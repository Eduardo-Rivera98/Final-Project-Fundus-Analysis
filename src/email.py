import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv()


def enviaMail(patient_name,email,option):
    """configurando correo"""
    key = os.getenv("emailpassword")
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Eye Fundus Analysis Results'
    message['From'] = 'eyefundusdetection@gmail.com'
    message['To'] = email
    receptor = email

    # PARA ENVIAR EL ARCHIVO ADJUNTO
    nombre_adjunto = "Resultados"
    file_name = f'{patient_name} - {option}'
    archivo_adjunto = open(f"PDFs/{file_name}.pdf", 'rb')
    # Creamos un objeto MIME base
    message.attach(MIMEText('Here are your eye fundus analysis results', 'plain'))
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    #Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', f"attachment; filename= {nombre_adjunto}.pdf",)
    # Y finalmente lo agregamos al mensaje
    message.attach(adjunto_MIME)
    text = message.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('eyefundusdetection@gmail.com', f'{key}')
    server.sendmail('eyefundusdetectionr@gmail.com', f'{receptor}', text)
    server.quit()