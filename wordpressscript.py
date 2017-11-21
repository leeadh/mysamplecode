from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import pandas as pd
import os,sys
import datetime
import numpy as np
import functools
import datetime as dt   


#authenticate
wp_url = "http://13.228.23.120/wordpress/xmlrpc.php"
wp_username = "admin"
wp_password = "4p7lP1y%1YtZKhNLnF"
wp = Client(wp_url, wp_username, wp_password)

#reading the file
xls = pd.ExcelFile('input.xlsx');
posts = xls.parse('Posts');

for index, row in posts.iterrows():
	title = row['Title']
	content = row['Content']
	post = WordPressPost()
	post.title = title
	post.content = content
	post.post_status = 'publish'
	post.terms_names = {
	  'post_tag': ['test', 'firstpost'],
	  'category': ['Introductions', 'Tests']
	}
	wp.call(NewPost(post))



print("====Posts Added ====")
