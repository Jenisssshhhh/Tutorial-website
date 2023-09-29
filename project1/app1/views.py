from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import UserAccount,Topic,Course,Category,Difficultylevel,Message
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from validate_email import validate_email
from django.core.exceptions import ValidationError


def home(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render (request,'index.html',{'courses':courses,'categories':categories})

def about(request):
    return render(request,'about.html')

def topics(request, course_id):
    topics = Topic.objects.filter(course_id=course_id)
    
    # Create a set to store all difficulty levels for the topics
    levels_for_topics = set()
    
    for topic in topics:
        if topic.level:
            levels_for_topics.add(topic.level)
    
    return render(request, 'topics.html', {'topics': topics, 'levels': levels_for_topics})

def courses(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request,'courses.html',{'courses':courses,'categories':categories})


def category(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id)

    courses = Course.objects.filter(category=selected_category)
    
    context = {
        'selected_category': selected_category,
        'courses': courses,
    }
    
    return render(request, 'category.html', context)


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        # Check if email already exists
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered", extra_tags='user')
            return redirect("signup")
        
        if password != confirm_password:
            messages.error(request, "Passwords don't match", extra_tags='user')
            return redirect('signup')

        user = UserAccount.objects.create_user(email=email, password=password)
        messages.success(request, "Signup successful. You are now logged in", extra_tags='user')
        login(request, user)  # Automatically log in the user
        return redirect('home')  # Replace 'home' with your home page URL

    return render(request, 'signup.html')

        



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password!!!", extra_tags='user')
            return redirect('login')

    return render(request, 'login.html')





def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Please provide a valid email address.', extra_tags='user')
        else:
            message = Message(name=name, email=email, subject=subject, message=message_text)
            message.save()

            messages.success(request, 'Message sent successfully.', extra_tags='user')

    return render(request, 'contact.html')
