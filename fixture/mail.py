import poplib
import email
import time

class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            # stat[0] - count of mails, кортеж
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    # retr[0] - text of mails, кортеж
                    msglines = pop.retr(n+1)[1]
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg.get_payload()
            pop.quit()
            time.sleep(3)
        return None