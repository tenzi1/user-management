from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test


from .forms import CustomUserCreationForm, CustomUserChangeForm

def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully created account!')
            return redirect(reverse('dashboard'))
    else:
        form=CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form':form })


# user decorator
def get_user(request, pk):
    if request.user.pk == pk:
        return get_object_or_404(User, pk=pk)
    else:
        return request.user

def profile(request, pk):
    user = get_user(request,pk)
    # user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', args=(pk,)))
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'accounts/profile.html', {'form':form})




