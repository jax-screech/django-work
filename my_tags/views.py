from django.shortcuts import render
import datetime
from .models import Blog
import markdown
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    return render(request, 'index.html',context={"x": "welcome to django"})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def filter_demo(request):
    context = {
        "my_string": "Hello world!",
        "my_date": datetime.date(2025, 6, 18),
        "long_string": "This is a long string to be displayed entirely",
        
        "new_str": "Lets eat!",
        # assignments
        "random_str":"this string is a string",
        "people_str": ["Bob", "Sydney", "Lee", "Jordan", "Joe", "Pierre", "John", "Lisa"],
        "people_str2": "Alice\nBob\n\nCharlie\nDavid",
    }
    return render(request, 'filters.html', context)

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs': blogs})