from django.db import models
import re

class UserManager(models.Manager):
	def basic_validation(self, postdata):
		# empty error dictionary for messages to pop up
		errors ={}
		# make sure email is correct
		email_validate = re.compile(r'^[a-zA-Z0-9._-}+\.[a-zA-Z]+$')
		# setting password min characters same with first & last
		if len(postdata['password']) < 8:
			errors['password'] = "Your password needs to be 8 characters or more"
		if len(postdata['first_name']) < 2:
			errors['first_name'] = "Your first name must be 2 characters or more"
		if len(postdata['last_name']) < 2:
			errors['last_name'] = "Your last name must be 2 characters or more"
		# calling function to validate email 
		if not email_validate.match(postdata['email']):
			errors['email'] = "Email must be valid"
		# make sure passwords are matching
	 	if postdata['password'] != postdata['confirmPassword']:
	 		errors['password'] = "Passwords must match"
		return errors

# user info 
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=25)
	# to call the above error and validation class
	objects = UserManager()

#Comment model, in old mysql workbench assignment
class Comment(models.Model):
	# actual comment
	comment = models.TextField()
	# User to Comment
	poster = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
	# Comment to Wall
	wall = models.ForeignKey(Wall, related_name='user_comment', on_delete=models.CASCADE)

# Wall post
class Wall(models.Model):
	# content of post
	post = models.TextField()
	# user to comment
	poster = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
	# stores who likes post many-to-many
	likes = models.ManyToManyField(User, related_name='liked_post')



# Create your models here.
