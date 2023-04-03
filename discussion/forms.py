from .models import Post, Reply
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"}),
            'description': forms.Textarea(attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"})
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('description',)
        widgets = {
            'description': forms.Textarea(attrs={"class": "text-gray-800 border-2 border-gray-700 rounded-lg focus:outline-none block w-[95%] mr-2 py-1.5", "rows": "4"})
        }
