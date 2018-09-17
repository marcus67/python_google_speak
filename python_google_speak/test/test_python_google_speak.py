# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

import unittest
import io

from python_google_speak import speech_generator

TEXT_EN = "hello"
TEXT_DE = "hallo"

class TestGoogleSpeak(unittest.TestCase):

    def test_creation(self):

        gs = speech_generator.SpeechGenerator()
        self.assertIsNotNone(gs)

    def test_speak_english(self):

        gs = speech_generator.SpeechGenerator(p_locale="en_US")
        self.assertIsNotNone(gs)

        sound = gs.generate_audio_data(p_text=TEXT_EN)

        with io.open("data/hello.mp3", "rb") as f:
            ref_sound = f.read()

        self.assertEqual(sound, ref_sound)

    def test_speak_english(self):

        gs = speech_generator.SpeechGenerator(p_locale="de_DE")
        self.assertIsNotNone(gs)

        sound = gs.generate_audio_data(p_text=TEXT_DE)

        with io.open("data/hallo.mp3", "rb") as f:
            ref_sound = f.read()

        self.assertEqual(sound, ref_sound)



