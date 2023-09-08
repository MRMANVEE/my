
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def email_reminders(to_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'vsk05032000@gmail.com'  
    sender_password = 'jxekouqqxcozjayd'  

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending reminder: {e}")

if __name__ == "__main__":
    recipient_email = "koushikmanisha1302@gmail.com"

    today = datetime.date.today()
    reminder_message = f"Hello Manisha!\n\nThis is a very Strict reminder About your Marks we need to know your semister Marks list kindly ""Submit"" your marks list at our collage office room please kindly follow your Collage rules{today}.\n\nBest Regards,\n OU Law Collage"

    email_reminders(recipient_email, "Reminder: Upcoming Event", reminder_message)



