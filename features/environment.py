from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from behave import use_step_matcher
import json

use_step_matcher('re')

def initialize_browser(context):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1400,900')
    chrome_options.add_argument('--disable-features=NetworkService')
    context.driver = webdriver.Chrome(chrome_options=chrome_options)

def before_all(context):
    initialize_browser(context)
    with open("environment.json", "r") as f:
        context.env = json.load(f)
