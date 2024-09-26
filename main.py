from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the ChromeDriver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Google homepage
driver.get("https://www.google.com")

# Wait until the search input element with class name "gLFyf" is loaded
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

# Find the search input element and clear it (just in case there's pre-filled text)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()

# Type the search query "cihan alcin" and press Enter
input_element.send_keys("cihan alcin" + Keys.ENTER)

# Wait until the link to "Cihan's Portfolio" is present on the search results page
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Cihan's Portfolio"))
)

# Click on the link to navigate to Cihan's Portfolio website
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Cihan's Portfolio")
link.click()

# Wait until the "Apps" button on the portfolio page is visible
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Apps')]"))
)

# Click on the "Apps" button to display the list of apps
apps_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apps')]")
apps_button.click()

# Wait until the app titles (h2 elements with class 'text-primary') are loaded
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'text-primary')]"))
)

# Find all the app titles and count how many there are
app_titles = driver.find_elements(By.XPATH, "//h2[contains(@class, 'text-primary')]")
number_of_apps = len(app_titles)

# Loop through each app and interact with it
for i in range(number_of_apps):
    # Click on the app title
    app_titles[i].click()
    # Print the title of the clicked app
    print(app_titles[i].text, "clicked")
    # Wait for 3 seconds before interacting with the app
    time.sleep(3)

    # Loop to click the "Next" button to browse app slides
    for j in range(3):
        next_button = driver.find_element(
            By.XPATH, "//button[contains(@class, '-left-12')]"
        )
        next_button.click()
        time.sleep(2)

    # After viewing the slides, click the "Close" button to close the app view
    close_button = driver.find_element(
        By.XPATH, "//button[span[contains(text(),'Close')]]"
    )
    close_button.click()
    time.sleep(2)

# Wait 3 seconds after all apps have been interacted with
time.sleep(3)

# Close the browser window and end the session
driver.quit()
