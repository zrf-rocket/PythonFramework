from django.contrib.auth.models import User
from django.http import HttpResponseRedirect  # 重定向
from django.shortcuts import (
    redirect,  # 重定向
    render,
    get_object_or_404
)
from django.urls import (
    resolve,  # 重定向
    reverse
)

from .forms import ProfileForm


def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return HttpResponseRedirect(reverse('user:profile', args=[user.id]))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name}
        form = ProfileForm(default_data)
    return render(request, 'users/profile_update.html', {'form': form, 'user': user})

# User.objects.create_user(
#     first_name=first_name,
#     last_name=last_name,
#     username="Cramer",
#     email="rocket_2014@126.com",
#     password="123456"
# )
# User.objects.create_superuser(
#     first_name=first_name,
#     last_name=last_name,
#     username="SteveRocket",
#     email="rocket_2014@126.com",
#     password="123456"
# )
