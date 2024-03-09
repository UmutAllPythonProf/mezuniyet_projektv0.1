import speech_recognition as sr

def mikrofon(audio):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bir Şeyler Söylemeyi Deneyin !")
        audio = r.listen(source)


    try:
        print("Ben Google Ses Hizmetleri Ve Yapay Zeka Tabanlı Bir Dinleme Uygulaması Olarak Şunu Söylediğinizi Düşünüyorum : " + r.recognize_google(audio, language="tr-TR"))
    except sr.UnknownValueError:
        print("Ben Google Ses Hizmetleri Ve Yapay Zeka Tabanlı Bir Dinleme Uygulaması Olarak Söyledğiğnizi Anlayamadım")
    except sr.RequestError as error:
        print("Ben Ve Kendi Yapay Zekam Sonuçlarında Google Ses Hizmetleri'nden Sonuç İsteyemedim; {0}".format(error))
    
