from django.shortcuts import render
from posts.models import Post

# Create your views here.
def home(requests):
    context = {
        'posts': Post.objects.all(),
        'group_posts': dilemeter_data_on_the_page(Post.objects.all(), 2)
    }
    return render(requests, 'home.html', context=context)

def about_us(requests):
    return render(requests, 'about_us.html')

def dilemeter_data_on_the_page(data, elements_in_group):
    iter = len(data) // elements_in_group
    data_grouped = []
    for i in range(iter):
        data_grouped.append(data[i * elements_in_group:(i + 1) * elements_in_group])
    if not len(data) % elements_in_group == 0:
        data_grouped.append(data[iter*elements_in_group:])
    return data_grouped

