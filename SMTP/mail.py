import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_passwords = os.getenv("MY_PASSWORD")
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_passwords)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="alijamil22334@outlook.com",
        msg="Subject:Aoa.\n\n This is the body of my email.Congrats again."
    )