from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CustomUserCreationForm

# Create your views here.

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     # success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
#
#     def get_success_url(self):
#         username = self.request.POST['username']
#         password = self.request.POST['password']
#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#         problem = self.request.session.get('problem')
#         if problem:
#             return reverse_lazy('repair:schedule')
#         return reverse_lazy('repair:home')


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


    def get_success_url(self, user_data):
        username = user_data[0]
        password = user_data[1]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        problem = self.request.session.get('problem')
        if problem:
            return reverse('repair:schedule', kwargs={'pk': problem})
        return reverse('repair:home')

    def form_valid(self, form):
        user_data = (form['username'].value(), form['password1'].value())
        form.save()
        return HttpResponseRedirect(self.get_success_url(user_data))
