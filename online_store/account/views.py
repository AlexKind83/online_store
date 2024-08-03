from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


@login_required
def main_page(request):
    return render(request, 'store/main_page.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})



