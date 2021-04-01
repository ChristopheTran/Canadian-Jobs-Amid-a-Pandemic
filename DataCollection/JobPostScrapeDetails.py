import os
import bz2
import pickle
import requests
from bs4 import BeautifulSoup
import pandas

recordCounter = 0
totalHtmlFilesToProcess = 0
jobPostDetails = []

def extractInfo(htmlFile):
    soup = BeautifulSoup(encoded_str,'lxml')

    try:
        jobTitle = soup.find("span", property="title").text.strip()

        data = soup.find("ul", class_="job-posting-brief colcount-lg-2")
        city = data.find("span", class_="city").text.strip()

        try:
            pay = data.find("span", property="minValue").text.strip()
            payUnit = data.find("span", property="unitText").text.strip()
        except:
            pay = data.find_all("li")[1].text.replace('Salary','').strip()
            payUnit = None  
        
        print(f'''
        Job Title: {jobTitle}
        City: {city}
        Pay: {pay}
        PayUnit: {payUnit}
        ''')
    except:
        return

    jobPostDetails.append([jobTitle, city, pay, payUnit])
    global recordCounter
    recordCounter = recordCounter + 1


files = []
directory = "./DataSet/JobPostProcessed"
for filename in os.listdir(directory):
    if filename.endswith(".bz2"):
        print(os.path.join(directory, filename))
        file = bz2.BZ2File(os.path.join(directory, filename), 'rb')
        file = pickle.load(file)
        totalHtmlFilesToProcess += len(file)

        for i in range(len(file)):
            htmlFile = file[i]
            extractInfo(htmlFile)
            print(f'{recordCounter} records were successfully processed out of {totalHtmlFilesToProcess} records')
            


df = pandas.DataFrame(jobPostDetails, columns = ['Job Title', 'City','Pay','PayUnit']) 
df.to_csv('./DataSet/JobPostDetails/data.csv', index = False)
            










