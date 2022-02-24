from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from allauth.account.views import SignupView
from .forms import CustomUserCreationForm
from django.contrib import messages

class CustomSignUpView(SignupView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'
class HomePageView(TemplateView):
    template_name = 'home.html'

def signupPage(request):        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
            messages.success(request, 'Account was created for ' + user)
            return redirect('account_login')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'account/signup.html', context)