from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator

def registration(request):
    if request.method == 'POST':
        # Process registration form data
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user account (do not activate yet)
        user = User.objects.create_user(email, password)
        user.is_active = False
        user.save()

        # Generate activation token and link
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        current_site = get_current_site(request)
        activation_link = f"http://{current_site}/activate/{uid}/{token}/"

        # Send activation email
        subject = 'Activate your account'
        message = render_to_string('activation_email.html', {
            'user': user,
            'activation_link': activation_link,
        })
        from_email = 'danya.pochta76@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return redirect('activation_pending')
    return render(request, 'user/templates/user/Registraion/registration.html')
