from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .forms import LoginForm
from .models import Teacher, Student, Assignment
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ass_index')
        else:
            error_message = 'You put the incorrect credentials TRY AGAIN!'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class AssCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['name', 'description', 'due_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AssUpdate(UpdateView):
    model = Assignment
    fields = ['title', 'description', 'due_date']


class AssDelete(DeleteView):
    model = Assignment


def home(request):
    return render(request, 'home.html')


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        next = request.POST.get('next') or None
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and next is not None:
                login(request, user)
                return redirect(next)
            elif user is not None and next is None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Sorry, your username or password was invalid'
    form = LoginForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def ass_index(request):
    assignments = Assignment.objects.filter(user = request.user)
    return render (request, 'Assignment/index.html', {'assignments': assignments})


def ass_detail(request, ass_id):
    ass = Assignment.objects.get(id=ass_id)


@login_required
def assoc_student(request, assignment_id, student_id):
    Assignment.objects.get(id=assignment_id).students.add(student_id)
    return redirect('detail', student_id=student_id)


@login_required
def unassoc_student(request, assignment_id, student_id):
    Assignment.objects.get(id=assignment_id).students.remove(student_id)
    return redirect('detail', student_id=student_id)

def StudentCreate(request):
    return render(request, 'home.html')
