NGROK TUNNEL TRACKER

(SRB) - Serbian Language

(ENG) - English language


(SRB) -NGROK TUNNEL TRACKER - O APLIKACIJI

Aplikacija uradjena u Pythonu3, prati status tunela kreiranim pokretanjem aplikacije ngrok

Najpre je neophodno kreirati nalog na ngrok platformi https://ngrok.com/

Skinuti aplikaciju, i pratiti uputstva na stranici za pokretanje.


Ngrok tunelira aplikacije koje se pokrecu na localhostu, na nekom portu, generisuci proizvoljni URL.

Svakog puta kada se pokrene ngrok, uvek kreira novi tunel sa novim generickim URL-om

Aplikacija tunnel_tracker, prati trenutno aktivni tunel, belezi ga u direktorijum tunnels, unutar fajla tunnel_url.txt i salje na email adresu.

Ukoliko ne postoji direktorijum ili fajl, aplikacija ga sama kreira, i upisuje URL tunela.

Glavni fajl je app_tracker.py, on je minimalni fajl, od koga se kreira linux servis pokretanjem shell skripta create-service.sh

Ostala dva fajla app_tracker_descriptive_srb.py i app_tracker_descriptive_eng.py su fajlovi za otklanjanje gresaka i testiranje koda, posto sadrze print() funkcije i komentare, za razliku od glavnog aplikativnog fajla koji je minimalan.


INSTALACIJA

Najpre je neophodno dodeliti pravo egzekucije fajlu create-service.sh

sudo chmod +x create-service.sh

Nakon ovoga pokrenuti fajl create-service.sh . Ovaj fajl ce na osnovu glavnog aplikativnog fajla app_tracker.py kreirati linux servis, pokrenuti ga, testirati ga, i omoguciti njegovo automatsko pokretanje sa pokretanjem sistema,

./create-service.sh



(ENG) -NGROK TUNNEL TRACKER - ABOUT 

Application is build in Python3 language. it monitoring tunnel status, created in ngrok application.

First, it's need to create account at ngrok platform https://ngrok.com/

Download app, and folow instructions on the page.

Ngrok tunneling applications which runs on localhost, on some port, generating random URL.

Every time, when you start ngrok, it's create new tunnel, with new URL.

Application tunnel_tracker , tracks temporary active tunnel, writes it in directory tunnels, inside file tunnel_url.txt, and sends it on email.

If directory or file doesn't exists, it creates them , and, write URL inside that file, 

Main file of app is app_tracker.py, it is minimal file, which is used to create linux service by running create-service.sh shell script.

Other two files are app_tracker_descriptive_srb.py and app_tracker_descriptive_eng.py, and they are files for more informations about program, and could been used for debuging, because they are contain comments, and print() functions.



INSTALLATION

First, at all, you should give execution permision to the file create-service.sh

sudo chmod +x create-service.sh


After that, you should run create-service.sh . This file will create linux service based on the app-tracker.py, automaticaly start that service, test (give status of that service), and enables it on boot.

./create-service.sh




