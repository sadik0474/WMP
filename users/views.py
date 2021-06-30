import django
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView,LogoutView,PasswordResetView,PasswordChangeView,PasswordResetConfirmView)
from django.views.generic import TemplateView,RedirectView,DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


from .forms import RegistrationForm,ContactForm
class HomeTemplateView(TemplateView):

    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        if self.request.user.is_authenticated:
            print(self.request)
            # context = Search÷Form()
        return context
    

class RegisterFormView(FormView):
    template_name='register.html'
    form_class=RegistrationForm
    success_url = reverse_lazy('users:home')
    http_method_names = ['get', 'post']

    def get(self, request, *args: str, **kwargs) :
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)
        return super().form_valid(form)

class LoginFormView(LoginView):
    template_name='login.html'
    form_class=AuthenticationForm
    http_method_names = ['get', 'post']
    def get(self, request, *args: str, **kwargs) :
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class LogoutFormView(LogoutView):
    http_method_names=['get']
    next_page = reverse_lazy('home')

def ContactView(request):
    if request.method == 'POST':
        form=ContactForm(request.post)
        if form.is_valid():
            return reverse_lazy('home')