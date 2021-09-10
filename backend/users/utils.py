# from django.core.mail import EmailMessage
# import threading


# class EmailThread(threading.Thread):

#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()


# # aqui é onde define as tarefas do programa, no caso enviar e-mail.
# class Util:
#     @staticmethod # isso ajuda a usar metodo de classe sem instanciar a classe em si.
#     def send_email(data):
#         email = EmailMessage(
#             subject=data['email_subject'], body=data['email_body'], to=[data['to_email']]) # no 'to' pode-se definir uma lista de destinatários
#         EmailThread(email).start()



import smtplib
import email.message
# import email_settings
from django.conf import settings

## codigo python para envio de emails
## Autor: Adriano Machado
## Turma Entra 21
## Data 08 de set de 2021

class Util:
    def send_email(assunto, corpo_email, destinatario): 
        """ Esta função envia emails utilizando a conta do Gmail """ 
        
        # Criar a mensagem com assunto, destinatário e remetente
        msg = email.message.Message()
        msg['Subject'] = assunto 
        msg['From'] = "EasyDrink <{}>".format(settings.GMAIL_FROM)
        msg['To'] = ", ".join([destinatario]) 

        # Define o cabeçario do e-mail
        msg.add_header('Content-Type', 'text/html')

        # Define o corpo do e-mail
        msg.set_payload(corpo_email)

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
  