from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotnet import load_dotenv
from beautifulsoup4 import BeautifulSoup

load_dotenv()
# Credentials and constants

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdArTm_S2cJLmRHQUb1L-zjp6Wwnu1TUgsJnv9dlZzfIwDrWA/viewform?usp=header"