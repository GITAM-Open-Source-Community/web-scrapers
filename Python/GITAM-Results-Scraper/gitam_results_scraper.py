from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tqdm import tqdm
import xlsxwriter

# Customise the variable values to get the desired result

WORKBOOK_PATH = 'Drive:/workbook.xlsx' # Path to xlsx workbook
CHROMEDRIVER_PATH = 'Drive:/User/Documents/chromedriver' # Path to chromedriver.exe file

CAMPUS = 1 # Visakhapatnam = 1, Hyderabad = 2, Bangalore = 3
BATCH_YEAR = 19 # 19 for 2019 batch
SEMESTER = 4

SECTION_RANGE = (1, 20) # Inclusive range of the sections to be scraped.
ROLLNO_RANGE = (1, 70) # Inclusive range of roll numbers to be scraped in each section.

TOPPER_LOWER_BOUND = 9.0 # Minimum CGPA or GPA for a record to be featured in toppers sheet.

# Change only if necessary.
GITAM_RESULTS_LINK = 'https://doeresults.gitam.edu/onlineresults/pages/newgrdcrdinput1.aspx'
RESULT_PAGE = 'https://doeresults.gitam.edu/onlineresults/pages/View_Result_Grid.aspx'


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless") # Comment this line to see scraping live.

HEADERS =  ['Regd.No.', 'Name', 'GPA', 'CGPA'] 


workbook = xlsxwriter.Workbook(WORKBOOK_PATH)
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
gpa_top = workbook.add_worksheet(name='GPA-Toppers')
gpa_top.write_row(0, 0, HEADERS)
cgpa_top = workbook.add_worksheet(name='CGPA-Toppers')
cgpa_top.write_row(0, 0, HEADERS)

gi = ci = 1

for sec in range(SECTION_RANGE[0], SECTION_RANGE[1]+1):
    worksheet = workbook.add_worksheet(name=f'B{sec}')
    worksheet.write_row(0, 0, HEADERS)

    for i in tqdm(range(ROLLNO_RANGE[0], ROLLNO_RANGE[1]+1), desc = f'Section {sec}: '):
        regd = str(CAMPUS) + '2' + str(BATCH_YEAR).zfill(2) + '103' + str(sec).zfill(2) + str(i).zfill(3)

        driver.get(GITAM_RESULTS_LINK)
        Select(driver.find_element_by_id('cbosem')).select_by_value(str(SEMESTER))
        roll = driver.find_element_by_name('txtreg')
        roll.clear()
        roll.send_keys(regd)
        driver.find_element_by_name('Button1').click()

        if driver.current_url==RESULT_PAGE:
            name = str(driver.find_element_by_xpath("//span[contains(@id,'lblname')]").text)
            gpa = float(driver.find_element_by_xpath("//span[contains(@id,'lblgpa')]").text)
            cgpa = float(driver.find_element_by_xpath("//span[contains(@id,'lblcgpa')]").text)

            worksheet.write_row(i, 0, [regd, name, gpa, cgpa])
            if gpa>TOPPER_LOWER_BOUND:
                gpa_top.write_row(gi, 0, [regd, name, gpa, cgpa])
                gi+=1
            if cgpa>TOPPER_LOWER_BOUND:
                cgpa_top.write_row(ci, 0, [regd, name, gpa, cgpa])
                ci+=1

workbook.close()
driver.quit()
print('DONE!')