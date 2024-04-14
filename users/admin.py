from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


# Register your models here.

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'phone', 'avatar')

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "The two password fields didn't match."
            )
        return cleaned_data

    def save_as_user(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'phone', 'avatar')

    fieldsets = (
        (None, {'fields': ('username', 'phone', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'avatar', 'password', 'confirm_password'),
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    search_fields = ('username', 'phone')
    ordering = ('id', 'username')

    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
