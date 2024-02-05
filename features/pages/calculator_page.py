
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_number(self, number):
        self.driver.find_element_by_accessibility_id(number).click()

    def press_equal(self):
        self.driver.find_element_by_accessibility_id("=").click()

    def get_result(self):
        result_element = self.driver.find_element_by_accessibility_id("com.android.calculator:id/result")
        return result_element.text

    def get_element_by_id(self, value):
        id = find_element_by_accessibility_id(value)
        return self.driver.find_element_by_accessibility_id(id)


def find_element_by_accessibility_id(value):
    button = {
        "1": "com.android.calculator:id/digit_1",
        "2": "com.android.calculator:id/digit_2",
        "0": "com.android.calculator:id/digit_0",
        "=": "com.android.calculator:id/eq",
        "+": "com.android.calculator:id/op_add",
        "CLR": "com.android.calculator:id/clr",
    }

    return button[value]


def get_string_clr():
    return "CLR"



