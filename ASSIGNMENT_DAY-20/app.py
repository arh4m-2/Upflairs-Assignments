from flask import Flask, render_template, url_for, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/userdata')
def userdata():
    return render_template('form.html')


@app.route('/submitdata', methods=['GET','POST'])
def submitdata():
    if request.method == "POST":
        name = request.form['name']
        branch = request.form['branch']
        receiver_mail = request.form['receiver_mail']
        message = request.form['msg']
        
        user_data = {
            'Name' : name,
            'Branch': branch,
            'Receiver Mail': receiver_mail,
            'Message': message
        }

        try:
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.starttls()

    
            sender_mail = 'arhamjainagra@gmail.com'
            sender_pass = "lqok xmqs nljl kyya"



            server.login(sender_mail, sender_pass)
    
            message = f'Subject : Mail sent from python \n\nBody : {message}'

            server.sendmail(
            from_addr=sender_mail,
            to_addrs=receiver_mail,
            msg=message
            )
            print('Email Sent Successfully')

            server.quit()

        except Exception as e:
            print(e)


        return user_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4545, debug=True)