from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getClasses(username, password):
    attempt = 0
    opts = Options()
    opts.headless = True
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    opts.add_argument('--log-level=3')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=opts)

    loginPage = 'https://login.gitam.edu/Login.aspx'
    gLearn = 'https://gstudent.gitam.edu/G-Learn.aspx'

    driver.get(loginPage)
    currentPage = driver.current_url

    while currentPage != 'https://gstudent.gitam.edu/Welcome.aspx':
        pin = driver.find_element_by_name('txtusername')
        pin.clear()
        pin.send_keys(username)
        pw = driver.find_element_by_name('password')
        pw.clear()
        if(attempt == 0):
            pw.send_keys(password)
        else:
            password = getpass("Incorrect Password!\nEnter password again: ")
            pw.send_keys(password)

        driver.find_element_by_name('Submit').click()
        currentPage = driver.current_url
        attempt += 1

    driver.get(gLearn)

    links = driver.find_elements_by_css_selector('tbody tr td a')

    exportList = []

    for link in links:
        if(link.text.startswith('Session on')):
            url = link.get_attribute('href')
            link.text.replace('\n', ' ')
            link = link.text.split('\nDate')
            session = {
                "name": link[0].split(' created by ')[0],
                "lecturer": link[0].split(' created by ')[1],
                "date": link[1].split(" : ")[1].split(" :: Time:")[0],
                "time": link[1].split(" : ")[1].split(" :: Time:")[1],
                "url": url
            }
            exportList.append(session)

    driver.quit()

    return exportList