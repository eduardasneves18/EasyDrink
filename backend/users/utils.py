from django.core.mail import EmailMessage
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


# aqui é onde define as tarefas do programa, no caso enviar e-mail.
class Util:
    @staticmethod # isso ajuda a usar metodo de classe sem instanciar a classe em si.
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']]) # no 'to' pode-se definir uma lista de destinatários
        EmailThread(email).start()