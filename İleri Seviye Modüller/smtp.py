import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "ketenerhan2006@gmail.com"
mesaj["To"] = "ketenerhan2006@gmail.com"

mesaj["Subject"] = "TEST"

yazi = """

SMTP ile mail gönderme

-Ahmet Erhan Keten-

"""

mesaj_body = MIMEText(yazi , "plain")

mesaj.attach(mesaj_body)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("ketenerhan2006@gmail.com","*********")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("mail yollandı")

    mail.close()

except Exception as e:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()
    print(e)