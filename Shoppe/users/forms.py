from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django import forms
User = get_user_model()
class UserForm(forms.ModelForm):
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label="Xác nhận mật khẩu")
    class Meta():
        model = User
        fields =['username','email','password','confirmPassword','avatar','first_name','last_name','id_country']   
        widgets ={
            'password':forms.PasswordInput(),
            'avatar': forms.FileInput()
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')
        if password != confirmPassword:
            raise forms.ValidationError(
                'Xác nhận lại mật khẩu không đúng'
            )
     
class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        label="Mật khẩu mới",
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        label="Xác nhận mật khẩu",
        widget=forms.PasswordInput(),
    )
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    "Hai mật khẩu không giống nhau."
                )
            validate_password(password)
        return cleaned_data