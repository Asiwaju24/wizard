from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import random
from django.http import FileResponse, Http404

# Create your views here.



def test_404(request):
    raise Http404("Page not found!")

def home(request):
    projects = Projects.objects.all()
    blogs = Blog.objects.all().order_by('-posted_at')[:3] 
    context = {
        'projects': projects,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)

def about(request):
    team = Team.objects.all()
    feedback = Feedback.objects.all()
    colors = ['#FAD9A1', '#B9FBC0', '#CDB4DB', '#A1C9F1', '#FFC2C2', '#E2F0CB']

    context = {
        'feedback': feedback,
        'team': team,
    }
    for feedback in feedback:
        feedback.bg_color = random.choice(colors)
    return render(request, 'about.html', context)



def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'services.html')

def tech(request):
    field = Field.objects.all()
    language = Language.objects.all()

    context ={
        'field': field,
        'language': language,    
    }
    return render(request, 'tech.html', context)


def download_pdf(request, post_id):
    post = get_object_or_404(Language, pk=post_id)

    if not post.pdf:
        raise Http404("PDF not found.")

    return FileResponse(post.pdf.open('rb'), as_attachment=True, filename=post.pdf.name.split('/')[-1])


def download_field_pdf(request, field_id):
    post = get_object_or_404(Field, pk=field_id)

    if not post.pdf:
        raise Http404("PDF not found.")

    return FileResponse(post.pdf.open('rb'), as_attachment=True, filename=post.pdf.name.split('/')[-1])


def field_detail(request, id):
    field = get_object_or_404(Field, id=id)
    return render(request, 'field_detail.html', {'field': field})


def language_detail(request, id):
    language = get_object_or_404(Language, id=id)
    return render(request, 'language_detail.html', {'language': language})



def blog(request):
    posts = Blog.objects.all().order_by('-posted_at')
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'post': post})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Subscriber.objects.get_or_create(email=email)  # Avoid duplicates
            messages.success(request, "You've successfully subscribed!")
    return redirect(request.META.get('HTTP_REFERER', '/'))


@csrf_exempt
def inquiry(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            full_name=request.POST.get('fullName'),
            email=request.POST.get('email'),
            project_type=request.POST.get('projectType'),
            budget=request.POST.get('budget'),
            timeline=request.POST.get('timeline'),
            message=request.POST.get('message')
        )
        return render(request, 'inquiry_success.html')  # Or redirect to a success page
    return render(request, 'inquiry.html')  # The form page


def inquiry_confirm(request):
    inquiry_data = request.session.get('inquiry_data')
    if not inquiry_data:
        return redirect('inquiry_step1')

    if request.method == 'POST':
        # Save to DB
        form = InquiryForm(inquiry_data)
        if form.is_valid():
            form.save()
            del request.session['inquiry_data']  # Clean up
            return redirect('inquiry_success')

    return render(request, 'inquiry_confirm.html', {'inquiry': inquiry_data})


def inquiry_success(request):
    return render(request, 'inquiry_success.html')
