import urllib.request
import bs4 as bs
import os
import smtplib
import time

def getWebPage(url):
    resp=urllib.request.urlopen(url)
    html= resp.read()
    soup = bs.BeautifulSoup(html, 'lxml')
    return html, soup


def judge(soup):
    title = soup.title.string
    print(title)
 #   COMP9313 full number
    if(title == 'Class Details'):
        print("Enter the right COMP9417 page!")
        Open_list = []
        for i in soup.find_all("font",string="Open"):
            Open_list.append(i.string)
        print("Number of Open: ", len(Open_list))
        if len(Open_list)>2:
            print("Good!")
            send_email("PLEASECHANGE")
            return 1
        else:
            return 0
    return 0


def send_email(reveive_email):
    sender = "USE YOUR EMAIL"
    password = "YOUR PASS"
    
    content = "PLEASE CHANGE THE CONTAINS"
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender,password)
    mail.sendmail(sender,reveive_email,content)
    
    mail.close()
    print("email sent!!")
    



if __name__ == '__main__':
    time_start = time.time();
    url = 'http://timetable.unsw.edu.au/2018/COMP9417.html' PLEASE CHANGE
    receiver_email = "PLEASE CHANEG"
    
#    url = 'http://timetable.unsw.edu.au/2018/COMP9021.html'
    
    
    cont, soup = getWebPage(url)
#    print(soup)
    print('---------Check COMP9417----10s------')
    count = 1
    while True:
        if judge(soup) == 1#PLEASE CHANGE HERE(COUNT THE FULL APPEARE TIME in the url):
            print("Success!!!")
            print(time.strftime("%Y-%m-%d %A %X %Z", time.localtime()))
            break
        else:
            print("T_T Failed...")
            print("Count: ",count)
            print(time.strftime("%Y-%m-%d %A %X %Z", time.localtime()))
        count += 1
        time_now = time.time()
        Running_time  = time_now - time_start
        print("program already run for: ",Running_time, "s.")
        print("--------------------------")
        time.sleep(10)
    
