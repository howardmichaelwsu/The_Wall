from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# home page render
def index(request):
	return render(request, 'index.html')

# register
def register(request):
	errors = User.objects.basic_validation(request.POST)
	#checking the user entering all info
	if len(errors) > 0:
		for key, value in errors.item():
			messages.error(request, value)
		return redirect('/')
	new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
	request.session['user'] = new_user.first_name
	request.session['id'] = new_user.id
	#will render new page if successful and will also store user info so they can stay logged in
	return redirect('/success')

#login for exsiting user
def login(request):
	logged_user = User.objects.filter(email=request.POST['email'])
	if len(logged_user) > 0:
		logged_user = logged_user[0]
		if logged_user.password == request.POST['password']:
			request.session['user'] = logged_user.first_name
			request.session['id'] = logged_user.id
			return redirect('/success')
	return redirect('/')

def success(request):
	if 'user' not in request.session:
		return redirect('/')
	context = {
		'wall_post': Wall_Post.objects.all()
	}
	return render(request, 'success', context)

# logout for user and returing home
def logout(request):
	request.session.flush()
	return redirect('/')

def messaging(request):
	# wall post and getting user id that posting it
	Wall_Post.objects.create(message=request.POST['message'], poster=User.objects.get(id=request.session['id']))
	return redirect('/success')

#post comment under messaging
def post_comment(request, id):
	poster = User.objects.get(id=request.session['id'])
	message = Wall_Post.objects.get(id=id)
	Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_post=message)
	return redirect('/success')

def profile(request, id):
	context = {
		'user': User.objects.get(id=id)
	}
	return render(request, 'profile.html', context)

def likes(request, id):
	liked_post = Wall_Post.objects.get(id=id)
	user_likes = User.objects.get(id=request.session['id'])
	liked_post.user_like.add(user_likes)
	return redirect('/success')

def edit(request, id):
	edit_user = User.objects.get(id=id)
	edit_user.first_name = request.POST['first_name']
	edit_user.last_name = request.POST['last_name']
	edit_user.email = request.POST['email']
	edit_user.save()
	return redirect('/success')


# Create your views here.
