from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from . import forms
from blog import models

# Create your views here.


class UserRegisterView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = forms.UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = forms.PasswordChnagingForm
    success_url = reverse_lazy('password_success')


class PasswordSuccess(TemplateView):
    template_name = 'registration/password_scucess.html'


class ProfilePageView(DetailView):
    model = models.UserProfile
    template_name = 'registration/user_prfoile.html'

    def get_context_data(self, **kwargs):
        # user_data = models.UserProfile.objects.all()
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(models.UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(UpdateView):
    model = models.UserProfile
    form_class = forms.ProfilePageEditForm
    template_name = 'registration/edit_prfoile_page.html'
    # fields = ['bio', 'profile_pic', 'linkedin_url',
    #           'instagram_url', 'twitter_url', 'github_url', 'mobile_number', 'country', 'state', 'city', 'postal_code']
    success_url = reverse_lazy('home')


class CreateProfilePageView(CreateView):
    model = models.UserProfile
    template_name = 'registration/create_user_profile_page.html'

    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
