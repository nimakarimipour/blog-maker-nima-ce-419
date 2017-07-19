from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    summary = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200)


class AddCommentForm(forms.Form):
    text = forms.CharField(max_length=200)
    post_id = forms.IntegerField()
