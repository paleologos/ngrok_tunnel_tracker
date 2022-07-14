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
    sender_pass = 'GOOGLE APPLICATION PASSWORD'
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
    print('Mail Sent')

# directory path
dir_path="./tunnels"

p = subprocess.Popen("curl localhost:4040/api/tunnels ", stdout=subprocess.PIPE,  stderr=None, shell=True)
result = p.communicate()[0].decode('utf-8')

#  Write tunnel  URL-a 

#If tunnel exists
if len(result) >0 :
    res=json.loads(result)
    tunnel_url=res["tunnels"][0]["public_url"]

    # If directory "tunnels" don't exists
    if(os.path.isdir(dir_path) is False):
            print("Directory  'tunnels' don't exists, creating dir...")
            print("Create file 'tunnel_url.txt'...")
            os.mkdir(dir_path)
            with open(f"{dir_path}/tunnel_url.txt", "w") as f:
                f.write(tunnel_url+"\n")
                print("Tunnel write...")
                sendmail(tunnel_url)
    else:
        # if directory exists
        # if file "tunnel_url.txt" exists inside that dir
        if os.path.exists(f"{dir_path}/tunnel_url.txt"):
            #if file uxists
            with open(f"{dir_path}/tunnel_url.txt", "r+") as f:
                # file content
                c=f.read()
                #list of all tunnels from file
                list_c=c.strip().split('\n')
                # last tunnel from file
                last_c=list_c[len(list_c)-1] 
                #if tunnel is equal as last tunnel from file
                if tunnel_url == last_c:
                    pass
                # tunnel is not equal (new tunnel)
                else:
                    print("Tunnel write...")
                    f.write(tunnel_url+"\n")
                    sendmail(tunnel_url)
        else:
            #file "tunnel_url.txt" don't exists, also tunnel do not exists
            #write tunnel
            with open(f"{dir_path}/tunnel_url.txt", "w") as f:
                print("Create file 'tunnel_url.txt'...")
                print("Tunnel write...")
                f.write(tunnel_url+"\n")
                sendmail(tunnel_url)
# There is no any tunnel
else:
    pass
   