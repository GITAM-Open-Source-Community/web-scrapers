# GITAM Semester Results Scraper
This Python script can scrape all semester results from GITAM Semester Results [website](https://doeresults.gitam.edu/onlineresults/pages/newgrdcrdinput1.aspx "website").<br>
The script will generate a workbook with each section's data in a seperate worksheet with the section name. It will also feature student records which have high CGPA and GPA in 2 seperate sheets.<br>
To run the script, run the following in the command line, after downloading the script.<br>
`python gitam_results_scraper.py`

### Prerequisites
The program works based on Selenium with ChromeDriver.<br>
Download chromedriver [here](https://chromedriver.chromium.org/ "here") based on your Chrome browser version.<br>
#### Install the necessary packages for this program
Run this command to install the necessary packages:<br>
`pip install -r requirements.txt`<br><br>
**Or alternatively, you can install the required packages manually.**<br>
Install **Selenium** package for Python using the following command:<br>
`pip install selenium`

Install **tqdm** package for progress bars:<br>
`pip install tqdm`

Install **xlsxwriter** to write scraped data into .xlsx spreadsheets.<br>
`pip install xlsxwriter`
<br><br>
*Follow the comments in the script for customized output or modify the program yourself to suit your needs.*
