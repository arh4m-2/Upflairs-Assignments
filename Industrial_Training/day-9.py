import smtplib

#SMPT -> Simple Mail Transfer Protocol

try:
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()

    
    sender_mail = 'arkham.asylum34@gmail.com'
    sender_pass = "dodt fzje vtwb opak"

    receiver_mail = input('Enter reciever mail : ')
    subject = input('Enter Subjecet : ')
    body = input('Enter body of mail : ')

    server.login(sender_mail, sender_pass)
    
    message = f'Subject : {subject}\n\nBody : {body}'

    server.sendmail(
        from_addr=sender_mail,
        to_addrs=receiver_mail,
        msg=message
    )
    print('Email Sent Successfully')

    server.quit()

except Exception as e:
    print(e)
