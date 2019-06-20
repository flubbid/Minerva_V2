from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    error_message = ''
    if reqeuest.method == 'POST'
    form = UserCreationForm(request.POST)
    if form.is.valid():
        user = form.save()
        login(request, user)
        return redirect('index')
        else:
            error_message = 'You put the incorrect credentials TRY AGAIN!'
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)

@login_required 
class AssCreate(CreateView):
    model = Assignment
    fields = ['title', 'description', 'due_date']

class AssUpdate(UpdateView):
    model = Assignment
    fields = ['title', 'description', 'due_date']

class AssDelete(DeleteView):
    model = Assignment 

def home(request):
    return render(request, 'home.html')

def ass_index(request):
    assignments = Assignment.objects.all()
    return render (request, 'assignment/index.html', 'assignments': assignments)

def ass_detail(request, ass_id):
    ass = Assignment.objects.get(id=ass_id)
