from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




#the Beginning bits/intro
print("Made by Araav Patel | UC Berkeley | Computer Science")
print("Converted to Python 3 by Panth Shah | Fallon Middle School | 8th Grader")
print("")
print("")
welcomeMessage = "Welcome to Instacart Delivery Slot Search Tool!"
Ex = ""
Terms = ""
breakdown = ""
print (welcomeMessage)
print("")
print("")
print("Requirements: Latest Version of Google Chrome, Chrome Webdriver in path, Instacart account, pre-added payment method, pre-added address, pre-added phone number")
print("\n your instacart login credentials are required to run this program. No we do not steal your credentials. What is your email?")
Email = input(">")
print("\n what is your instacart login password?")
password = input(">")
print("")
def beginning(ExecuteProgram, Acknowledgement, breakout):
    print("Please Go to InstaCart and add any items you would like to order to your cart. Once you have done so, please fill out address and go to the next page.\n Would you like this tool to automatically place your order?")
    ExecuteProgram = input(">")    
    if ExecuteProgram == "Yes" or ExecuteProgram == "yes":
        print("Ok.")
        print("")
        while True:
            print("This Program will keep checking if a delivery slot is available, and if one is available, it will place your order.\n Please refrain from turning off the computer or messing with the tab in which the program is running in while this program is running or it may cause some issues.")
            print("")
            while True:
                print("Do you acknowledge the terms listed above? If so, type yes. if not, type no and you shall be able to view the terms again.")
                Acknowledgement = input(">")
                if Acknowledgement == "Yes" or Acknowledgement == "yes":
                    breakout = True
                    break
                elif Acknowledgement == "No" or Acknowledgement == "no":
                    breakout = False
                    break
                else:
                    print("please type yes or no.")
                    continue
            if breakout == True:
                break
            else:
                continue
    elif ExecuteProgram == "No" or ExecuteProgram == "no":
        print("Very well.")
        print("Thank you for using this Instacart auto delivery and order tool.\n If you would like to support development, please consider donating 1 dollar by using the following link: \n https://tinyurl.com/yapynqnh")
        quit() 
    else:
        print("Please Answer the Question In a Proper Manner")
        beginning(Ex, Terms, breakdown)
beginning(Ex, Terms, breakdown)



# Opens new window and logs into instacart
browser = webdriver.Chrome()
browser.get("https://www.instacart.com")
time.sleep(10)
LoginButton = browser.find_element_by_partial_link_text("Log in")
LoginButton.click()
time.sleep(4)
EnterEmail = browser.find_element_by_id("nextgen-authenticate.all.log_in_email")
EnterEmail.send_keys(Email)
EnterPassword = browser.find_element_by_id("nextgen-authenticate.all.log_in_password")
EnterPassword.send_keys(password)
EnterPassword.click()
LoginEnter = browser.find_element_by_xpath("//button[@type='submit']")
LoginEnter.click()
time.sleep(15)
browser.get("https://www.instacart.com/store/checkout_v3")

# Repeats until the script finds a delivery slot available

while True:
    try:
        DeliveryButton = browser.find_element_by_xpath("//input[@name='delivery_option']")
        DeliveryButton.click()
        print("Slot Available. Placing Order.")
        break
    except:
        try:
            NoOrders = browser.find_element_by_xpath("//span[@text='Sorry, we’re fresh out of same-day delivery options at this store.']")
            print("no slot available. refreshing page.")
            browser.refresh()
        except:
            print("slot available. Placing Order.")
            break
try:
    ContinueButton = browser.find_element_by_xpath("//textarea[@placeholder='Add delivery instructions (optional)']")
    ContinueButton.submit()
except:
    time.sleep(1)
try:
    AddContact = browser.find_element_by_xpath("//button[@text='Allow']")
except:
    time.sleep(1)
PlaceOrder = browser.find_element_by_xpath("//div[@class='rmq-4534e6b']//button[@type='button']")
PlaceOrder.click()

print("Thank you for using this Instacart auto delivery and order tool.\n If you would like to support development, please consider donating 1 dollar by using the following link: \n https://tinyurl.com/yapynqnh")
quit()    
