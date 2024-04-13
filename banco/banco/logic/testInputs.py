import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def send_form_data(url, number, wait_time=10):  # Added wait_time parameter
  """
  Uses Selenium to simulate form submission with the given number.

  Args:
      url: The URL of the web application's form page.
      number: The number to input in the form.
      wait_time: The implicit wait time in seconds (default: 10).
  """
  i = 1
  for i in range(10):
    start = time.time()
    driver = webdriver.Chrome()  # Replace with the path to your webdriver (e.g., Firefox)
    driver.implicitly_wait(wait_time)  # Set implicit wait time

    driver.get(url)

    # Find form elements (replace with actual selectors)
    phone_number_field = WebDriverWait(driver,1).until(
          EC.presence_of_element_located((By.NAME, "phonenumber"))
    )
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")  # Adjust selector

    phone_number_field.send_keys(number)
    submit_button.click()

  # ... (rest of your code)

    WebDriverWait(driver,1).until(
          EC.url_contains("/sendSuccess/")
    )
    
    driver.quit()

    end_time = time.time()

    print(end_time-start)

# Replace with the actual URL and adjust wait time as needed
url = 'http://127.0.0.1:8000/sendOtp/'
number = '+573053461617'
wait_time = 15  # You can adjust this value

send_form_data(url, number, wait_time)



