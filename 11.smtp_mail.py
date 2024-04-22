"""EXEMPLO DE ENVIO DE E-MAIL"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "eng.edmar@gmail.com"
TO = ["eng.edmar@gmail.com"]
SUBJECT = "Meu e-mail via python"
TEXT = """\
Este é um e-mail teste.
"""

# SMTP - esse protocolo exige esse formato de metadados
message = """\
From: {FROM}
To: {TO}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))