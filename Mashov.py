import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

SCHOOL_ID = 480053
CREDENTIALS_FILE = r'c:\temp\corona.txt'

driver = webdriver.Chrome(ChromeDriverManager().install())


def get_credentials():
    with open(CREDENTIALS_FILE, 'r') as file:
        content = file.readlines()
    return content[0], content[1]


def login(username, pass_word):
    driver.get("http://web.mashov.info/students/login")
    form = driver.find_element_by_class_name('mat-tab-body-wrapper')
    school = form.find_element_by_id('mat-input-3')
    year = form.find_element_by_tag_name('mat-select')
    user = form.find_element_by_id('mat-input-0')
    password = form.find_element_by_id('mat-input-4')
    enter_button = form.find_element_by_tag_name('button')
    school.clear()
    school.send_keys(SCHOOL_ID)
    school.send_keys(Keys.RETURN)
    if 'שנה נוכחית' not in year.text:
        year.send_keys(Keys.ARROW_UP)
    if 'שנה נוכחית' not in year.text:
        year.send_keys(Keys.ARROW_DOWN)
    if 'שנה נוכחית' not in year.text:
        raise Exception
    user.clear()
    user.send_keys(username)
    password.clear()
    password.send_keys(pass_word)
    enter_button.click()
    time.sleep(3)


def fill_form():
    driver.get("http://web.mashov.info/students/main/covidClearance")
    cb1_val = driver.find_element_by_id('mat-checkbox-1-input')
    cb2_val = driver.find_element_by_id('mat-checkbox-2-input')
    cb1 = driver.find_element_by_id('mat-checkbox-1')
    cb2 = driver.find_element_by_id('mat-checkbox-2')
    if not cb1_val.is_selected():
        cb1.click()
    if not cb2_val.is_selected():
        cb2.click()
    form = driver.find_element_by_tag_name('mat-card-actions')
    send = form.find_element_by_tag_name('button')
    send.click()


def main():
    user, password = get_credentials()
    login(user, password)
    fill_form()
    driver.quit()


if __name__ == '__main__':
    main()
