import smtplib, ssl

port = 465  # For SSL
password = 'Rp1m34man*'

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("basil.chatha8@gmail.com", password)

print('SUCCESS!')
