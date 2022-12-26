from sys import *
import time
import os
import psutil

def ProcessDisplay(log_dir='Demo'):
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
    f.write("All Runing Process : " + time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))


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