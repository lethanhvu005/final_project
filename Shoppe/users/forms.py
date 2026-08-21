from django.contrib.auth import get_user_model
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
     
    