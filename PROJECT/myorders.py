from flask import Flask, render_template, redirect,request
# from flask_mail import Mail, Message
from .data import *

@app.route('/admin/myorders')
def order():
    myorder=Hireme.query.all()
    return render_template('/admin/myorders/myorders.html', myorder=myorder)


# Accept Order
# @app.route('/admin/myorders/accept/<email>')
# def acceptorder(email):
#     send=Hireme.query.get(email)
#     try:
#         msg = Message("Salam sifarişiniz qəbul edildi",
#             sender='sefereliyevelmir33@gmail.com',
#             recipients={{send.email}}
#         )
#         msg.body = "Ən qısa müddətdə sizinlə əlaqə saxlanılacaq"
#         mail.send(msg)
#         return redirect('/admin/myorders')
#     except Exception as e:
#         return(str(e))
        

