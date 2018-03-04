# -*- coding: utf-8 -*-

# See http://archive.is/OgeSS

import requests
import locale
import playsound


GOOGLE_URL = "http://translate.google.com/translate_tts"

class GoogleSpeak(object):
    
    def __init__(self, p_locale=None):
        
        self.locale = p_locale
        
        if self.locale is None:
            self.locale = locale.getdefaultlocale()[0]
            
            
    def speak_to_audio_data(self, p_text):
        
        params = {
            "ie" : "UTF-8",
            "client" : "tw-ob",
            "q": p_text,
            "tl": self.locale}
        
        try:
            result = requests.get(url=GOOGLE_URL, 
                                  params=params)
            
        except Exception as e:
            raise Exception("Exception '%s' while retrieving audio file from Google for text '%s' " %
                            ( str(e), p_text ) )
            
        if result.status_code != 200:
            raise Exception("HTTP status code %d while retrieving audio file from Google for text '%s' " %
                            ( result.status_code, p_text ) )
            
        return result.content
        
        

def test():
    gs = GoogleSpeak(p_locale="de_DE")
    audio_data = gs.speak_to_audio_data(p_text="Die Bibliothek scheint korrekt installiert worden zu sein.")
    
    with open("/tmp/audio.bin", "wb") as file:
        file.write(audio_data)
        
    playsound.playsound("/tmp/audio.bin")
    
    
