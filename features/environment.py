from appium import webdriver
from pages.calculator_page import CalculatorPage

def before_scenario(context, scenario):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': '/TesteAppiumTopaz/app/Calculatora.apk',
        'automationName': 'UiAutomator2',
        'appActivity': 'com.android.calculator.Calculator'
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.calculator_page = CalculatorPage(context.driver)

# Este hook será executado após cada cenário
def after_scenario(context, scenario):
    context.calculator.get_element_by_id("CLR").click()

def after_scenario(context, feature):
    context.driver.quit()