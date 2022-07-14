import subprocess
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#Funkcija za slanje mail-a
def sendmail(tunn):
    mail_content = f" <h1 style='color:purple'>New NGROK Tunnel generated: {tunn}</h1> "
    #Mail adresa i lozinka
    sender_address = 'SENDER@gmail.com'
    sender_pass = 'GOOGLE APPLICATION PASSWORD'
    receiver_address = 'RECIEVER@gmail.com'
    #MIME konfiguracija
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'New NGROK tunnel'   
    #Telo i attachment poruke
    message.attach(MIMEText(mail_content, 'html'))
    #SMTP sesija
    session = smtplib.SMTP('smtp.gmail.com', 587) #deklarisati port gmail
    session.starttls() #bezbednost
    session.login(sender_address, sender_pass) #logovanje sa email-om i lozinkom
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail poslat')

# putanja do direktorijuma
dir_path="./tunnels"

p = subprocess.Popen("curl localhost:4040/api/tunnels ", stdout=subprocess.PIPE,  stderr=None, shell=True)
result = p.communicate()[0].decode('utf-8')

#  Upis URL-a tunela

#Tunel postoji
if len(result) >0 :
    res=json.loads(result)
    tunnel_url=res["tunnels"][0]["public_url"]

    # Direktorijum "tunnels" ne postoji
    if(os.path.isdir(dir_path) is False):
            print("Direktorijum  'tunnels' ne postoji, kreiram direktorijum...")
            print("Kreiram fajl 'tunnel_url.txt'")
            os.mkdir(dir_path)
            with open(f"{dir_path}/tunnel_url.txt", "w") as f:
                f.write(tunnel_url+"\n")
                print("Upis tunela...")
                sendmail(tunnel_url)
    else:
        # Direktorijum postoji
        # Ukoliko "tunnel_url.txt" postoji unutar tog direktorijuma
        if os.path.exists(f"{dir_path}/tunnel_url.txt"):
            #fajl postoji
            with open(f"{dir_path}/tunnel_url.txt", "r+") as f:
                # sadrzaja fajla
                c=f.read()
                #izlistavanje svih tunela iz fajla kao liste
                list_c=c.strip().split('\n')
                # zadnji tunel iz liste tunela
                last_c=list_c[len(list_c)-1] 
                #ukoliko je tunel isti kao poslednji tunel iz fajla
                if tunnel_url == last_c:
                    pass
                # tunel nije isti, generisan je novi tunel
                else:
                    print("Upis tunela...")
                    f.write(tunnel_url+"\n")
                    sendmail(tunnel_url)
        else:
            #fajl "tunnel_url.txt" ne postoji, takodje tunl ne postoji
            #upisi novi tunl
            with open(f"{dir_path}/tunnel_url.txt", "w") as f:
                print("Kreiram fajl 'tunnel_url.txt'")
                print("Upis tunela...")
                f.write(tunnel_url+"\n")
                sendmail(tunnel_url)
# Tunel ne postoji
else:
    pass
   