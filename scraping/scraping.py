from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys


def configure_browser():
    # use firefox's driver
    firefox_options = webdriver.FirefoxOptions()

    # change download directory
    download_dir = os.getcwd() + "/data/data_" + sys.argv[1]
    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.download.dir", download_dir)

    # set preference for saving file instead of opening it
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", 'text/csv,application/csv')

    # don't open firefox
    firefox_options.add_argument("--headless")

    driver = webdriver.Firefox(options = firefox_options, executable_path = './drivers/geckodriver')

    return driver


def fetch_csv_elements():
    ogpl_elements = driver.find_elements_by_class_name('ogpl-processed')
    li_elements = driver.find_elements_by_tag_name('li')
    csv_list = sorted(set(ogpl_elements) & set(li_elements), key = ogpl_elements.index)
    return csv_list


def output_for_error_handling(page, file_no, check_csv_or_json):
    # output page no. and file no. for error handling
    print("Page: {} File: {}".format(page, file_no), end = "")
    if check_csv_or_json.get_attribute('innerHTML') == 'csv':
        print("(csv)", end = "")
    print("")


# expectation for checking whether page number is changed after loading new page
class page_num_changed:
    def __init__(self, locator, attr):
        self.locator = locator
        self.attr = attr

    def __call__(self, driver):
        if int(WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, self.locator))).get_attribute('innerHTML')) == self.attr:
            return WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, self.locator)))
        else:
            return False


if __name__ == '__main__':
    
    # set configurations for the browser
    driver = configure_browser()

    # range for downloading content on pages = [start, end)
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    for page in range(start, end):
        # wait until we get on the first tab
        while driver.current_window_handle != driver.window_handles[0]:
            pass

        # wait until all the files from the previous page are downloaded 
        while driver.find_elements_by_id('confirmation_popup'):
            pass

        website = "https://data.gov.in/resources-from-web-service/6622307?page={}".format(page)
        driver.get(website)

        WebDriverWait(driver, 200).until(page_num_changed('pager-current', page+1))

        # wait until page is loaded
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'csv')))

        # fetch all the csv file elements
        csv_list = fetch_csv_elements()

        # elements which are used to check whether the resource is in csv format or json(we'll ignore csv as csv contains json :P) 
        elements_to_check_csv_or_json = driver.find_elements_by_class_name('data-extension')

        # loop over all the files
        for i in range(len(csv_list)):
            # wait until we get on the first tab
            while driver.current_window_handle != driver.window_handles[0]:
                pass

            # wait until form is absent
            while driver.find_elements_by_id('confirmation_popup'):
                pass

            # click on "export csv"
            driver.execute_script("arguments[0].click();", csv_list[i])

            # wait until form is present
            while not driver.find_elements_by_id('confirmation_popup'):
                pass

            # select appropriate inputs to the form
            usage_type = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="edit-download-reasons-2"]')))
            purpose = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="edit-reasons-d-3"]')))
            
            driver.execute_script("arguments[0].click();", usage_type)
            driver.execute_script("arguments[0].click();", purpose)

            # click on submit
            submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="edit-submit"]')))
            driver.execute_script("arguments[0].click();", submit)

            # output_for_error_handling(page, i+1, elements_to_check_csv_or_json[i])

            # switch to the first tab
            driver.switch_to.window(driver.window_handles[0])