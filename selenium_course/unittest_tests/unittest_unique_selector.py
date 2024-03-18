from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest

from script_unique_selector import registration



class TestRegistration(unittest.TestCase):
    correct = "Congratulations! You have successfully registered!"

    def test_registration1(self):
        welcome_text = registration(1)
        self.assertEqual(self.correct, welcome_text, "Text is wrong")

    def test_registration2(self):
        welcome_text = registration(2)
        self.assertEqual(self.correct, welcome_text, "Text is wrong")



if __name__ == "__main__":
    unittest.main()