from django.shortcuts import render

posts = [
    {
        'author': 'Howard',
        'title': 'Posty',
        'content': 'Firsty yeahhhh',
        'date_posted': 'August 7, 2020'
    },
    {
        'author': 'Ainslee',
        'title': 'Posty Two',
        'content': 'Secondy yeahhhh',
        'date_posted': 'August 7, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
