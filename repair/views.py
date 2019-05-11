from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

from .models import Phone, ProblemType, RepairCharge, Repairables

# Create your views here.
# def home(request, *args, **kwargs):
#     return render(request, 'repair/phone_list.html')

class PhoneCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "repair.can_add"
    model = Phone
    fields = ('name', "image")

class PhoneListView(ListView):
    model = Phone

class DashboardPhoneListView(ListView):
    model = Phone
    template_name = 'repair/dashboard_phone_list.html'

class PhoneDetailView(DetailView):
    model = Phone
    template_name = "repair/phone_detail.html"

class PhoneUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "repair.can_edit"
    model = Phone
    fields = ('name', "image")

class PhoneDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "repair.can_delete"
    model = Phone
    # success_url = "repair:home"

    def get_success_url(self):
        return reverse('repair:dashboard_phone_list')

class ProblemTypeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "repair.can_add"
    model = ProblemType
    fields = ('name', "description")

class ProblemTypeListView(ListView):
    model = ProblemType
    # template_name = "repair/phone_list.html"

class DashboardProblemTypeListView(ListView):
    model = ProblemType
    template_name = 'repair/dashboard_problem_type_list.html'

class ProblemTypeDetailView(DetailView):
    model = ProblemType
    template_name = "repair/phone_detail.html"

class ProblemTypeEditView(PermissionRequiredMixin, UpdateView):
    permission_required = "repair.can_edit"
    model = ProblemType
    fields = ('name', "description")

class ProblemTypeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "repair.can_delete"
    model = ProblemType
    # success_url = "repair:home"

    def get_success_url(self):
        return reverse('repair:dashboard_problem_type_list')

class ScheduleView(View):

    def get(self, request, *args, **kwargs):
        problem = request.session.get('problem')
        if not problem:
            problem_id = kwargs.get('pk')
            if problem_id:
                problem = problem_id
                request.session['problem'] = problem


        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signup'))

        # send_mail('Digi Compute Schedule confirmation',
        #           'You\'ve successfully claimed a repair schedule to digicompute.com. Click the following link to visit our site. {}'.format(request.get_host()),
        #           '95mainuddin@gmail.com', [request.user.email, ], fail_silently=False)
        # send_mail('Digi Compute Schedule confirmation',
        #           'A new user has claimed a schedule for his phone repair. {}'.format(request.get_host()),
        #           '95mainuddin@gmail.com', ['saifulbsl55@gmail.com', ], fail_silently=False)

        problem_type = get_object_or_404(ProblemType, id=problem)

        subject = "New Ticket From Digicompute"
        to = ['saifulbsl55@gmail.com']
        from_email = '95mainuddin@gmail.com'

        ctx = {
            'user': request.user.username,
            'phone_name': problem_type.phone.name,
            'problem_type': problem_type.name
        }

        message = get_template('email_template.html').render(ctx)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()

        return HttpResponseRedirect(reverse('repair:home'))


# def schedule_view(request, *args, **kwargs):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('repair:home'))
#     else:
#         return HttpResponseRedirect


