
#!/bin/bash
sudo apt-get install php7.2-curl php7.2-mbstring php7.2-xml -y
sudo apt-get install php7.3-curl php7.3-mbstring php7.3-xml -y
sudo apt-get install php php-mysqli php-gd libapache2-mod-php -y
sudo apt install hhvm

export PHP_limbo=$(php --version | grep -i 'PHP'|cut -d ')' -f 1 | head -1 | cut -c 5-10|cut -d '.' -f 1,2)


source ~/.bashrc
echo $PHP_limbo

sudo python3 Nakerah-lab.py $PHP_limbo
