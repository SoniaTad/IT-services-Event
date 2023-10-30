from flask import Flask, render_template , request
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
app = Flask(__name__)


sender = ''

password = ''


    
@app.route("/")
def main():
    return render_template('Welcome2.html')
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
       message=request.form['contents']
       message2=request.form['email']

       msg = MIMEMultipart()
       msg['From'] = 'sender@email'  #will need to add the email of the sender 
       msg['To'] = message2
       msg['Subject'] = 'ITs summer event'
       msg.attach(MIMEText(body, 'plain'))
       pdfname = 'Docker&kubernetes.pdf'
       binary_pdf = open(pdfname, 'rb')
       payload = MIMEBase('application', 'octate-stream', Name=pdfname)
       # payload = MIMEBase('application', 'pdf', Name=pdfname)
       payload.set_payload((binary_pdf).read())
       encoders.encode_base64(payload)
       payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
       msg.attach(payload)

       session = smtplib.SMTP('smtp.office365.com', 587)
       session.starttls()
       session.login(sender, password)
       text = msg.as_string()
       session.sendmail('sender@email', message2, text)    #change email of sender 
       session.quit()
       print('Mail Sent')
       
       

    
       

       # databese configuration 
       connection = mysql.connector.connect(
       user = 'root',
       password = 'root',
       host= 'db',
       port = '3306',
       database = 'staff'
       )
       cursor = connection.cursor()
       #cursor.execute('TRUNCATE TABLE Staff_details')
       connection.commit()
       cursor.execute("INSERT INTO Staff_details (Name,Email) VALUES (%s,%s)",(message,message2))
       connection.commit()
       cursor.execute("SELECT * FROM Staff_details")
       test=cursor.fetchall()
       
       
       return render_template("Welcome.html",message=message,message2=message2,test=test)
    else:
      
      message='IT DIDNT WORK'
      return render_template("Welcome2.html",message=message)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
