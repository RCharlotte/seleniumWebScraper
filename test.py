
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\seleniumbrowser\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get("https://www.myjobsinkenya.com/")
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("python")
driver.find_element(By.XPATH, "//input[contains(@value,'python')]").click()
pythonJobs = driver.find_elements(By.XPATH, "//a[contains(@href,'//www.myjobsinkenya.com/jobs/')]")
pythonJobslocations= driver.find_elements(By.XPATH,"//span[contains(@class,'office')]")

mypythonjobs=[]
mypythonlocations=[]

for jobs in pythonJobs:

    mypythonjobs.append(jobs.text)

for joblocs in pythonJobslocations:

    mypythonlocations.append(joblocs.text)

finallist = zip(mypythonjobs,mypythonlocations)

for data in list(finallist):
    print(data)


