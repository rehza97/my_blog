from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Tag
# that how we use pagination
from django.core.paginator import PageNotAnInteger , EmptyPage, Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    
    context ={
        'blogs' : blogs,
        'tags' : tags
    }
    return render(request , 'home.html',context)

def blogs(request):
    queryset = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    # pagintion code
    page = request.GET.get('page',1)
    paginator = Paginator(queryset , 4)
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')
    context ={
        'blogs' : blogs,
        'tags' : tags,
        'paginator' : paginator,
        }
    return render(request , 'blog.html',context)


def category_blogs(request , slug):
    category = get_object_or_404(Category , slug=slug)
    queryset = category.category_blog.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    page = request.GET.get('page',1)
    paginator = Paginator(queryset , 4)
    all_blogs = Blog.objects.order_by('-created_date')[:5]
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')
    context ={
        'blogs' : blogs,
        'tags':tags,
        'paginator' : paginator,
        'all_blogs' : all_blogs,
        
    }
    return render(request , 'category_blog.html',context)
def tag_blogs(request , slug):
    tag = get_object_or_404(Tag , slug=slug)
    queryset = tag.tag_blog.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    page = request.GET.get('page',1)
    paginator = Paginator(queryset , 4)
    all_blogs = Blog.objects.order_by('-created_date')[:5]
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')
    context ={
        'blogs' : blogs,
        'tags':tags,
        'paginator' : paginator,
        'all_blogs' : all_blogs,
        
    }
    return render(request , 'category_blog.html',context)

def post_details(request , slug):
    blog = get_object_or_404(Blog , slug=slug)
    context ={
        'blog' : blog,
    }
    return render(request , 'post-details.html',context)