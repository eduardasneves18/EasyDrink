import smtplib
import email.message
from django.conf import settings


class Util:
    def send_email(subject, email_body, addressee): 
        """ Esta função envia emails utilizando a conta do Gmail """ 
        
        # Criar a mensagem com assunto, destinatário e remetente
        msg = email.message.Message()
        msg['Subject'] = subject
        msg['From'] = "EasyDrink <{}>".format(settings.GMAIL_FROM)
        msg['To'] = ", ".join([addressee]) 

        # Define o cabeçario do e-mail
        msg.add_header('Content-Type', 'text/html')

        # Define o corpo do e-mail
        msg.set_payload(email_body)

        # Define a senha
        password = settings.GMAIL_SENHA

        # Define o SMTP do GMAIL
        s = smtplib.SMTP(settings.GMAIL_SMTP)

        # Inicia a conexão
        s.starttls()

        # Realiza o login utilizando usuário e senhas do settings.
        s.login(settings.GMAIL_FROM, password)

        # Envia o e-mail em codificação utf-8
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  