from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for locating elements
import os
import booking.constants as const
from booking.filtrations import BookingFiltration

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Users/LENOVO/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        currencies = self.find_elements(By.CSS_SELECTOR, 'button[data-testid="selection-item"]')
        
        for element in currencies:
            if element.find_element(By.CLASS_NAME,'CurrencyPicker_currency').text == currency:
                element.click()
                break
        


    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR, 'li[id="autocomplete-result-0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        datebtn = self.find_element(By.CSS_SELECTOR, 'button[data-testid="date-display-field-start"]')
        datebtn.click()

        
        check_in_out_element = self.find_elements(By.TAG_NAME, 'table')

        
        check_in_element = check_in_out_element[0].find_element(By.CSS_SELECTOR , f'span[date-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = check_in_out_element[1].find_element(By.CSS_SELECTOR , f'span[date-date="{check_out_date}"]')
        check_out_element.click()



    