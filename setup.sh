#!/bin/bash
php_v=$(php --version | grep -i 'PHP'|cut -d ')' -f 1 | head -1 | cut -c 5-10|cut -d '.' -f 1,2)
export php_v

sudo source ~/.bashrc

sudo python Nakerah-lab.py
