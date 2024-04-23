from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Assignment9:
    #decleration of variable
    def __init__(self):
        self.url="https://www.saucedemo.com/"
        self.driver=webdriver.Firefox()
        self.username="user-name"
        self.password="password"
        self.login_button="login-button"
        self.enter_login="standard_user"
        self.enter_password="secret_sauce"
        self.action=ActionChains(self.driver)
        self.current_title=self.driver.title
        self.url1=self.driver.current_url
    #Opening of webpage
    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def login(self):
        #Identifying the user name field and entering the user name
        self.driver.find_element(by=By.ID,value=self.username).send_keys(self.enter_login)

        #Identifying the p[assword field and entering the password
        self.driver.find_element(by=By.ID,value=self.password).send_keys(self.enter_password)

        #Identifyiong the Login button and clicking on it
        self.driver.find_element(by=By.ID,value=self.login_button).click()

        #Identifying the web page element and copying the page content to a variable
        content=self.driver.find_element(by=By.ID, value="inventory_container").text

        #Creating a text file on desktop
        file=open("C:\\Users\\Admin\\Desktop\\Webpage_task_11.txt","w")

        #Writing the current title of the web page to the created text file
        file.write("current title:"+self.current_title+"\n")

        # Writing the current url of the web page to the created text file
        file.write("url : "+ self.url1+"\n")

        #Writing the content of the web page to text file
        file.write(content)

        #Closing the text file
        file.close()

        #closing the webpage
        self.driver.close()

#Creating object for the class
obj= Assignment9()

#calling the methods in th eclass
obj.browse()
obj.login()
