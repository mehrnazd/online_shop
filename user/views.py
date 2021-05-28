from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


from .forms import LoginForm, CustomerSignupForm, SupplierSignupForm
from .models import CustomerProfile

User = get_user_model()


class UserTypeSignUp(View):
    form = None
    template_name = None

    def get_type_form(self):
        return self.form

    def get(self, request):
        form = self.get_type_form()()
        context = {
            'form': form
        }
        #html
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.get_type_form()(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        #html
        return render(request, self.template_name, context)

class CustomerSignup(UserTypeSignUp):
    form = CustomerSignupForm
    template_name = 'signup.html'


class SupplierSignup(UserTypeSignUp):
    form = SupplierSignupForm
    template_name = 'signup_sup.html'


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            # logout(request)
            return redirect('/')
        form = LoginForm()
        next_url = request.GET.get('next', '')
        context = {
            'form': form,
            'next_url': next_url
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "login successfully!")
                next_url = request.GET.get('next', None)
                if next_url:
                    return redirect(next_url)
                return redirect('/')
            else:
                return redirect('login')



def Logout(request):
    logout(request)
    return redirect('login')

@method_decorator(csrf_exempt, name="dispatch")
class ShowCustomerProfile(LoginRequiredMixin, View):
    login_url = "/profile/user/"
    def get(self, request):
        if CustomerProfile.objects.filter(user=request.user).exists():
            profile_object = request.user.customer_profile
        else:
            profile_object = CustomerProfile.objects.create(user=request.user)

        context = {
            'profile_object': profile_object,
        }
        return render(request, 'user/profile.html', context)



class EditCustomerProfile(TemplateView):
    template_name = 'user/profile_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_object'] = self.request.user
        return context



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })



