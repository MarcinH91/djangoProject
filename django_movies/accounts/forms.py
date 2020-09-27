from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea

from accounts.models import Profile


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SignUpForm(SubmittableForm, UserCreationForm):
    shoes = CharField(
        label='Tell me your shoes size. (for ex. 40)',
        widget=Textarea,
        min_length=1,
    )
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit)
        shoes = self.cleaned_data['shoes']
        profile = Profile(shoes=shoes, user=user)
        profile.save()
        return user

class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass

class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass
