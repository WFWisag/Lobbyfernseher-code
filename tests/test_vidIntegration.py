import unittest
import os
import src.writeInHTML as wih

class TestWriteInHTML(unittest.TestCase):
    
        def test_getReplacedTag(self):
            self.assertEqual(wih.getReplacedTag(), ("<img class='folie' src='1.jpg' />", "img"))
            self.assertEqual(wih.getReplacedTag(), ("<video class='folie' src='1.mp4' autoplay></video>", "vid"))

        def test_getFileType(self):
            self.assertEqual(wih.getFileType("1.jpg"), "img")
            self.assertEqual(wih.getFileType("1.mp4"), "vid")

        def test_getVideoDuration(self):
            self.assertEqual(wih.getVideoDuration("file_example_MP4_1920_18MG.mp4"), 30)