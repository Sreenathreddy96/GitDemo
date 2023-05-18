from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    Username = (By.XPATH, "//input[@placeholder='Username']")
    Password = (By.NAME, "password")

    submit = (By.XPATH, "//button[@type='submit']")
    profile = (By.CLASS_NAME, "oxd-userdropdown-tab")
    logout = (By.XPATH, "//a[normalize-space()='Logout']")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.Username)

    def getPassword(self):
        return  self.driver.find_element(*LoginPage.Password)

    def getSubmitButton(self):
        return self.driver.find_element(*LoginPage.submit)
    def getProfile(self):
        return self.driver.find_element(*LoginPage.profile)

    def getLog0ut(self):
        return self.driver.find_element(*LoginPage.logout)







