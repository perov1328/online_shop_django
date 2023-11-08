from random import randint

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from users.models import User

@login_required
def generate_new_password(request):
    new_password = ''.join([str(randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:catalog'))

def verify(request):
    if request.method == 'POST':
        number = request.POST.get('number')
    try:
        user = User.objects.get(verification_code=number)
        user.verified = True
        user.save()
        return redirect(reverse('users:login'))
    except:
        return render(request, 'users/verification.html')