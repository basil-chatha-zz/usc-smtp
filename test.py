import smtplib, ssl

port = 465  # For SSL
password = ''

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.usc.edu", port, context=context) as server:
    server.login("bchatha@usc.edu", password)

print('SUCCESS!')
