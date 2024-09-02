import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = 'jouozyfn7gn3sa2o@ethereal.email'
    login = 'jouozyfn7gn3sa2o@ethereal.email'
    password = 'S72NusVznrfDYRUk7K'

    msg = MIMEMultipart()
    msg['from'] = "viagens_confirmar@email.com"
    msg['to'] = ', '.join(to_addrs)

    msg['Subject'] = "Confirmação de viagens"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", port=587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()