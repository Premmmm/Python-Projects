import speech_recognition as sr
import webbrowser as wb
import requests as req
import smtplib
import sys

try:

    r1 = sr.Recognizer()
    r2 = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening Speak now')
        audio = r1.listen(source)

    if 'ahhhhhh' or 'help' or 'Help' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        # site url where you can get your address with your ip address
        res = req.get('https://ipinfo.io/')
        data = res.json()

        city = data['city']
        location = data['loc'].split(',')
        location1 = data['loc']
        cord = 'Help needed !!!\n\nLatitude: {} \nLongitude: {}'.format(
            location1[0:7], location1[8:])

        latitude = location[0]
        longitude = location[1]
        print('City: {a} \nLatitude: {b} \nLongitude: {c}'.format(
            a=city, b=latitude, c=longitude))
        message = 'City: {}\nLatitude: {}\nLongitude: {}'.format(
            city, latitude, longitude)

        sender_mail = ""  # enter sender email here
        receiver_mail = ""  # enter reciever email here
        passsword = ""  # enter sender password here
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, passsword)
        print('login success')
        server.sendmail(sender_mail, receiver_mail, cord)
        print("email sent !")

    else:
        print('INVALID KEYWORD')

except:
	print("Unexpected exception:", sys.exc_info()[0])
