from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sefereliyevelmir33@gmail.com'
app.config['MAIL_PASSWORD'] = 'elmir2003'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/mail-gonder/')
def mailgonder():
    try:
        msg = Message("Salam Bu mail avtomatik olaraq flask ilə göndəriləcək",
          sender="sefereliyevelmir33@gmail.com",
          recipients=["safaraliyeva.shams@gmail.com"])
        msg.body = "Bu Python ilə mail yollama aplikasiyasl üçün bir sınaqdır\n\nƏgər bu mail sizə çatıbsa deməli program işləyir. Zəhmət olmasa mənə xəbər verin."           
        mail.send(msg)
        return 'Mail başarıyla gönderildi!'
    except Exception as e:
        return(str(e)) 

if __name__ == '__main__':
   app.run(debug = True)