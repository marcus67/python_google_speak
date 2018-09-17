# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

import requests
import locale


# See http://archive.is/OgeSS
GOOGLE_URL = "http://translate.google.com/translate_tts"

class SpeechGenerator(object):
    
    def __init__(self, p_locale=None):
        
        self.locale = p_locale
        
        if self.locale is None:
            self.locale = locale.getdefaultlocale()[0]
            
            
    def generate_audio_data(self, p_text):
        
        params = {
            "ie" : "UTF-8",
            "client" : "tw-ob",
            "q": p_text,
            "tl": self.locale}
        
        try:
            result = requests.get(url=GOOGLE_URL, params=params)
            
        except Exception as e:
            raise Exception("Exception '%s' while retrieving audio file from Google for text '%s' " %
                            ( str(e), p_text ) )
            
        if result.status_code != 200:
            raise Exception("HTTP status code %d while retrieving audio file from Google for text '%s' " %
                            ( result.status_code, p_text ) )
            
        return result.content
        

    
    
