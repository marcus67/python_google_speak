# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

import unittest
import io
import os.path

from python_google_speak import speech_generator

TEXT_EN = "hello"
TEXT_DE = "hallo"

MP3_PREFIX = b'\xff\xf3D\xc4\x00'

class TestGoogleSpeak(unittest.TestCase):

    def test_creation(self):

        gs = speech_generator.SpeechGenerator()
        self.assertIsNotNone(gs)

    def setUp(self):

        self.base_dir = os.path.dirname(__file__)

    def test_generate_english(self):

        gs = speech_generator.SpeechGenerator(p_locale="en_US")
        self.assertIsNotNone(gs)

        sound = gs.generate_audio_data(p_text=TEXT_EN)
        self.assertIsNotNone(sound)

        self.assertEqual(sound[0:len(MP3_PREFIX)], MP3_PREFIX)

    def test_generate_german(self):

        gs = speech_generator.SpeechGenerator(p_locale="de_DE")
        self.assertIsNotNone(gs)

        sound = gs.generate_audio_data(p_text=TEXT_DE)
        self.assertIsNotNone(sound)

        self.assertEqual(sound[0:len(MP3_PREFIX)], MP3_PREFIX)


    @unittest.skipIf(os.getenv("SKIP_AUDIO_COMPARISON") is not None, "No comparison of generated audio")
    def test_spoken_english(self):

        gs = speech_generator.SpeechGenerator(p_locale="en_US")
        self.assertIsNotNone(gs)

        sound = gs.generate_audio_data(p_text=TEXT_EN)

        with io.open(os.path.join(self.base_dir, "data/hello.mp3"), "rb") as f:
            ref_sound = f.read()

        self.assertEqual(sound, ref_sound)

    @unittest.skipIf(os.getenv("SKIP_AUDIO_COMPARISON") is not None, "No comparison of generated audio")
    def test_spoken_german(self):

        gs = speech_generator.SpeechGenerator(p_locale="de_DE")
        self.assertIsNotNone(gs)

        sound = gs.generate_audio_data(p_text=TEXT_DE)

        with io.open(os.path.join(self.base_dir, "data/hallo.mp3"), "rb") as f:
            ref_sound = f.read()

        self.assertEqual(sound, ref_sound)
