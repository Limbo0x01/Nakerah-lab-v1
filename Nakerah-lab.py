#!/usr/bin/python3
import os
import sys
import time

f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
PHP_V=sys.argv[1]


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
os.system("sudo ufw status")
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

os.system("sudo apt-get install python3-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("sudo pip install MySQL-python -y")
os.system("sudo apt install python3-pip")

os.system("sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip2.py")
os.system("sudo python get-pip2.py")



os.system("curl -O https://bootstrap.pypa.io/pip/2.7/get-pip.py")
os.system("python get-pip.py")
os.system("python -m pip install --upgrade 'pip < 21.0'")
os.system("sudo apt-get install python-dev default-libmysqlclient-dev -y")


os.system("sudo apt-get install python3-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("sudo pip install MySQL-python -y")

os.system("sudo apt install libmariadb3 libmariadb-dev -y")
os.system("sudo apt install mariadb-server -y")
os.system("sudo service mariadb start")
os.system("pip3 install mariadb")
###########mutillidae 

os.system("sudo apt update -y")
os.system("sudo apt install php-xml php-fpm libapache2-mod-php php-mysql php-gd php-imap php-mysql php-curl php-mbstring -y")
os.system("sudo a2enmod proxy_fcgi setenvif")
os.system("sudo systemctl restart apache2")
os.system("sudo a2enconf php7.4-fpm")
os.system("sudo systemctl reload apache2")
os.system("sudo systemctl restart apache2.service")
os.system("sudo service php7.4-fpm restart")
os.system("sudo systemctl restart mysql")
######################
os.system("sudo apt-get install python-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("pip install pymysql -y")
os.system("pip3 install mysql-connector-python")
os.system("sudo apt install python3-dev libpython3-dev")
os.system("sudo apt install python3-mysqldb")
os.system("sudo apt-get install libmysqlclient-dev -y")
os.system("sudo -H pip3 install mysqlclient -y")
os.system("sudo apt-get install python3-dev libmysqlclient-dev -y")

os.system("pip install MySQL-python")

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
print("--------------------------------------------------------")
# allow url include for dvwa
# Read in the file
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('display_errors = Off', 'display_errors = On')

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
os.system("sudo rm -r mutillidae2.zip")
os.system("sudo rm -r mutillidae")

os.system("sudo git clone https://github.com/webpwnized/mutillidae")
time.sleep(0.5)
os.system("sudo tar -xzvf xvwa.tar.gz")


os.system("sudo rm -r *.zip  *.gz")
time.sleep(0.5)
print("[+] Create a sample index.html")
time.sleep(0.5)
os.system("sudo mv index.html /var/www/html/index.html")
time.sleep(0.5)
os.system("sudo mv 873.jpg  c-logo-hd.png  /var/www/html")


try:
    print("Step 9: Create MariaDB databases ")
    import mariadb
    time.sleep(0.5)
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="mysql"

    )

    print("Creating databases....")
    cursor = conn.cursor()
    print("Step 9.1: Creating dvwa database ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  dvwa;")
    cursor.execute("CREATE USER IF NOT EXISTS 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
    cursor.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("dvwa fninshed")
    
    # data xvwa;
    print("Step 9.2: Creating xvwa database ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  xvwa;")
    cursor.execute("CREATE USER IF NOT EXISTS 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("SQL fninshed")
    # data bWAPP;
    print("Step 9.3: Creating bWAPP database ")
    cursor.execute("CREATE USER IF NOT EXISTS 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    # data sql;
    print("Step 9.4: Creating secursority and challenges databases ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  secursority;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS  challenges;")
    cursor.execute("CREATE USER IF NOT EXISTS 'sql'@'localhost' IDENTIFIED BY 'sql';")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'sql'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'sql'@'localhost';")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("9.4 secursority & challenges fninshed")
    # data mutillidae;
    print("Step 9.5: Creating mutillidae  database")
    cursor.execute("CREATE DATABASE IF NOT EXISTS mutillidae;")
    cursor.execute("CREATE USER IF NOT EXISTS 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
    cursor.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
    cursor.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
    cursor.execute("use mysql;")
    cursor.execute("flush privileges;")
    print("mutillidae part 1")
    time.sleep(0.5)
    cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY 'mutillidae';")
    cursor.execute("SET PASSWORD FOR 'root'@'localhost' = PASSWORD('mutillidae');")
    cursor.execute("flush privileges;")
    time.sleep(0.5)
    print("mutillidae part 2")

    print("Every thing is going well...")
    conn.close()

except:
    import MySQLdb
    print("Step 10: Create mysql databases ")

    hostname = 'localhost'
    username = 'root'
    password = ''
    database = 'mysql'


    # Simple routine to run a query on a database and print the results:
    def doQuery(conn):
        cur = conn.cursor()
        # data dvwa;
        print("Step 9.1: Creating DVWA database ")
        cur.execute("CREATE DATABASE IF NOT EXISTS dvwa;")
        cur.execute("CREATE USER IF NOT EXISTS 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
        cur.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data sql;
        print("Step 9.2: Creating XVWA database ")
        cur.execute("CREATE DATABASE IF NOT EXISTS xvwa;")
        cur.execute("CREATE USER IF NOT EXISTS 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
        cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data bWAPP;
        print("Step 9.3: Creating BWAPP database ")
        cur.execute("CREATE USER IF NOT EXISTS 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
        cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data sql;
        print("Step 9.4: Creating security and challenges databases ")
        cur.execute("CREATE DATABASE IF NOT EXISTS security;")
        cur.execute("CREATE DATABASE IF NOT EXISTS challenges;")
        cur.execute("CREATE USER IF NOT EXISTS 'sql'@'localhost' IDENTIFIED BY 'sql';")
        cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'sql'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'sql'@'localhost';")
        cur.execute("flush privileges;")
        time.sleep(0.5)
        # data mutillidae;
        print("Step 9.5: Creating mutillidae database ")
        cur.execute("CREATE DATABASE IF NOT EXISTS mutillidae;")
        cur.execute("CREATE USER IF NOT EXISTS 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
        cur.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
        cur.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
        cur.execute("use mysql;")
        cur.execute("flush privileges;")
        print("mutillidae part 1")
        time.sleep(0.5)
        
        cur.execute("update user set authentication_string=PASSWORD('mutillidae') where user='mutillidae';")
        cur.execute("update user set plugin='mysql_native_password' where user='mutillidae';")
        cur.execute("flush privileges;")
        time.sleep(0.5)

        print("mutillidae part 2")
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
                os.system("sudo cp -r mutillidae /var/www/html/ ;sudo chown -R www-data:www-data /var/www/html/mutillidae/")

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
                os.system("sudo cp -r mutillidae /var/www/html/ ;sudo chown -R www-data:www-data /var/www/html/mutillidae/")
                os.system("sudo cp -r hackademic /var/www/html/")
                os.system("sudo cp -r sqli-labs /var/www/html/")
                time.sleep(0.5)
                op_list()
        except:
            print(" You can't see the numbers ? enter something exist  ")
    else:
        break
print(" Goodbye Friend !!")
os.system("sudo service apache2 restart")
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

