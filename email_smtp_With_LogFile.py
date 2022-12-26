from sys import *
import time
import os
import psutil
import urllib3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib



def MailSender(filname, time):
    try:
        fromaddr = "ranjeetdhole26@gmail.com"
        toaddr = "ranjeetdhole96@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
                Hello %s,
                       Welcome,
                       Log file is created at : %s
                       This is auto generated mail.
                Thanks and Regards,
               Ranjeet Dhole
                """ % (toaddr, time)

        subject = """Process log generted at : %s""" % time

        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filname, "rb")

        part = MIMEBase('application', 'octet-stream')

        part.set_payload((attachment).read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition', "attachment; filename=%s" % filname)

        msg.attach(part)
     
        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()
        server.login(fromaddr, "mcqekfgobhuumoso")
        text = msg.as_string()

        server.sendmail(fromaddr,toaddr,text)

        server.quit()

        print("Log file successfully sent throught Mail")

        print("Mail has been sucessfully sent")
    except Exception as E:
        print("Unable to send mail", E)

def ProcessDisplay(log_dir = 'data'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "_" * 80
    log_path = os.path.join(log_dir, " file %s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("All Runing Process : "+time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms/ (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))
    


    MailSender(log_path,time.ctime())


        
def main():

    print("Process Monitoring Automation with periodic Mail Sender....")

    print("Application name:" + argv[0])

    if (len(argv) != 2):
        print("Invalid number of argumnets")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used log record of running processess")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
        

    except ValueError:
        print("Error : Invaild datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()