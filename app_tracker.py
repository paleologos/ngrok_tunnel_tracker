import subprocess
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#Send mail function
def sendmail(tunn):
    mail_content = f" <h1 style='color:purple'>New NGROK Tunnel generated: {tunn}</h1> "
    #The mail addresses and password
    sender_address = 'SENDER@gmail.com'
    sender_pass = 'GOOGLE APPLICATION PASWORD'
    receiver_address = 'RECIEVER@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'New NGROK tunnel'   
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    #print('Mail Sent')

# putanja do direktorujuma
dir_path="./tunnels"

p = subprocess.Popen("curl localhost:4040/api/tunnels ", stdout=subprocess.PIPE,  stderr=None, shell=True)
result = p.communicate()[0].decode('utf-8')

#  Upisivanje URL-a tunela

#Da li postoji tunel
#Tunel postoji
if len(result) >0 :
    res=json.loads(result)
    tunnel_url=res["tunnels"][0]["public_url"]

    # ako direktorijum ne postoji
    if(os.path.isdir(dir_path) is False):
            os.mkdir(dir_path)
            with open(f"{dir_path}/tunnel_url.txt", "w") as f:
                f.write(tunnel_url+"\n")
                sendmail(tunnel_url)
    else:
        # direktorijum postoji
        # da li fajl unutar njega postoji
        if os.path.exists(f"{dir_path}/tunnel_url.txt"):
            #fajl postoji
            with open(f"{dir_path}/tunnel_url.txt", "r+") as f:
                c=f.read()
                list_c=c.strip().split('\n')
                last_c=list_c[len(list_c)-1] 
                #da se tunel nije promenio -tunel je isti kao u fajlu
                if tunnel_url == last_c:
                    pass
                # tunel se promenio
                else:
                    f.write(tunnel_url+"\n")
                    sendmail(tunnel_url)
        else:
            #fajl unutar direktorijuma ne postoji - samim tim ni tunel
            #upis tunela
            with open(f"{dir_path}/tunnel_url.txt", "w") as f:
                f.write(tunnel_url+"\n")
                sendmail(tunnel_url)
# Tunel ne postoji
else:
    pass
   