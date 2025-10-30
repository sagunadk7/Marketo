from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    """Forms for creating new users in admin - includes repeated passwords fields"""
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomUser
        fields = ("phone_number",)

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Password don't match")
        return p2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class CustomUserChangeForm(forms.ModelForm):
    """ Form for updating users in admin - shows the hashed password as read-only"""
    password = ReadOnlyPasswordHashField(label="Password", help_text ="Raw passwords are not stored so there is no way to see this user's password,")

    class Meta:
        model = CustomUser
        fields = ("phone_number","password","is_active","is_staff","is_superuser")

    @property
    def clean_password(self):
        return self.initial.get("password")


