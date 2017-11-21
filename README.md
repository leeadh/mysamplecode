### 

ENV Setup

step 1 : go to AWS console and get an EC2 instance (tier 2 micro)- Linux AMI 
step 2: set up EC2 with pem keys (Or ppk if you are a window user)
step 3: run sudo yum update
step 4: sudo -i
step 5: yum install php5 mysql5-server httpd for apache server and php
step 6: yum install php
step 7: go to wordpress website (https://wordpress.org/download/ )and then copy https://wordpress.org/latest.tar.gz
Step 8: go to root and then # /etc/init.d/mysqld start to start mysql server
step 9: go to cd/var/www/html
step 10: # wget https://wordpress.org/latest.tar.gz (from step 7)
Step 11: unzip tar file : tar xzf latest.tar.gz
Step 12 : chown -R apache.apache wordpress
Step 13: vi /etc/httpd/conf/httpd.conf
Step 14: /etc/init.d/httpd restart
step 15: go to the public ip address in EC2 : http://13.228.23.120/wordpress/


======= Additional Step: Incase you run into a"Your PHP installation appears to be missing the MySQL extension which is required by WordPress."=====

Do the following

*resolution https://wordpress.org/support/topic/your-php-installation-appears-to-be-missing-the-mysql-extension-which-is-require

1) yum install -y mysql mysql-server - Ensure that MySQL and MySQL server are installed

2) yum install -y php php-mysql - Ensure that PHP and the PHP MySQL components are installed

3) Restart Apache﻿


To run python script 
1) Install python
2) Install numphy: pip install numpy
3) install wordpress XML RPC: pip install python-wordpress-xmlrpc
4) install pandas: pip install pandas
5) naviagte to directory and run python wordpressscript.py