import os 
import getpass
os.system("tput setaf 1")
print("\t\t\t\t\t\t\t\tHey welcome to my TUI thats makes life simple")
os.system("tput setaf 2")
print("\t\t\t\t\t\t\t\t.............................................")
 
passwd = getpass.getpass("Enter your password : ")
apass = "1234"
if passwd != apass:
    print("auth incorrect")
    exit()

print("where you world like to peform your job (local/remote) : ",end='')
os.system("tput setaf 3")

location = input()

if location == "remote":
    remoteIP = input("Enter you IP : ")

while True:
    print("""
    press 1 : to see date
    press 2 : to see cal
    press 3 : to create web server
    press 4 : to add the user
    press 5 : to create file
    press 6 : to setup N/W 
    press 7 : to exit
    """)
    print("Enter your choise : ", end="")
    ch = input()
    if location == "local":
        if int(ch) == 1:
            os.system("date")
        elif int (ch) == 2:
            os.system("cal")
        elif int (ch) == 3:
            print("we are checking your software installed or not")
            os.system("rpm -qv list httpd")
            print("if installed type capital 0 to abort the process else type capital 1 to continue : ", end="")
            os.system("tput setaf 4")
            choise = input()
            if int(choise) == 1:
                os.system("sudo dnf -v  install httpd")
                os.system("sudo systemctl start httpd")
                os.system("sudo systemctl status httpd")
                os.system("sudo systemctl enable httpd")
            elif int(choise) == 0 :
                print("process is aborted!")
                os.system("tput setaf 5")
            else:
                print("Enter valid choise")
        elif int (ch) == 4:
            print("Can U plz give username : ",end="")
            create_user = input()
            os.system("sudo useradd {}".format(create_user))
        elif int (ch) == 5:
            os.system("vim file.txt")
        elif int (ch) == 6:
            os.system("sudo ifconfig -v enp0s3 down")
            os.system("sudo ifconfig -v enp0s3 up")
        elif int (ch) == 7:
            exit()
        else :
            print("Enter valid choice")
    elif location == "remote":
        if int(ch) == 1:
            os.system("ssh {0} date".format(remoteIP))
        elif int (ch) == 2:
            os.system("ssh {0} cal".format(remoteIP))
        elif int (ch) == 3:
            print("we are checking your software installed or not")
            os.system("tput setaf 6")
            os.system("ssh {0} rpm -qv list httpd".format(remoteIP))
            print("if installed type capital 0 to abort the process else type capital 1 to continue : ", end="")
            os.system("tput setaf 8")
            choise = input()
            if int(choise) == 1:
                os.system("ssh {0} sudo dnf -v  install httpd".format(remoteIP))
                os.system("ssh {0} sudo systemctl start httpd".format(remoteIP))
                os.system("ssh {0} sudo systemctl status httpd".format(remoteIP))
                os.system("ssh {0} sudo systemctl enable httpd".format(remoteIP))
            elif int(choise) == 0 :
                print("process is aborted!")
                os.system("tput setaf 9")
            else:
                print("Enter valid choise")
        elif int (ch) == 4:
            print("Can U plz give username : ",end="")
            create_user = input()
            os.system("ssh {0} sudo useradd {1}".format(remoteIP , create_user))
        elif int (ch) == 5:
            os.system("ssh {0} vim file.txt".format(remoteIP))
        elif int (ch) == 6:
            os.system("ssh {0} sudo ifconfig -v enp0s3 down".format(remoteIP))
            os.system("ssh {0} sudo ifconfig -v enp0s3 up".format(remoteIP))
        elif int (ch) == 7:
            exit()
        else :
            print("Enter valid choice")
    else :
        print("Location doesn't suppport!")
    input("Enter to continue..............")
    os.system("tput setaf 10")
    os.system("clear")
