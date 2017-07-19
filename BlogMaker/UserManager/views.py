from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse

from Blog.models import Blog
from UserManager.forms import SignIn, SignUp, TestForm
from UserManager.models import UserInfo

# todo Upload images.


def sign_in(request):
    if request.method == 'POST':
        form = SignIn(request.POST)
        ans = {}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                ans['status'] = 1
                token = UserInfo.objects.all().filter(user__username=username).first()
                ans['token'] = token.token
                return JsonResponse(ans)
            else:
                ans['status'] = -1
                ans['message'] = 'wrong password'
            return JsonResponse(ans)
        else:
            ans['status'] = -1
            if form.error_message is not '':
                ans['message'] = form.error_message
            else:
                ans['message'] = 'unknown error happened'
            return JsonResponse(ans)
    else:
        print('Not a POST method')


def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        ans = {}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            blog = Blog.objects.create(owner=user, name='Home-' + user.username)
            user_info = UserInfo.create_user_info(user, blog)
            ans['status'] = 1
            ans['message'] = 'Successfully Created User.'
            user.save()
            blog.save()
            user_info.save()
            return JsonResponse(ans)
        else:
            print('Form is not valid')
            ans['status'] = -1
            if form.error_message is not '':
                ans['message'] = form.error_message
            else:
                ans['message'] = 'unknown error happened'
            return JsonResponse(ans)
    else:
        print('Not a POST method')


def get_home_blog_id(request):
    if request.method == 'GET':
        user = get_user(request)
        if user is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        username = user.username
        blog = Blog.objects.filter(owner__username=username).first()
        ans = {'blog_id': blog.blog_id, 'name': blog.name}
        return JsonResponse(ans)


def get_user(request):
    token = request.META.__getitem__('HTTP_X_TOKEN')
    user = UserInfo.objects.filter(token=token).first()
    if user is not None:
        return user.user
    return None


def test(request):
    if request.method == 'POST':
        ans = {'status': 1}
        print(request.META.__getitem__('HTTP_X_TOKEN'))
        form = TestForm(request.POST)
        if form.is_valid():
            print('Its valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            title = form.cleaned_data['title']
            print(username, password, title)
            return JsonResponse(ans)
        else:
            print(form.error_message)
            return JsonResponse({'status': -1, 'message': 'form not right'})
