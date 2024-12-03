from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """ customized user creation form """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name',)


class CustomUserChangeForm(UserChangeForm):
    """ custom for to modifiy existing user model """

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
