from django.http import JsonResponse


from Blog.forms import AddPostForm, AddCommentForm
from Blog.models import Post, Blog, Comment
from UserManager.models import UserInfo


def get_posts(request, blog_id):
    ans = {}
    user = get_user(request)
    if user is None:
        print('invalid')
        return JsonResponse({'status': -1, 'message': 'invalid token'})
    print('In get posts', user)
    count = int(request.GET.get('count'))
    offset = int(request.GET.get('offset'))
    posts = list(Post.objects.filter(blog__blog_id=blog_id).order_by('time'))[offset:offset + count]
    ans['status'] = 1
    ans['posts'] = []
    for p in posts:
        temp = {'datetime': p.time, 'id': p.post_id, 'title': p.title, 'summary': p.summary}
        ans['posts'].append(temp)
    return JsonResponse(ans)


def get_post(request, blog_id):
    if request.method == 'GET':
        user = get_user(request)
        if user is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        post_id = request.GET.get('id')
        p = Post.objects.filter(post_id=post_id).first()
        post = {'datetime': p.time, 'id': p.post_id, 'title': p.title, 'summary': p.summary, 'text': p.text}
        ans = {'status': 1, 'post': post}
        return JsonResponse(ans)
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            summary = form.cleaned_data['summary']
            blog = Blog.objects.filter(blog_id=blog_id).first()
            if blog is not None:
                post = Post.create(blog, title, summary, text)
                post.save()
                return JsonResponse({'status': 1, 'message': 'Successfully Added The Post'})


def get_comments(request):
    ans = {}
    user = get_user(request)
    if user is None:
        return JsonResponse({'status': -1, 'message': 'invalid token'})
    post_id = request.GET.get('post_id')
    count = int(request.GET.get('count'))
    offset = int(request.GET.get('offset'))
    post = Post.objects.filter(post_id=post_id).first()
    comments = list(Comment.objects.filter(post=post).order_by('time'))[offset:offset + count]
    ans['status'] = 1
    ans['comments'] = []
    for c in comments:
        temp = {'datetime': c.time, 'text': c.text}
        ans['comments'].append(temp)
    return JsonResponse(ans)


# post_id text POST
def add_comment(request):
    if request.method == 'POST':
        user = get_user(request)
        if user is None:
            return JsonResponse({'status': -1, 'message': 'invalid token'})
        form = AddCommentForm(request.POST)
        if form.is_valid():
            print('form is valid')
            text = form.cleaned_data['text']
            post_id = form.cleaned_data['post_id']
            post = Post.objects.filter(post_id=post_id).first()
            if post is not None:
                comment = Comment.create(post, text)
                comment.save()
                print(comment)
                ans = {'status': 1}
                temp = {'text': text, 'datetime': comment.time}
                ans['comment'] = temp
                print(ans)

                return JsonResponse({'status': 1, 'comment': ans})
        else:
            print('form is not valid')
    return JsonResponse({'status': -1, 'message': 'Under Construction'})


def get_user(request):
    token = request.META.__getitem__('HTTP_X_TOKEN')
    user = UserInfo.objects.filter(token=token).first()
    if user is not None:
        return user.user
    return None
