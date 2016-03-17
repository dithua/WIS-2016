import json
import urllib2
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'  # print msg
print 'Argument List:', str(sys.argv)  # print msg 

if len(sys.argv) > 1 :   # check if user passed argument
	data = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts?userId='+sys.argv[1]))  #call api using user's argument
	print 'Data counter :', len(data), 'posts.' # print msg 
	if len(data) > 0:  # check if data var has values using length
		ans = raw_input('Do you want to print them?')  #ask user if wants to print posts
		if ans == 'y' or ans == 'Y':
			for json_object in data:  #print all posts data
				print "User Id: \t"+ str(json_object['userId'])
				print "Post Id: \t"+ str(json_object['id'])
				print "Title: \t"+ str(json_object['title'])
				print "Body: \t"+ str(json_object['body']) +"\n"
				comments = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+str(json_object['id'])+'/comments' ))  #call api to fetch comments for each post

				print "~~~~~~~~~~~~ Comments ~~~~~~~~~~~~~~" # print msg 
				for json_comments in comments:  #print all comments
					print "name: \t"+ str(json_comments['name'])
					print "email: \t"+ str(json_comments['email'])
					print "body: \t"+ str(json_comments['body'])+"\n"
				print "~~~~~~~~~~~~ END of Comments for post with id " + str(json_object['id']) +"~~~~~~~~~~~~~~~~~~~~\n"

		else:
			sys.exit(0)  # exit 
	else:
		print 'No posts found!' # print msg 
else:
	print 'usage : ' + sys.argv[0] + 'postID' # print msg 
