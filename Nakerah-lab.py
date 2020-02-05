#!/usr/bin/python
import os
import time
import sys
f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
PHP_V=sys.argv[1]
hostname = 'localhost'
username = 'root'
password = ''
database = 'mysql'

print("Step 1: Install apache")
os.system("sudo apt-get install unzip")
#print("[+] Update your local package : ")
#os.system("sudo apt update")
print("[+] Install the apache2 package:")
os.system("sudo apt-get install apache2 -y")
print("[+] Enable its rewrite module, and restart the service :")
os.system("sudo a2enmod rewrite && systemctl restart apache2")
print("[+] Step 2 - Adjusting the Firewall ")
os.system("sudo ufw app list")
os.system("sudo ufw allow 'Apache'")
os.system("sudo ufw status'")
#-----------------------------------------------------------#
print("-------------------------------------------------------")
print("[+] Step 3 - Checking your Web Server")
os.system("sudo systemctl status apache2 --no-pager")
print("[+] Step 4 - Setting Up Virtual Hosts (Recommended)")
print("[+] Assign ownership of the directory:")
os.system("sudo chown -R $USER:$USER /var/www/")
print("[+] The permissions of your web")
os.system("sudo chmod -R 755 /var/www/")
print("[+] Disable the default site defined in 000-default.conf:")
os.system("sudo a2dissite 000-default.conf")
print("[+] Test for configuration errors: ")
os.system("sudo apache2ctl configtest ")
print("[+] Restart Apache to implement your changes:")
os.system("sudo systemctl reload apache2 ")
#-----------------------------------------------------------#
print("-------------------------------------------------------")

print("Step 5: Install MySQL")
os.system("sudo apt-get install mysql-server php-mysql -y")
print("-------------------------------------------------------")
print("This steps for Kali linux")
os.system("sudo ls -lart /var/run/my")
os.system("sudo mkdir /var/run/mysqld")
os.system("sudo touch /var/run/mysqld/.sock")
os.system("sudo chown -R mysql /var/run/mysqld/")
os.system("sudo /etc/init.d/mysql restart")



print("Step 6: Install php")
# for dvwa
os.system("sudo apt-get install php7.2-curl php7.2-mbstring php7.2-xml -y")
os.system("sudo apt-get install php7.3-curl php7.3-mbstring php7.3-xml -y")
os.system("sudo apt-get install php php-mysqli php-gd libapache2-mod-php -y")
print("-------------------------------------------------------")
print("Step 7: Install python")
os.system("sudo apt-get install python3 -y")
os.system("sudo apt-get install python3-pip -y")

os.system("sudo apt-get install python-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("pip install pymysql -y")
os.system("sudo apt-get install libmysqlclient-dev -y")
os.system("sudo -H pip3 install mysqlclient -y")
os.system("sudo apt-get install python3-dev libmysqlclient-dev -y")

#os.system("pip install MySQL-python")

print("-------------------------------------------------------")
# allow url include for dvwa
# Read in the file
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('allow_url_include = Off', 'allow_url_include = On')

# Write the file out again
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'w') as file:
    file.write(filedata)
time.sleep(0.5)
print("Restart Apache2...")
os.system("sudo service apache2 restart")
print("-------------------------------------------------------")

print("[+] Now working with the files ")
# unzip files
os.system("sudo unzip file.zip")
time.sleep(0.5)
os.system("sudo unzip bWAPP.zip")
time.sleep(0.5)
os.system("sudo unzip sqli-labs.zip")
time.sleep(0.5)
os.system("sudo unzip hackademic.zip")
time.sleep(0.5)
os.system("sudo unzip dvwa.zip")
time.sleep(0.5)
os.system("sudo unzip mutillidae2.zip")
time.sleep(0.5)
os.system("sudo tar -xzvf xvwa.tar.gz")

# mov them
'''
os.system("sudo mv bWAPP /var/www/html/")
time.sleep(0.5)
os.system("sudo mv xvwa /var/www/html/")
time.sleep(0.5)
os.system("sudo mv dvwa /var/www/html/")
time.sleep(0.5)
os.system("sudo mv mutillidae /var/www/html/")
time.sleep(0.5)
os.system("sudo mv hackademic /var/www/html/")
time.sleep(0.5)
os.system("sudo mv sqli-labs /var/www/html/")
'''

os.system("sudo rm -r *.zip  *.gz")
time.sleep(0.5)
print("[+] Create a sample index.html")
time.sleep(0.5)
os.system("sudo mv index.html /var/www/html/index.html")
time.sleep(0.5)
os.system("sudo mv 873.jpg  c-logo-hd.png  /var/www/html")


'''
print("Step 8: Install the vulnerable servers")
os.system("sudo chmod -R 777 /var/www/html/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt")
os.system("sudo chmod -R 777 /var/www/html/dvwa/hackable/uploads")
os.system("sudo chmod -R 777 /var/www/html/dvwa/config")
os.system("sudo chmod 777 /var/www/html/bWAPP/passwords/")
os.system("sudo chmod 777 /var/www/html/bWAPP/images/")
os.system("sudo chmod 777 /var/www/html/bWAPP/documents/")
#os.system("sudo mkdir /var/www/html/bWAPP/logs/")
os.system("sudo chmod 777 /var/www/html/bWAPP/logs/")
os.system("sudo chown -R www-data:www-data /var/www/html/bWAPP/")
'''

