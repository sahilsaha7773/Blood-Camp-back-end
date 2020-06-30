from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, Http404
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from django.http import JsonResponse
# Create your views here.

def user_login(request):
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated succesfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = LoginForm()

	return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
	f = Friend.objects.friends(request.user)
	users = User.objects.filter(is_active=True).exclude(username=request.user.username).exclude(is_superuser=True)
	return render(request, 'account/dashboard.html', {'section': dashboard, 'f': f})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		profile_form = ProfileEditForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()

			Profile.objects.create(user=new_user)
			ProfileEditForm(instance=new_user.profile, data=request.POST).save()
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
		profile_form = ProfileEditForm()
	return render(request, 'account/register.html', {'user_form': user_form, 'profile_form':profile_form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		
	return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def user_list(request):
	friends = Friend.objects.friends(request.user)
	friends = len(friends)
	users = User.objects.filter(is_active=True).exclude(username=request.user.username).exclude(is_superuser=True)
	return render(request, 'account/user/list.html', {'section': 'people', 'users': users, 'friends': friends})

@login_required
def user_detail(request, username):
	user = get_object_or_404(User, username=username, is_active=True)
	if(user==request.user):
		return edit(request)
	f = Friend.objects.friends(request.user)
	flag = 0
	for i in f:
		if i==user:
			flag = 1
			break
	friendsr = Friend.objects.unread_requests(user=user)
	for j in friendsr:
		if j.from_user==request.user:
			flag = 2
			break
	return render(request, 'account/user/detail.html', {'section': 'people', 'user': user, 'flag': flag})
	

@login_required
def flist(request):#friend requests
	friendsr = Friend.objects.unread_requests(user=request.user)
	return render(request, 'account/user/flist.html', {'friends': friendsr, 'section': 'friend_requests'})

@login_required
def frequest(request, username):
	other_user = get_object_or_404(User, username=username, is_active=True)
	# other_user = User.objects.get(pk=1)
	Friend.objects.add_friend(
	    request.user,                               # The sender
	    other_user,                                 # The recipient
	    message='Hi! I would like to add you')      # This message is optional
	return JsonResponse({'sent':1})

@login_required
def fconfirm(request, username):
	from friendship.models import FriendshipRequest
	friend_request = FriendshipRequest.objects.get(to_user=request.user,from_user=username)
	friend_request.accept()
	return JsonResponse({'confirmed':1})
	# or friend_request.reject()

@login_required
def freject(request, username):
	from friendship.models import FriendshipRequest
	friend_request = FriendshipRequest.objects.get(to_user=request.user,from_user=username)
	friend_request.reject()
	return JsonResponse({'rejected':1})

@login_required
def fl(request):#friends
	friends = Friend.objects.friends(request.user)
	return render(request, 'account/user/lf.html', {'friends': friends, 'section':'confirmed'})