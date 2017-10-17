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
#    COMP9313 full number
    if(title == 'Class Details'):
#        print("Enter the right COMP9313 page!")
        Full_list = []
#        abc = soup.find_all("font",string="Full")
        for i in soup.find_all("font",string="Full"):
            Full_list.append(i.string)
#        print("Number of Full: ", len(Full_list))
        if len(Full_list)<8:
            send_email("chenhao1415@gmail.com")
            return 1
        else:
            return 0
    return 0


def send_email(reveive_email):
    sender = "comp9321temp@gmail.com"
    password = "abcd1234abcd"
    
    content = "COMP9313 has vacancy!!!! go get it!!!!"
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender,password)
    mail.sendmail(sender,reveive_email,content)
    
    mail.close()
    print("email sent!!")
    



if __name__ == '__main__':
    time_start = time.time();
    url = 'http://timetable.unsw.edu.au/2018/COMP9313.html'
    receiver_email = "chenhao1415@gmail.com"
    
#    url = 'http://timetable.unsw.edu.au/2018/COMP9021.html'
    
    
    cont, soup = getWebPage(url)
#    print(soup)
    print('---------Check COMP9313----------')
    count = 1
    while True:
        if judge(soup) == 1:
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
    
