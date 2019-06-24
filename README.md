# timsheet_cheat
Never worry about a late timesheet submission again. This script uses selenium to automate the inov8 timesheet webpages to set Monday-Friday to "1" and click "save as draft". Haven't given it the full power of submitting yet incase the timesheet is incorrect.
## Requirements
* Python 3
* Selenium (pip install selenium)
* Chrome webdriver on system path (http://chromedriver.chromium.org/downloads)
* Virtualenv (pip install virtualenv)(optional - only needed if using the init script)
## Example
```
python timesheet_cheat.py "<username>" "<password>"
```
## Potential Improvements
* Allow the script to submit the timesheet instead of save as draft (maybe a prompt?)
* Only update days that are not already completed
* Currently only updates the current week, could iterate through incomplete weeks and update

## Tips
If you see the following error: 
```
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
Make sure chrome webdriver is on the system path. If that doesn't work, modify the python script and give the driver element the path of the chrome webdriver:
```
self.driver = webdriver.Chrome('/path/to/chromewebdriver')
```
