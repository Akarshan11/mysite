
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .models import Student
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tution.forms import ContactForm
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

# Create your views here.


def index(request):
    return render(request, 'tution/index.html', context=None)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']

            email = form.cleaned_data['email']

            user.save()

            return redirect('personal')
    else:
        form = UserForm()
    return render(request, 'tution/register.html', {'form': form})


def home(request):
    all_student = Student.objects.all()
    context = {'all_student': all_student}

    return render(request, 'tution/home.html', context)


def personal(request):
    return render(request, 'tution/personal.html', context=None)


def academic(request):
    return render(request, 'tution/form2.html', context=None)


class StudentCreate(CreateView):

    model = Student
    fields = ['name', 'f_name', 'dob', 'mob', 'email', 'address', 'pic']



def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('tution/contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['youremail@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('home')

    return render(request, 'tution/contact.html', {'form': form_class})
