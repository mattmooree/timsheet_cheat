from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from element_dictionary import ElementDictionary
import argparse


class TimesheetFiller:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "https://inov8consulting.timesheetportal.com/"
        self.element_dict = ElementDictionary().element_dict
        self.driver = webdriver.Chrome("C:\\Users\\Matthew Moore\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def fill_in_timesheet(self):
        self.driver.get(self.url)
        self.driver.find_element_by_name("txtUsername").send_keys(self.username)
        self.driver.find_element_by_name("txtAuthToken").click()
        self.driver.find_element_by_name("txtAuthToken").send_keys(self.password + Keys.ENTER)
        days = [x for x in self.element_dict if x.__contains__("day")]
        for day in days:
            select = Select(self.driver.find_element_by_xpath(self.element_dict[day]))
            select.select_by_visible_text('1')
        self.driver.find_element_by_xpath(self.element_dict["save_draft_btn"]).click()
        self.driver.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help="Username for timesheets login")
    parser.add_argument('password', help="Password for timesheets login")
    args = parser.parse_args()
    timesheet_filler = TimesheetFiller(args.username, args.password)
    timesheet_filler.fill_in_timesheet()


if __name__ == "__main__":
    main()
