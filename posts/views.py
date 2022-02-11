from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    paginate = p.get_page(page)

    return render(request, 'index.html', {'posts': posts, 'paginate': paginate})

def post(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'post.html', {'post': post})