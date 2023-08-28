import json
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from django.http import JsonResponse

User = get_user_model()

def authorization(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(username=username, email=email, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('service'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/Authorization/authorization.html', context)



def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('authorization'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/Registration/registration.html', context)


def profile(request):
    form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
               }
    return render(request, 'user/profile/profile.html', context)


"""def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Генерируем токен и формируем ссылку
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            activation_link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
            activation_url = f'http://{current_site}{activation_link}'

            # Отправляем письмо
            subject = 'Активация аккаунта на сайте RDC'
            message = render_to_string('user/activation_email.html', {
                'user': user,
                'activation_link': activation_url,
            })
            from_email = 'noreply@rdc.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Вы успешно зарегистрировались! Пожалуйста, проверьте свою почту для активации аккаунта.')
            return HttpResponseRedirect(reverse('authorization'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/Registration/registration.html', context)
"""
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Ваш аккаунт успешно активирован. Теперь вы можете войти.')
        return HttpResponseRedirect(reverse('authorization'))
    else:
        return HttpResponseBadRequest('Ссылка для активации недействительна.')


def register_view(request):
    if request.method == 'POST':
        # Получить данные из запроса
        data = json.loads(request.body)

        # Выполнить обработку регистрации
        # data содержит поля формы, например: data['phoneNumber'], data['lastName'], ...

        # Вернуть JSON-ответ
        response_data = {'message': 'Регистрация успешно выполнена'}
        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({'message': 'Метод не разрешен'}, status=405)