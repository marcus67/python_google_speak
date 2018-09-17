# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

import playsound
import tempfile

def playback_audio_data(p_audio_blob, p_block=True):

    with tempfile.NamedTemporaryFile("wb") as f:
        f.write(p_audio_blob)
        playsound.playsound(f.name, block=p_block)
