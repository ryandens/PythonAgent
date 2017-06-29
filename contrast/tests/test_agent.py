from unittest import TestCase
import contrast

class TestContrast(TestCase):

    def test_contrast(self):
        s = contrast.test()
        self.assertEqual(s, "This is a test")