print("Step 9: Create databases ")
import MySQLdb
# Simple routine to run a query on a database and print the results:
def doQuery(conn):
    cur = conn.cursor()
    # data dvwa;
    cur.execute("create database dvwa;")
    cur.execute("CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
    cur.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
    cur.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
    cur.execute("flush privileges;")
    time.sleep(0.5)
    # data sql;
    cur.execute("create database xvwa;")
    cur.execute("CREATE USER 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
    cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
    cur.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
    cur.execute("flush privileges;")
    time.sleep(0.5)
    # data bWAPP;
    cur.execute("CREATE USER 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
    cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
    cur.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
    cur.execute("flush privileges;")
    time.sleep(0.5)
    # data sql;
    cur.execute("create database security;")
    cur.execute("create database challenges;")
    cur.execute("CREATE USER 'sql'@'localhost' IDENTIFIED BY 'sql';")
    cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'sql'@'localhost';")
    cur.execute("SHOW GRANTS FOR 'sql'@'localhost';")
    cur.execute("flush privileges;")
    time.sleep(0.5)
    # data mutillidae;
    cur.execute("create database mutillidae;")
    cur.execute("CREATE USER 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
    cur.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
    cur.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
    cur.execute("use mysql;")
    cur.execute("flush privileges;")
    time.sleep(0.5)
    cur.execute("update user set authentication_string=PASSWORD('mutillidae') where user='mutillidae';")
    cur.execute("update user set plugin='mysql_native_password' where user='mutillidae';")
    cur.execute("flush privileges;")
    time.sleep(0.5)
    for firstname, lastname in cur.fetchall():
        print(firstname, lastname)
print("Using MySQLdb ... ")
myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
doQuery(myConnection)
myConnection.close()
print("Creating databases done ...... ")



os.system("clear")
f = open('banner.txt', 'r')
file_contents = f.read()
print("file_contents")
f.close()
def op_list():
    print("Chose any number to install what you want ")
    print("\033[1;30;40m [+] Enter (1) To install { bWAPP      }")
    print("\033[1;31;40m [+] Enter (2) To install { xvwa       }")
    print("\033[1;32;40m [+] Enter (3) To install { dvwa       }")
    print("\033[1;33;40m [+] Enter (4) To install { mutillidae }")
    print("\033[1;34;40m [+] Enter (5) To install { hackademic }")
    print("\033[1;35;40m [+] Enter (6) To install { sqli-labs  }")
    print("\033[1;37;40m [+] Enter (7) To install { ALL        }")
    print("\033[0;31;40m [+] Enter (8) Or anything To  { Exit  }")

print("\033[1;36;40m Welcome :) This is Nakerah-lab v1 ")
x = 1
op_list()
while x != 0:
    if x <= 7:
        try:
            x = int(input("Enter Your Order :"))
            if x == 1:
                print("Wait for install { bWAPP      }")
                os.system("sudo cp -r bWAPP /var/www/html/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/passwords/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/images/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/documents/")
                #os.system("sudo mkdir /var/www/html/bWAPP/logs/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/logs/")
                os.system("sudo chown -R www-data:www-data /var/www/html/bWAPP/")
                time.sleep(0.5)
                op_list()
            elif x == 2:
                print("Wait for install { xvwa       }")
                os.system("sudo cp -r xvwa /var/www/html/")
                time.sleep(0.5)
                op_list()
            elif x == 3:
                print("Wait for install { dvwa       }")
                os.system("sudo cp -r dvwa /var/www/html/")
                os.system("sudo chmod -R 777 /var/www/html/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt")
                os.system("sudo chmod -R 777 /var/www/html/dvwa/hackable/uploads")
                os.system("sudo chmod -R 777 /var/www/html/dvwa/config")
                time.sleep(0.5)
                op_list()
            elif x == 4:
                print("Wait for install { mutillidae }")
                os.system("sudo cp -r mutillidae /var/www/html/")
                time.sleep(0.5)
                op_list()
            elif x == 5:
                print("Wait for install { hackademic }")
                os.system("sudo cp -r hackademic /var/www/html/")
                time.sleep(0.5)
                op_list()
            elif x == 6:
                print("Wait for install { sqli-labs  }")
                os.system("sudo cp -r sqli-labs /var/www/html/")
                time.sleep(0.5)
                op_list()
            elif x == 7:
                print("Wait for install { All        }")
                os.system("sudo cp -r bWAPP /var/www/html/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/passwords/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/images/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/documents/")
                #os.system("sudo mkdir /var/www/html/bWAPP/logs/")
                os.system("sudo chmod 777 /var/www/html/bWAPP/logs/")
                os.system("sudo chown -R www-data:www-data /var/www/html/bWAPP/")
                time.sleep(0.5)
                os.system("sudo cp -r xvwa /var/www/html/")
                os.system("sudo cp -r dvwa /var/www/html/")
                os.system("sudo chmod -R 777 /var/www/html/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt")
                os.system("sudo chmod -R 777 /var/www/html/dvwa/hackable/uploads")
                os.system("sudo chmod -R 777 /var/www/html/dvwa/config")
                time.sleep(0.5)
                os.system("sudo cp -r mutillidae /var/www/html/")
                os.system("sudo cp -r hackademic /var/www/html/")
                os.system("sudo cp -r sqli-labs /var/www/html/")
                time.sleep(0.5)
                op_list()
        except:
            print(" You can't see the numbers ? enter something exist  ")
    else:
        break
print(" Goodbye Friend !!")
os.system("clear")
print("\033[0;32;40m ")
f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()

print("--------------------------------------------------------------")
print("Hello Friend ... ")
print("Now u can using yor lab ... ")
print("Just Open your Browser IP Machine = >>  : ")
os.system("IP=$(ifconfig|grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] Http://$IP/index.html")

