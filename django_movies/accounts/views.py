from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from accounts.forms import SubmittableAuthenticationForm, SubmittablePasswordChangeForm
from django.urls import reverse_lazy


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class = SubmittablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class SuccessMessagedLogoutView(LogoutView):
    def get_next_page(self):
        result = super().get_next_page()
        messages.success(self.request, 'Successfully logged out!')
        return result