from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Blog

def index(request):
    
    return render(request, 'index.html')

def bio(request):
    
    return render(request, 'bio.html')


def book(request):
    
    return render(request, 'book.html')


def contact(request):
    
    return render(request, 'contact.html')


def video(request):
    
    return render(request, 'video.html')


def blog(request):
    # Retrieve all posts
    posts = Blog.objects.order_by('-published_date')

    # Set the number of posts per page
    posts_per_page = 9

    # Paginate the posts
    paginator = Paginator(posts, posts_per_page)

    # Get the current page number from the URL parameters
    page_number = request.GET.get('page')

    try:
        # Get the posts for the requested page
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': paginated_posts})


def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})


def search(request):
    query = request.GET.get('q', '')  # Get the user's search query
    blog_results = Blog.objects.none()
    

    if query:
        # Search across all categories
        blog_results = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
        )
       

    # Combine the results and pass them to the template
    context = {
        'query': query,
        'blog_results': blog_results,
        
    }
    return render(request, 'search_results.html', context)