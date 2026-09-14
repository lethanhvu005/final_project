from django.contrib import messages
from django.shortcuts import render ,redirect
from django.contrib.auth import login ,logout,update_session_auth_hash
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .forms import UserForm,ChangePasswordForm
from .models import UserCustomer
from django.utils.encoding import force_bytes, force_str
from django.utils.http import (
    urlsafe_base64_encode,
    urlsafe_base64_decode,
)
def RegisterUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_superuser=False
            user.is_staff=False
            user.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'register.html',{'form':form})
def LoginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if request.user.is_staff:
                return redirect("admin:index")
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
def LogoutUser(request):
    logout(request)
    return redirect('home')
@login_required
def Account(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Bạn cần đăng nhập để vào Account!')
        return redirect('users:LoginUser')
    else:
        user = request.user
        if request.method == 'POST':
            form =UserForm(request.POST,request.FILES,instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                update_session_auth_hash(request,user)
                return redirect('users:Account')
        else:
            form =UserForm(instance=user)
    return render(request,'account.html',{'form':form})
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get(
            "forgot_password",
            "",
        ).strip()
        user = UserCustomer.objects.filter(
            email__iexact=email
        ).first()
        if user is None:
            return JsonResponse({
                "err": "Email không hợp lệ",
            })
        uidb64 = urlsafe_base64_encode(
            force_bytes(user.pk)
        )
        token = default_token_generator.make_token(user)
        path = reverse(
            "users:change_password",
            kwargs={
                "uidb64": uidb64,
                "token": token,
            },
        )
        reset_url = request.build_absolute_uri(path)
        subject = "Có vẻ bạn đã quên mật khẩu"
        from_email = settings.DEFAULT_FROM_EMAIL
        to = [user.email]
        text_content = (
            f"Nhấn vào đường dẫn sau để đổi mật khẩu: "
            f"{reset_url}"
        )
        html_content = render_to_string(
            "email/send_mail.html",
            {
                "name": user.username,
                "email": user.email,
                "reset_url": reset_url,
            },
        )
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            to,
        )
        msg.attach_alternative(
            html_content,
            "text/html",
        )
        msg.send()
        return JsonResponse({
            "success": "done",
        })

    return render(request, "forgot_password.html")
def change_password(request,uidb64,token):
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = UserCustomer.objects.get(id=user_id)
    except(  TypeError,
        ValueError,
        OverflowError,
        UserCustomer.DoesNotExist,):
        user = None
    if user is None:
        return render(
            request,
            "change_password.html",
            {
                "invalid_link": True,
            },
        )
    if not default_token_generator.check_token(
        user,
        token,
    ):
        return render(
            request,
            "change_password.html",
            {
                "invalid_link": True,
            },
        )

    if request.method == "POST":
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            new_password = form.cleaned_data[
                "password"
            ]
            user.set_password(new_password)
            user.save(update_fields=["password"])
            messages.success(
                request,
                "Đổi mật khẩu thành công.",
            )
            return redirect("users:LoginUser")
    else:
        form = ChangePasswordForm()
    return render(
        request,
        "change_password.html",
        {
            "form": form,
            "invalid_link": False,
        },
    )

        