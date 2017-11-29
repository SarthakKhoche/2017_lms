'''
Problem Statement ID: 2017_lms
Aim :- Getting the list of all new assignments and posts from your LMS.
'''

from bs4 import BeautifulSoup
import requests
import datetime
import warnings

empty_list = []

#To ignore the warnings caused by the bypassing the error caused due to absence of SSL certificate!
warnings.filterwarnings("ignore")

#Clears output.txt in order to get fresh updates in every half an hour.
open('output.txt', 'w').close()

#Logging in LMS through Python Script
with requests.Session() as c:
    Initial_URL = "https://lms.iiitb.ac.in/moodle/login/index.php"
    USERNAME = ""  #Username of the person who wants to access the LMS(in the double inverted commas)
    PASSWORD = ""  #Password of the person who wants to access the LMS(in the double inverted commas)
    c.get(Initial_URL, verify=False)
    login_data = dict(username = USERNAME, password = PASSWORD, next ='/')
    c.post(Initial_URL, data=login_data)
    page = c.get("https://lms.iiitb.ac.in/moodle/my/")

soup = BeautifulSoup(page.content, "html.parser")

#Accesing the required data from LMS through Python Script
with open("output.txt", 'a') as file:

    now = str(datetime.datetime.now())
    empty_list.append("As until date and time : " + now + "\n")

    for i in soup.find_all("div", {"class" : "box coursebox"}):
        if(i.find_all("div", {"class" : "activity_info"})):
            empty_list.append('\n' + i.div.h2.a["title"] + ' : \n')
            for j in i.find_all("div", {"class" : "collapsibleregioncaption"}):
                empty_list.append(j.text + '\n')

    if(len(empty_list) == 1):
	list.append("No New Updates!")
    else:
	for i in range(len(empty_list)):
            file.write(empty_list[i]) 

# The output will be generated in a text-file by the name "output.txt", in the same directory as that of this given code!
