from behave import given, when, then
from appium import webdriver
from pages.calculator_page import CalculatorPage


@given('que eu abri o app de calculadora')
def step_impl(context):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': '/TesteAppiumTopaz/app/Calculatora.apk',
        'automationName': 'UiAutomator2',
        'appActivity': 'com.android.calculator.Calculator'
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    context.calculator_page = CalculatorPage(context.driver)

@when('eu digito "{number}"')
def step_impl(context, number):
    context.calculator_page.enter_number(number)

@when('eu pressiono "="')
def step_impl(context):
    context.calculator_page.press_equal()

@then('o resultado deve ser "{expected_result}"')
def step_impl(context, expected_result):
    result = context.calculator_page.get_result()
    assert result == expected_result, f"Resultado esperado: {expected_result}, obtido: {result}"

