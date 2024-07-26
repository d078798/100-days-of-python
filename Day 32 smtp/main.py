# smtp.gmail.com
# smtplib.SMTP("smtp.gmail.com", port=587)
import smtplib
my_email = "d078798.codes@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com",587,timeout=120])
password = "abcd1234"
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email, to_addrs="d078798.codes@outlook.com", msg="Hello")
connection.close()