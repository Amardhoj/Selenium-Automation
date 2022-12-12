from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service =  Service(executable_path="D:\Pycharm\FirstProg\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com/maps/@22.4803835,88.3530736,15z")
sleep(2)

def searchplace():
    Place = driver.find_element(By.CLASS_NAME, "mL3xi")
    Place.send_keys("New Delhi")
    Submit = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
    Submit.click()
searchplace()

def directions():
    sleep(5)
    directions = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span")
    directions.click()
directions()

def find():
    sleep(5)
    find = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys("Siliguri")
    sleep(5)
    search = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()

def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
    print("TotalKilometers:", Totalkilometers.text)
    sleep(5)
    Car = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    print("Car Travel:", Car.text)
    sleep(5)
    Train = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[2]/div[1]/div[2]/div[1]/div")
    print("Train Travel:", Train.text)
    sleep(5)
kilometers()
