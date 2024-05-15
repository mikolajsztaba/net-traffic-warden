import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, password):
    # Tworzenie obiektu wiadomosci
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Dodawanie tresci wiadomosci
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Ustanowienie polaczenia z serwerem SMTP Outlook/Hotmail
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()  # Uzywanie TLS do zabezpieczenia polaczenia
        server.login(from_email, password)  # Logowanie sie do serwera
        text = msg.as_string()  # Konwersja wiadomosci do formatu string
        server.sendmail(from_email, to_email, text)  # Wysylanie wiadomosci
        server.quit()  # Zamykanie polaczenia z serwerem

        print(f'Email wyslany do {to_email}')
    except Exception as e:
        print(f'Wystapil blad podczas wysylania emaila: {e}')

# Przyklad uzycia
if __name__ == "__main__":
    subject = "Testowy Email"
    body = "To jest testowa wiadomosc wyslana z klienta pocztowego w Pythonie."
    to_email = ""
    from_email = ""
    password = ""

    send_email(subject, body, to_email, from_email, password)
