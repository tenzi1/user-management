from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):

#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'e.g user@example.com', 'class':'form-control'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
        

class CustomUserCreationForm(UserCreationForm):
    # password1 = forms.CharField(widget=forms.PasswordInput( attrs ={
    #     'class': 'form-control',

    #     'placeholder': 'Password'
    # }))
    # password2 = forms.CharField(widget=forms.PasswordInput( attrs = {
    #     'class': 'form-control',
    #     'placeholder': 'Confirm Password'
    # }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class':'form-control',
        #         'placeholder':'Username'
        #         }),
        #     'email': forms.EmailInput(attrs={
        #         'class':'form-control',
        #         'placeholder':'e.g. user@example.com'
        #         }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Password'
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Confirm Password'
        #     })

        # }


class CustomUserChangeForm(UserChangeForm):
    password=None
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login' )

    def clean_date_joined(self):
        if self.instance: 
            return self.instance.date_joined
        else: 
            return self.fields['date_joined']