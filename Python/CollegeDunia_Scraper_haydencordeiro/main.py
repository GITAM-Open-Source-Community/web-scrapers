import time
from numpy import degrees
from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome()
driver.get("https://collegedunia.com/btech/maharashtra-colleges?sub_stream_id=424,426") 
time.sleep(5)
colleges=driver.execute_script('''var colleges=document.getElementsByClassName("clg-name-address")
var ol=[];
for(var i=0;i<colleges.length;i++){

    ol.push(colleges[i].textContent)
}
return ol
''')

driver.close()
df = pd.DataFrame({'colleges':colleges})

df.to_excel ('export_dataframe.xlsx', index = True, header=True)
