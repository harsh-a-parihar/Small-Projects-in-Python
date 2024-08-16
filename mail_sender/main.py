import smtplib
import datetime as dt


MY_EMAIL = 'ENTER YOUR EMAIL ID'    # Your mail-id from which you want to send mail
MY_PASSWORD = 'ENTER PASSWORD OF MAIL ID'   # Password of associated with mail-id

now = dt.datetime.now()     # current data and time
Weekday = now.weekday()     # today's weekday (from 0 to 6)

if Weekday in range(0, 7):      # 7 excluded
    with open('content.txt', 'r') as content_file:
        content = content_file.read()

    with smtplib.SMTP('smtp.gmail.com', port=587) as connector:     # build connection with your smtp mail service provider
        connector.starttls()    # builds extra security layer
        connector.login(user=MY_EMAIL, password=MY_PASSWORD)    # login to your mail service
        connector.sendmail(from_addr=MY_EMAIL, to_addrs="ENTER PERSON'S EMAIL ID YOU WANT TO SEND MAIL",
                           msg=f"Subject:ENTER SUBJECT OF MAIL.\n\n<ENTER CONTENT>{content}")
        

''' You can automate this whole process using <python anywhere>, 
go on the website, deploy code and automate it to run when scheduled. '''

#----------------------------------------------------------------------------------------------------------#
