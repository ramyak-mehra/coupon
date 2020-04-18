from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from coupan.models import Coupan
from django.core.paginator import Paginator
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username} , You Can Login Now')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES,
                             instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        user = request.user.profile.user_category
        if user == 'Company':
            coupans = Coupan.objects.filter(owner=request.user).order_by('-publish_date')
            paginator = Paginator(coupans , 2)
            page = request.GET.get('page')
            coupans = paginator.get_page(page)
            context = {
                'u_form': u_form,
                'p_form': p_form,
                'coupans' : coupans,
                'user' : user
            }
            return render(request, 'users/profile.html', context)
        else:
            context = {
                'u_form': u_form,
                'p_form': p_form,
            }
            return render(request, 'users/profile.html', context)

