from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import Users
from .forms import UserForm

# Create your views here.

def index(request):
    my_users = Users.objects.all()
    print(my_users)
    return render(
        request,
        'index.html',
        {'my_users': my_users}
    )


def form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_application:index'))
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def detail(request, user_id):
    user = get_object_or_404(Users, id=user_id)
    return render(request, 'details.html', context={'user': user})
