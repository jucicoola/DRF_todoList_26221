# 1 Standard Library : 없음

# 2 Third-party: django 
from django.views.generic import TemplateView

# 3 Local application : 없음

class SignupPageView(TemplateView):
    template_name = "accounts/signup.html"


class LoginPageView(TemplateView):
    template_name = "accounts/login.html"

