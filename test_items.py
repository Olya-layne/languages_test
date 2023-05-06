import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_button(browser):
    browser.get(link)
    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    
    time.sleep(15)
    
    assert add_button is not None
    