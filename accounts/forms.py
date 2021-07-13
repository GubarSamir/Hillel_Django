from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AccountRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class AccountUpdateForm(UserChangeForm):
    # Чтоб убрать с формы поле password, раскоментируйте строку ниже
    password = None

    class Meta(UserChangeForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
