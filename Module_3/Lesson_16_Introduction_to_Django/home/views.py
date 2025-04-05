from django.shortcuts import render

def index(request):
    """
    Render the index page of the home app.
    """
    return render(request, 'home/index.html')

def about(request):
    """
    Render the about page with a dynamic message.
    
    Returns:
        HttpResponse: The rendered about page.
    """
    context = {
        "message": "This is the About page of our Django application, demonstrating URL routing, views, and dynamic templates."
    }
    return render(request, 'home/about.html', context)