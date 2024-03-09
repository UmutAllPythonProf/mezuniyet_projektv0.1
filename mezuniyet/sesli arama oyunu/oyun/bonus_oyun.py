from time import *
import time
from microphone import *
import speech_recognition as sr
from random import *
import random

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)




























































































































































































######################kolay= ["dairy", "mouse", "computer"]

orta= ["programming", "algorithm", "developer"]

zor= ["neural network", "machine learning", "artificial intelligence"]




while True:
    puan = int(0)

    cvp1 = input("Mod Seçin ")

    def on_message():
        
        if cvp1=="kolay" :
            print("Pekala")
            time.sleep(1)
            print("Kolay Mod Yükleniyor ..." * 3)
            time.sleep(2)

            print("Şimdi Sana Söyledğiğm Kelimeyi Telafuz Et")
            time.sleep(1)
            kelime = random.randint(kolay)
            print("Kelime : {}".format({kelime}))
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Kelimeyi Söyle")
                audio = r.listen(source)
                
                if audio==kelime:
                    puan += 1
                    print("!!! Doğru, Tebrikler !!!")
                else:
                    print("Maalesef Yanlış Cevap Verdiniz")

        elif cvp1=="orta":
            print("Pekala")
            time.sleep(1)
            print("Orta Mod Yükleniyor ..." * 3)
            time.sleep(2)

            print("Şimdi Sana Söyledğiğm Kelimeyi Telafuz Et")
            time.sleep(1)
            kelime = random.randint(orta)
            print("Kelime : {}".format({kelime}))
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Kelimeyi Söyle")
                audio = r.listen(source)
                
                if audio==kelime:
                    puan += 2
                    print("!!! Doğru, Tebrikler !!!")
                else:
                    print("Maalesef Yanlış Cevap Verdiniz")

        elif cvp1=="zor":
            print("Pekala")
            time.sleep(1)
            print("Zor Mod Yükleniyor ..." * 3)
            time.sleep(2)

            print("Şimdi Sana Söyledğiğm Kelimeyi Telafuz Et")
            time.sleep(1)
            kelime = random.randint(zor)
            print("Kelime : {}".format({kelime}))
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Kelimeyi Söyle")
                audio = r.listen(source)
                
                if audio==kelime:
                    puan += 1
                    print("!!! Doğru, Tebrikler !!!")
                else:
                    print("Maalesef Yanlış Cevap Verdiniz")
        

    




